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

from __future__ import annotations
from typing import Any, Dict, Optional
from cl.runtime.data.context import Context
from cl.runtime.data.key import Key
from cl.runtime.data.record import Record


class StubNoKeyRecord(Key):
    """Stub record used in tests."""

    key_field_str: Optional[str]
    """First primary key attribute."""

    key_field_int: Optional[int]
    """Second primary key attribute."""

    base_field_str: Optional[str]
    """String attribute of base class."""

    base_field_float: Optional[float]
    """Float attribute of base class."""

    def __init__(self):
        """Initialize instance attributes."""
        self.key_field_str = 'abc'
        self.key_field_int = 123
        self.base_field_str = 'def'
        self.base_field_float = 4.56

    def to_dict(self) -> Dict[str, Any]:
        """Serialize self as dictionary (may return shallow copy)."""
        return {
            'key_field_str': self.key_field_str,
            'key_field_int': self.key_field_int,
            'base_field_str': self.base_field_str,
            'base_field_float': self.base_field_float,
        }

    def get_table(self) -> str:
        """Name of the database table where the record for this key is stored."""
        return f"{type(self).__module__}.{type(self).__name__}"

    def get_key(self) -> str:
        """Key as string in semicolon-delimited string format without table name."""
        return f"{self.key_field_str};{self.key_field_int}"

