"""Содержит тесты для проверки работы main.py."""

import main
from unittest.mock import patch

ARG_PARSE_PATH = "main.arg_parse"
CSV_READER_PATH = "main.csv_reader"


def test_unknown_report(mock_report, capfd):
    """Проверка вывода при неизвестном названии отчёта."""
    with patch(ARG_PARSE_PATH) as mock_args:
        mock_args.return_value.report = "unknown_report"
        mock_args.return_value.files = []
        main.main()
        out, _ = capfd.readouterr()
        assert "Неизвестный отчет: unknown_report" in out


def test_file_not_found(capfd):
    """Проверка обработки FileNotFoundError при несуществующем файле."""
    with patch(ARG_PARSE_PATH) as mock_args:
        mock_args.return_value.report = "performance"
        mock_args.return_value.files = ["nonexistent.csv"]
        with patch(
                CSV_READER_PATH,
                side_effect=FileNotFoundError(
                    "File not found: nonexistent.csv"
                )
        ):
            main.main()
        out, _ = capfd.readouterr()
        assert "File not found: nonexistent.csv" in out


def test_successful_report_print(mock_report, capfd):
    """Проверка успешного вывода отчёта в консоль."""
    from reports.performance import PerformanceReport

    with patch(ARG_PARSE_PATH) as mock_args, \
         patch(CSV_READER_PATH, return_value=mock_report):
        mock_args.return_value.report = "performance"
        mock_args.return_value.files = ["dummy.csv"]

        with patch.object(PerformanceReport, "generate", return_value=[
            {"position": "Backend Developer", "avg_performance": 4.7},
            {"position": "QA Engineer", "avg_performance": 4.5}
        ]):
            main.main()
            out, _ = capfd.readouterr()
            assert "Backend Developer" in out
            assert "4.7" in out


def test_empty_report_output(capfd):
    """Проверка вывода при пустом результате generate()."""
    from reports.performance import PerformanceReport

    with (
        patch(ARG_PARSE_PATH) as mock_args,
        patch(CSV_READER_PATH, return_value=[{}])
    ):
        mock_args.return_value.report = "performance"
        mock_args.return_value.files = ["dummy.csv"]

        with patch.object(PerformanceReport, "generate", return_value=[]):
            main.main()
            out, _ = capfd.readouterr()
            assert "Нет данных для отображения." in out
