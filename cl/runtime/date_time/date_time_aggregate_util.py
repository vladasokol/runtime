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

from datetime import date, datetime, time
from typing import Any, Dict, Optional, Type

import pytz

from cl.runtime.date_time.aggregation_class import aggregation_class
from cl.runtime.date_time.base_date_time_util import BaseDateTimeUtil
from cl.runtime.primitive.date_util import DateUtil
from cl.runtime.primitive.date_time_util import DateTimeUtil
from cl.runtime.primitive.time_util import TimeUtil


@aggregation_class
class DateTimeAggregateUtil:  # TODO: Refactor to make the API similar to other utilities
    """General util class for date time types."""

    """
    Mandatory dictionary for aggregation_class. Define relations between types and util classes for this types.
    key - type;
    value - util class for type.
    """
    _utils_map: Dict[Type, BaseDateTimeUtil] = {
        date: DateUtil,
        time: TimeUtil,
        datetime: DateTimeUtil,
    }

    """
    Mandatory dictionary for aggregation_class. Used to generate aggregation methods.
    key - name of method in interface;
    value - name of aggregation method.
    """
    _methods_map: Dict[str, str] = {
        'validate': 'validate_expected',
        'to_iso_int': 'value_to_iso_int',
        'from_iso_int': 'value_from_iso_int',
        'to_str': 'value_to_str',
        'from_str': 'value_from_str',
    }

    @staticmethod
    def validate_expected(value: Any, expected_type: type) -> None:
        """
        Aggregation method for interface method 'validate'.
        The implementation will be generated by the aggregation_class decorator.
        """
        pass

    @staticmethod
    def value_to_iso_int(value: Any) -> int:
        """
        Aggregation method for interface method 'to_iso_int'.
        The implementation will be generated by the aggregation_class decorator.
        """
        pass

    @staticmethod
    def value_from_iso_int(iso_int: int, expected_type: type) -> Any:
        """
        Aggregation method for interface method 'from_iso_int'.
        The implementation will be generated by the aggregation_class decorator.
        """
        pass

    @staticmethod
    def value_to_str(value: Any) -> str:
        """
        Aggregation method for interface method 'to_str'.
        The implementation will be generated by the aggregation_class decorator.
        """
        pass

    @staticmethod
    def value_from_str(value_str: str, expected_type: type) -> Any:
        """
        Aggregation method for interface method 'from_str'.
        The implementation will be generated by the aggregation_class decorator.
        """
        pass

    @staticmethod
    def create_date(year: int, month: int, day: int) -> date:
        """Factory method to create datetime.date."""
        result: date = date(year, month, day)
        return result

    @staticmethod
    def create_time(hour: int, minute: int, second: int, millisecond: Optional[int] = None) -> time:
        """Factory method to create datetime.time."""
        if millisecond is None:
            millisecond = 0
        result: time = time(hour, minute, second, 1000 * millisecond)
        return result

    @staticmethod
    def create_datetime(
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        millisecond: Optional[int] = None,
    ) -> datetime:
        """Factory method to create datetime.datetime."""

        if millisecond is None:
            millisecond = 0

        result = datetime(
            year,
            month,
            day,
            hour,
            minute,
            second,
            microsecond=1000 * millisecond,
            tzinfo=pytz.UTC,
        )
        return result