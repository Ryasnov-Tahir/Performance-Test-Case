"""Содержит точку входа для работы программы."""

from tabulate import tabulate
from csv_reader import csv_reader
from reports.registry import REGISTRY
from interface import arg_parse


def main():
    """
    Основная функция запуска программы.

    :return: Список словарей с результатами отчёта, либо None при ошибке.
    """
    args = arg_parse()

    if args.report not in REGISTRY:
        print(
            f"Неизвестный отчет: {args.report}."
            f"Доступны: {list(REGISTRY.keys())}"
        )
        return

    try:
        file_data = csv_reader(args.files)
    except FileNotFoundError as error:
        print(error)
        return

    report_class = REGISTRY[args.report]
    report_obj = report_class(file_data)

    result_data = report_obj.generate()

    if not result_data:
        print("Нет данных для отображения.")
        return

    idx = 1
    for row in result_data:
        temp = dict(row)
        row.clear()
        row[""] = idx
        for key in temp:
            row[key] = temp[key]
        idx += 1

    headers = []
    for key in result_data[0].keys():
        headers.append(key)

    print(tabulate(result_data, headers="keys", tablefmt="simple"))


if __name__ == "__main__":
    main()
