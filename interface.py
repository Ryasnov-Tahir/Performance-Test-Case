"""Содержит функцию для разбора аргументов командной строки."""

import argparse


def arg_parse() -> argparse.Namespace:
    """
    Создаёт и возвращает объект с аргументами командной строки.

    :return: Namespace.
    """
    parser = argparse.ArgumentParser(
        description="Developer performance report generator"
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name (e.g. performance)"
    )

    return parser.parse_args()
