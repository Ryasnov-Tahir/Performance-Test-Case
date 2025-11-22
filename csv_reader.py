"""Содержит функцию для чтения CSV-файлов."""

import csv
from typing import List, Dict


def csv_reader(paths: List[str]) -> List[Dict[str, str]]:
    """
    Читает один или несколько scv-файлов.

    :param paths: Список путей к scv-файлам.
    :return: Список словарей с данными из scv.
    :raises FileNotFoundError: Если один из файлов не найден.
    """
    rows = []

    for path in paths:
        try:
            with open(path, newline="", encoding="utf-8") as scv_file:
                reader = csv.DictReader(scv_file)
                rows.extend(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")

    return rows
