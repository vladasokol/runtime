# Copyright (C) 2023-present The Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from itertools import groupby
from typing import Iterable

from cl.runtime import DataSource
from cl.runtime.records.protocols import KeyProtocol, RecordProtocol, is_key
from cl.runtime.serialization.flat_dict_serializer import FlatDictSerializer
from cl.runtime.serialization.string_serializer import StringSerializer
from cl.runtime.storage.data_source_types import TDataset, TIdentity, TQuery
from cl.runtime.storage.sql.sqlite_schema_manager import SqliteSchemaManager


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


@dataclass(slots=True, kw_only=True, frozen=True)
class SqliteDataSource(DataSource):

    db_name: str = 'test_db.sqlite'
    _connection: sqlite3.Connection = None
    _schema_manager: SqliteSchemaManager = None

    def __post_init__(self) -> None:
        """Initialize private attributes."""

        # TODO: Implement dispose logic
        # Use setattr to initialize attributes in a frozen object
        object.__setattr__(self, "_connection", sqlite3.connect(self.db_name))
        self._connection.row_factory = dict_factory
        object.__setattr__(
            self, "_schema_manager", SqliteSchemaManager(sqlite_connection=self._connection)
        )

    def batch_size(self) -> int:
        pass

    def load_one(self, record_or_key: KeyProtocol | None, *, dataset: TDataset = None,
                 identities: Iterable[TIdentity] | None = None) -> RecordProtocol | None:
        pass

    # TODO (Roman): maybe return mapping {key: record} in load_many
    def load_many(self, records_or_keys: Iterable[KeyProtocol | None] | None, *, dataset: TDataset = None,
                  identities: Iterable[TIdentity] | None = None) -> Iterable[RecordProtocol | None] | None:

        serializer = FlatDictSerializer()
        key_serializer = StringSerializer()

        # it is important to preserve the original order of records_or_keys.
        # itertools.groupby works just like that and does not violate the order.

        # group by key type and then by it is key or record. if not keys - return themselves.
        for key_type, records_or_keys_group in groupby(records_or_keys, lambda x: x.get_key_type()):
            for is_key_group, keys in groupby(records_or_keys_group, lambda x: is_key(x)):

                if not is_key_group:
                    yield from keys

                serialized_keys = tuple(key_serializer.serialize_key(key) for key in keys)

                value_placeholders = ", ".join(["?"]*len(serialized_keys))
                table_name = self._schema_manager.table_name_for_type(key_type)
                sql_statement = f'SELECT * FROM "{table_name}" WHERE _key IN ({value_placeholders});'

                cursor = self._connection.cursor()
                cursor.execute(sql_statement, serialized_keys)
                reversed_columns_mapping = {v: k for k, v in self._schema_manager.get_columns_mapping(key_type).items()}
                for data in cursor.fetchall():
                    del data['_key']
                    # TODO (Roman): select needed columns on db side.
                    data = {reversed_columns_mapping[k]: v for k, v in data.items() if v is not None}

                    yield serializer.deserialize_data(data)

    def load_by_query(self, query: TQuery, *, dataset: TDataset = None,
                      identities: Iterable[TIdentity] | None = None) -> Iterable[RecordProtocol]:
        pass

    def save_one(self, record: RecordProtocol | None, *, dataset: TDataset = None, identity: TIdentity = None) -> None:
        return self.save_many([record])

    def save_many(
            self, records: Iterable[RecordProtocol], *, dataset: TDataset = None, identity: TIdentity = None
    ) -> None:

        serializer = FlatDictSerializer()
        key_serializer = StringSerializer()

        grouped_records = defaultdict(list)

        # TODO (Roman): improve grouping
        for record in records:
            grouped_records[record.get_key_type()].append(record)

        for key_type, records_group in grouped_records.items():

            serialized_records = []

            for rec in records_group:
                serialized_record = serializer.serialize_data(rec, is_root=True)
                serialized_record["_key"] = key_serializer.serialize_key(rec)
                serialized_records.append(serialized_record)

            all_fields = list({k for rec in serialized_records for k in rec.keys()})

            sql_values = tuple(
                serialized_record[k] if k in serialized_record else None
                for serialized_record in serialized_records
                for k in all_fields
            )

            columns_mapping = self._schema_manager.get_columns_mapping(key_type)
            quoted_columns = [f'"{columns_mapping[field]}"' for field in all_fields]
            columns_str = ", ".join(quoted_columns)

            value_placeholders = ", ".join([f"({', '.join(['?']*len(all_fields))})" for _ in range(len(records_group))])

            table_name = self._schema_manager.table_name_for_type(key_type)

            self._schema_manager.create_table(table_name, columns_mapping.values(), if_not_exists=True)

            sql_statement = f"REPLACE INTO \"{table_name}\" ({columns_str}) VALUES {value_placeholders};"

            cursor = self._connection.cursor()
            cursor.execute(sql_statement, sql_values)
            self._connection.commit()

    def delete_many(self, keys: Iterable[KeyProtocol] | None, *, dataset: TDataset = None,
                    identities: Iterable[TIdentity] | None = None) -> None:
        pass

    def delete_db(self) -> None:
        """Delete all tables and indexes on current db instance."""

        # delete several time because tables depended on foreign key can not be deleted before related tables exist.
        while True:

            if not self._connection:
                break

            cursor = self._connection.cursor()

            # delete tables
            delete_all_tables = [
                str(next(iter(x.values())))
                for x in cursor.execute(
                    "select 'drop table ' || name || ';' from sqlite_master where type = 'table';",
                ).fetchall()
            ]

            for delete_statement in delete_all_tables:
                cursor.execute(delete_statement)

            # delete indexes
            delete_all_indexes = [
                str(next(iter(x.values())))
                for x in cursor.execute(
                    "select 'drop index ' || name || ';' from sqlite_master where type = 'index';",
                ).fetchall()
            ]

            for delete_statement in delete_all_indexes:
                cursor.execute(delete_statement)

            # stop if nothing to delete
            if len(delete_all_tables) == 0 and len(delete_all_indexes) == 0:
                break

        # close connection
        if self._connection:
            self._connection.close()

        # TODO (Roman): delete db file