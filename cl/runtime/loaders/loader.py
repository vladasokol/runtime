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

from abc import ABC
from abc import abstractmethod
from cl.runtime.records.record_mixin import RecordMixin
from cl.runtime.storage.protocols import DataSourceProtocol
from cl.runtime.loaders.loader_key import LoaderKey
from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class Loader(LoaderKey, RecordMixin[LoaderKey], ABC):
    """Load records into the specified data source."""

    def get_key(self) -> LoaderKey:
        return LoaderKey(loader_id=self.loader_id)

    @abstractmethod
    def load(self, data_source: DataSourceProtocol) -> None:
        """Load one or multiple records into the specified data source."""