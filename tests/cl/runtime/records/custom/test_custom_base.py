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

import pytest
from stubs.cl.runtime.records.custom.stub_custom_base import StubCustomBase


def test_smoke():
    """Smoke test."""

    # Create test base_record and populate with sample data
    record = StubCustomBase()

    # Test type and key
    key = record.get_key()
    assert key == (StubCustomBase, "abc", 123)

    # Test roundtrip serialization
    packed_key, packed_dict = record.pack()
    assert packed_key == key

    record_clone = StubCustomBase(**packed_dict)
    clone_key, clone_dict = record_clone.pack()
    assert clone_key == key
    assert len(clone_dict) == 3
    assert clone_dict == packed_dict


if __name__ == "__main__":
    pytest.main([__file__])