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
from cl.runtime.prebuild.init_files import check_init_files
from pathlib import Path


def test_init_files():
    """Prebuild test to check that __init__.py is present in all code directories."""

    # Project root assuming the script is located in project_root/scripts
    project_root = Path(__file__).parents[4]

    # Relative paths to source directories
    relative_paths = ["cl", "stubs"]

    # Absolute paths to source directories
    root_paths = [project_root / x for x in relative_paths]

    # Get the list of missing init files are present without fixing the problem
    missing_files = check_init_files(root_paths, apply_fix=False)

    # Confirm that there are no missing files
    assert not missing_files


if __name__ == "__main__":
    pytest.main([__file__])