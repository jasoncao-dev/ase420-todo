import pytest
from unittest.mock import Mock
from src.RecordCommand import RecordCommand


def test_record_command():
    db_mock = Mock()
    formatter_mock = Mock()
    record_command = RecordCommand()

    args = {
        'date': '2023/04/01',
        'from_time': '10:00',
        'to_time': '11:00',
        'task': 'Study Python',
        'tag': 'STUDY'
    }

    result = record_command.execute(args, db_mock, formatter_mock)
    db_mock.add_task.assert_called_once_with(args['date'], args['from_time'], args['to_time'], args['task'],
                                             args['tag'])
    assert result == "Task recorded successfully."
