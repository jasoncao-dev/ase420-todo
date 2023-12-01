import pytest
from unittest.mock import Mock
from src.PriorityCommand import PriorityCommand

def test_priority_command():
    db_mock = Mock()
    formatter_mock = Mock()
    priority_command = PriorityCommand()

    mock_priority_data = [('Study Python', 18000), ('Exercise', 7200)]

    db_mock.get_priority_tasks.return_value = mock_priority_data
    formatter_mock.format_priority.return_value = "Formatted priority"

    result = priority_command.execute({}, db_mock, formatter_mock)
    db_mock.get_priority_tasks.assert_called_once()
    formatter_mock.format_priority.assert_called_once_with(mock_priority_data)
    assert result == "Formatted priority"