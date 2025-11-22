"""Файл для хранения константы с доступными отчетами."""

from types import MappingProxyType
from reports.performance import PerformanceReport

REGISTRY = MappingProxyType({"performance": PerformanceReport})
