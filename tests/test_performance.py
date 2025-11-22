"""Тесты для проверки отчёта PerformanceReport."""

from reports.performance import PerformanceReport

AWAITING_VALUE = 4.7


def test_performance_report(mock_report):
    """Проверяет корректность расчёта средней производительности."""
    report = PerformanceReport(mock_report)
    test_results = report.generate()

    assert len(test_results) == 2

    backend = None
    for i_res in test_results:
        if i_res["position"] == "Backend Developer":
            backend = i_res
            break

    assert backend is not None, "Backend Developer not found in results"
    assert backend["avg_performance"] == AWAITING_VALUE
