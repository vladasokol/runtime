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

from cl.runtime.records.dataclasses.dataclass_mixin import DataclassMixin
from cl.runtime.records.dataclasses.dataclass_mixin import datafield
from dataclasses import dataclass
from typing import Tuple
from typing import Type

TypeDeclKey = Tuple[Type["TypeDecl"], str]


@dataclass
class TypeDecl(DataclassMixin):
    """Base class of type declaration in schema."""

    type_id: str = datafield()
    """
    Unique dot-delimited type identifier. May optionally include package alias.
    Used for table name in storage, and _type field in JSON.
    """

    label: str = datafield(optional=True)
    """Readable type label in the front end."""

    def get_key(self) -> TypeDeclKey:
        return type(self), self.type_id