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

from cl.runtime.storage.key import Key
from cl.runtime.storage.attrs import data_field, data_class
from stubs.cl.runtime.storage.attrs.stub_attrs_record_key import StubAttrsRecordKey


@data_class
class StubAttrsNestedFieldsKey(Key):
    """Record where the key is composite and includes other keys."""

    primitive: str = data_field(default="abc")
    """String key element."""

    embedded_1: StubAttrsRecordKey = data_field(factory=StubAttrsRecordKey)
    """Embedded key 1."""

    embedded_2: StubAttrsRecordKey = data_field(factory=StubAttrsRecordKey)
    """Embedded key 2."""