"""Содержит абстрактный класс BaseReport."""

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseReport(ABC):
    """Базовый класс для всех отчётов."""

    def __init__(self, csv_data: List[Dict[str, str]]):
        """
        Init отчета с данными.

        :param csv_data: Список словарей, содержащих данные в формате CSV.
        :type csv_data: List[Dict[str, str]]
        """
        self.csv_data = csv_data

    @abstractmethod
    def generate(self):
        """
        Генерация отчёта.

        :return: Список словарей с результатами отчёта.
        :rtype: List[Dict]
        """
        raise NotImplementedError(
            "Метод generate() должен быть реализован в дочернем классе отчёта"
        )
