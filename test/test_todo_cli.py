import pytest
from unittest.mock import Mock
from program import TodoCLI


@pytest.fixture
def mock_input_handler(mocker):
    input_handler = mocker.patch('program.InputHandler', autospec=True)
    input_handler_instance = input_handler.return_value
    input_handler_instance.parse_input.return_value = (Mock(), None)
    return input_handler_instance


@pytest.fixture
def mock_database(mocker):
    return mocker.patch('program.Database', autospec=True).return_value


@pytest.fixture
def todo_cli(mock_input_handler, mock_database):
    return TodoCLI()


def test_record_command(todo_cli, mock_input_handler, mock_database):
    mock_input_handler.parse_input.return_value = (
        {
            'command': 'record',
            'date': '2023/04/01',
            'from_time': '10:00',
            'to_time': '11:00',
            'task': 'Study Python',
            'tag': 'STUDY'
        },
        None
    )

    result = todo_cli.execute_command("record 2023/04/01 10:00 11:00 'Study Python' :STUDY")

    mock_input_handler.parse_input.assert_called_once_with("record 2023/04/01 10:00 11:00 'Study Python' :STUDY")
    mock_database.add_task.assert_called_once_with(
        '2023/04/01', '10:00', '11:00', 'Study Python', 'STUDY'
    )
    assert result == "Task recorded successfully."


def test_record_command_with_invalid_input(todo_cli, mock_input_handler, mock_database):
    mock_input_handler.parse_input.return_value = (None, "Invalid input format.")

    result = todo_cli.execute_command("record 2023-04-01 10:00 'Study Python' :STUDY")

    mock_input_handler.parse_input.assert_called_once_with("record 2023-04-01 10:00 'Study Python' :STUDY")
    mock_database.add_task.assert_not_called()
    assert "Invalid input format." in result


def test_query_command_with_valid_tag(todo_cli, mock_input_handler, mock_database):
    mock_input_handler.parse_input.return_value = (
        {
            'command': 'query',
            'tag': 'STUDY'
        },
        None
    )
    mock_database.query_tasks.return_value = [
        ('2023/04/01', '10:00', '11:00', 'Study Python', 'STUDY')
    ]

    result = todo_cli.execute_command("query :STUDY")

    mock_input_handler.parse_input.assert_called_once_with("query :STUDY")
    mock_database.query_tasks.assert_called_once_with(date=None, task=None, tag='STUDY')
    assert "Study Python" in result


def test_query_command_no_results(todo_cli, mock_input_handler, mock_database):
    mock_input_handler.parse_input.return_value = (
        {
            'command': 'query',
            'date': '2023/04/02'
        },
        None
    )
    mock_database.query_tasks.return_value = []

    result = todo_cli.execute_command("query 2023/04/02")

    mock_input_handler.parse_input.assert_called_once_with("query 2023/04/02")
    mock_database.query_tasks.assert_called_once_with(date='2023/04/02', task=None, tag=None)
    assert "No tasks found" in result


def test_query_command_with_date(todo_cli, mock_input_handler, mock_database):
    expected_tasks = [
        ('2023/04/01', '10:00', '11:00', 'Study Python', 'STUDY'),
        ('2023/04/01', '12:00', '13:00', 'Lunch Break', '')
    ]
    mock_input_handler.parse_input.return_value = (
        {
            'command': 'query',
            'date': '2023/04/01'
        },
        None
    )
    mock_database.query_tasks.return_value = expected_tasks

    result = todo_cli.execute_command("query 2023/04/01")

    mock_input_handler.parse_input.assert_called_once_with("query 2023/04/01")
    mock_database.query_tasks.assert_called_once_with(date='2023/04/01', task=None, tag=None)
    for task in expected_tasks:
        assert task[3] in result
