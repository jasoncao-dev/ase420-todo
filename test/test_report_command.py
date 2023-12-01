import pytest
from unittest.mock import Mock
from src.ReportCommand import ReportCommand

def test_report_command():
    db_mock = Mock()
    formatter_mock = Mock()
    report_command = ReportCommand()

    args = {
        'from_date': '2023/01/01',
        'to_date': '2023/01/31'
    }
    mock_report_data = [(1, '2023/01/01', '10:00', '11:00', 'New Year Planning', 'PLANNING')]

    db_mock.generate_report.return_value = mock_report_data
    formatter_mock.format_report.return_value = "Formatted report"

    result = report_command.execute(args, db_mock, formatter_mock)
    db_mock.generate_report.assert_called_once_with(args['from_date'], args['to_date'])
    formatter_mock.format_report.assert_called_once_with(mock_report_data)
    assert result == "Formatted report"