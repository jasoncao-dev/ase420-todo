# tests/test_query_command.py
import pytest
from unittest.mock import Mock
from src.QueryCommand import QueryCommand

def test_query_command():
    db_mock = Mock()
    formatter_mock = Mock()
    query_command = QueryCommand()

    args = {'date': '2023/04/01'}
    mock_tasks = [(1, '2023/04/01', '10:00', '11:00', 'Study Python', 'STUDY')]

    db_mock.query_tasks.return_value = mock_tasks
    formatter_mock.format_query_results.return_value = "Formatted result"

    result = query_command.execute(args, db_mock, formatter_mock)
    db_mock.query_tasks.assert_called_once_with(args['date'], None, None)
    formatter_mock.format_query_results.assert_called_once_with(mock_tasks)
    assert result == "Formatted result"
