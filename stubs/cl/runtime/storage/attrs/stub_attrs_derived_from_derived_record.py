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
from typing import Optional
from cl.runtime.primitive.date_time_util import DateTimeUtil
from cl.runtime.primitive.date_util import DateUtil
from cl.runtime.storage.attrs import data_field, data_class
from stubs.cl.runtime.storage.attrs.stub_attrs_derived_record import StubAttrsDerivedRecord


@data_class
class StubAttrsDerivedFromDerivedRecord(StubAttrsDerivedRecord):
    """Two levels in inheritance hierarchy away from StubAttrsRecord."""

    derived_from_derived_field: str = data_field(factory="derived_from_derived")
    """Stub field."""
