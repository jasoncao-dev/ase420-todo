import pytest
from src.Formatter import Formatter


def test_format_report():
    formatter = Formatter()
    report_data = [(1, '2023/01/01', '10:00', '11:00', 'New Year Planning', 'PLANNING')]

    result = formatter.format_report(report_data)
    expected_result = "2023/01/01 10:00 11:00 New Year Planning PLANNING"
    assert result == expected_result

def test_format_query_results():
    formatter = Formatter()
    query_data = [(1, '2023/04/01', '10:00', '11:00', 'Study Python', 'STUDY')]

    result = formatter.format_query_results(query_data)
    expected_result = "1 2023/04/01 10:00 11:00 Study Python"
    assert result == expected_result

def test_format_priority():
    formatter = Formatter()
    priority_data = [('Study Python', 18000), ('Exercise', 7200)]

    result = formatter.format_priority(priority_data)
    assert "Study Python" in result
    assert "Exercise" in result
    assert "5h 0m 0s" in result
    assert "2h 0m 0s" in result