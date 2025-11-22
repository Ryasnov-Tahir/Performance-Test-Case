"""Содержит тест для файла csv_reader."""

from csv_reader import csv_reader


def test_read_csv_files(tmp_path):
    """Проверяет работу csv_reader."""
    csv_content = "name,position,performance\n" "Alex,Backend Developer,4.8\n"

    test_file = tmp_path / "tmp.csv"
    test_file.write_text(csv_content, encoding="utf-8")

    test_result = csv_reader([str(test_file)])
    assert len(test_result) == 1
    assert test_result[0]["position"] == "Backend Developer"
