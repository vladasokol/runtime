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
from dataclasses import dataclass
from cl.runtime.plots.bar.bar_plot_style_key import BarPlotStyleKey
from cl.runtime.records.record_mixin import RecordMixin


@dataclass(slots=True, kw_only=True)
class BarPlotStyle(BarPlotStyleKey, RecordMixin[BarPlotStyleKey], ABC):
    """Color and layout options for BarPlot."""

    axis_origin: float = 0.
    """Origin of axis (defaults to zero if not specified)."""

    axis_min: float = 0.
    """Lower limit of axis range (defaults to zero if not specified). Data outside the range is permitted."""

    axis_max: float | None = None
    """Upper limit of axis (maximum data value is used when not specified). Data outside the range is permitted."""

    def get_key(self) -> BarPlotStyleKey:
        return BarPlotStyleKey(style_id=self.style_id)