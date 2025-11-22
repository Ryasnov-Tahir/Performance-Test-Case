"""Содержит фикстуру для тестов проекта."""

import pytest


@pytest.fixture
def mock_report():
    """
    Фикстура с примером данных сотрудников для тестирования отчётов.

    :return: Список словарей
    :rtype: List[Dict[str, str]]
    """
    return [
        {"position": "Backend Developer", "performance": "4.8"},
        {"position": "Backend Developer", "performance": "4.6"},
        {"position": "QA Engineer", "performance": "4.5"},
    ]
