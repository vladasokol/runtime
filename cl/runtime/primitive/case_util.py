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

import inflection


class CaseUtil:
    """Utilities for case conversion and other operations on string."""

    @classmethod
    def pascal_to_snake_case(cls, value: str) -> str:
        """Convert PascalCase to snake_case using custom rule for separators in front of digits."""
        # TODO: Implement custom rule for separators in front of digits
        cls.check_pascal_case(value)
        result = inflection.underscore(value)  # TODO: Replace by custom method
        return result

    @classmethod
    def upper_to_snake_case(cls, value: str) -> str:
        """Convert UPPER_CASE to snake_case using custom rule for separators in front of digits."""
        # TODO: Implement custom rule for separators in front of digits
        cls.check_upper_case(value)
        return value.lower()  # TODO: Replace by custom method

    @classmethod
    def snake_to_pascal_case(cls, value: str) -> str:
        """Convert snake_case to PascalCase using custom rule for separators in front of digits."""
        # TODO: Implement custom rule for separators in front of digits
        cls.check_snake_case(value)
        # TODO: Replace by custom method
        result = ".".join(inflection.camelize(token, uppercase_first_letter=True) for token in value.split("."))
        return result

    @classmethod
    def upper_to_pascal_case(cls, value: str) -> str:
        """Convert UPPER_CASE to PascalCase using custom rule for separators in front of digits."""
        # TODO: Implement custom rule for separators in front of digits
        cls.check_upper_case(value)
        return cls.snake_to_pascal_case(value.lower())  # TODO: Replace by custom method

    @classmethod
    def pascal_to_upper_case(cls, value: str) -> str:
        """Convert PascalCase to UPPER_CASE using custom rule for separators in front of digits."""
        # TODO: Implement custom rule for separators in front of digits
        cls.check_pascal_case(value)
        snake_case_value = cls.pascal_to_snake_case(value)  # TODO: Replace by custom method
        return snake_case_value.upper()  # TODO: Replace by custom method

    @classmethod
    def check_snake_case(cls, value: str) -> None:
        """Error message if arg is not snake_case or does not follow custom rule for separators in front of digits."""
        # TODO: Extend check to include custom rule
        cls._check_no_space(value, "snake_case")
        cls._check_no_upper(value, "snake_case")

    @classmethod
    def check_pascal_case(cls, value: str) -> None:
        """Error message if arg is not PascalCase or does not follow custom rule for separators in front of digits."""
        # TODO: Extend check to include custom rule
        cls._check_no_space(value, "PascalCase")
        cls._check_no_underscore(value, "PascalCase")

    @classmethod
    def check_title_case(cls, value: str) -> None:
        """Error message if arg is not Title Case or does not follow custom rule for separators in front of digits."""
        # TODO: Extend check to include custom rule
        cls._check_no_underscore(value, "Title Case")

    @classmethod
    def check_upper_case(cls, value: str) -> None:
        """Error message if arg is not UPPER_CASE or does not follow custom rule for separators in front of digits."""
        # TODO: Extend check to include custom rule
        cls._check_no_space(value, "UPPER_CASE")
        cls._check_no_lower(value, "UPPER_CASE")

    @classmethod
    def _check_no_space(cls, value: str, format_: str) -> None:
        """Error message stating string does not follow format if it contains a space."""
        if " " in value:
            raise RuntimeError(f"String {value} is not {format_} because it contains a space.")

    @classmethod
    def _check_no_underscore(cls, value: str, format_: str) -> None:
        """Error message stating string does not follow format if it contains an underscore."""
        if "_" in value:
            raise RuntimeError(f"String {value} is not {format_} because it contains an underscore.")

    @classmethod
    def _check_no_lower(cls, value: str, format_: str) -> None:
        """Error message stating string does not follow format if it contains a lowercase character."""
        if any(char.islower() for char in value):
            raise RuntimeError(f"String {value} is not {format_} because it contains a lowercase character.")

    @classmethod
    def _check_no_upper(cls, value: str, format_: str) -> None:
        """Error message stating string does not follow format if it contains an uppercase character."""
        if any(char.isupper() for char in value):
            raise RuntimeError(f"String {value} is not {format_} because it contains a uppercase character.")