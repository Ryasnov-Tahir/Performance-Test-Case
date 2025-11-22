"""Содержит класс PerformanceReport для отчета о производительности."""

from typing import Dict
from collections import defaultdict
from reports.base import BaseReport


def _sort_key(report_dict: Dict[str, float]) -> float:
    """
    Функция-ключ для сортировки результатов отчёта.

    :param report_dict: Словарь с отчетом.
    :return: Средняя производительность.
    """
    return report_dict["avg_performance"]


class PerformanceReport(BaseReport):
    """
    Отчёт по эффективности разработчиков.

    Группирует сотрудников по должности и вычисляет среднюю производительность.
    """

    def generate(self):
        """
        Генерация отчёта.

        :return: Список словарей с результатами отчёта.
        :rtype: List[Dict[str, float]]
        """
        totals = defaultdict(list)

        for row in self.csv_data:
            position = row.get("position", "").strip()
            perf_raw = row.get("performance", "").strip()
            if position == "" or perf_raw == "":
                continue
            try:
                performance = float(perf_raw)
            except ValueError:
                continue

            totals[position].append(performance)

        result_list = []
        for position, perf_values in totals.items():
            avg_perf = sum(perf_values) / len(perf_values)
            result_list.append(
                {"position": position, "avg_performance": round(avg_perf, 2)}
            )

        result_list.sort(key=_sort_key, reverse=True)

        return result_list
