"""Тесты для проверки функции разбора аргументов командной строки."""

import sys
import pytest
from interface import arg_parse


def test_arg_parse(monkeypatch):
    """Проверяет корректный разбор аргументов командной строки."""
    test_args = [
        "main.py",
        "--files",
        "file1.csv",
        "file2.csv",
        "--report",
        "performance",
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    args = arg_parse()

    assert args.files == ["file1.csv", "file2.csv"]
    assert args.report == "performance"


def test_arg_parse_missing_files(monkeypatch):
    """Проверка отсутствия аргумента --files."""
    test_args = ["main.py", "--report", "performance"]
    monkeypatch.setattr(sys, "argv", test_args)

    with pytest.raises(SystemExit):
        arg_parse()


def test_arg_parse_missing_report(monkeypatch):
    """Проверка отсутствия аргумента --report."""
    test_args = ["main.py", "--files", "file1.csv"]
    monkeypatch.setattr(sys, "argv", test_args)

    with pytest.raises(SystemExit):
        arg_parse()
