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
from typing import TYPE_CHECKING, Union
from cl.runtime.storage.attrs import data_field, data_class
from cl.runtime.storage.data import Data
if TYPE_CHECKING:
    from stubs.cl.runtime.storage.attrs.stub_attrs_cyclic_b import StubAttrsCyclicB


@data_class
class StubAttrsCyclicA(Data):
    """Stub class A with a field whose type is key for class B."""

    b: StubAttrsCyclicB = data_field()
    """Key for class B."""

    @staticmethod
    def create() -> StubAttrsCyclicA:
        """Create an instance of this class populated with sample data."""

        # Import inside function to avoid cyclic reference error
        from stubs.cl.runtime.storage.attrs.stub_attrs_cyclic_b import StubAttrsCyclicB

        obj = StubAttrsCyclicA()
        obj.b = StubAttrsCyclicB()
        return obj