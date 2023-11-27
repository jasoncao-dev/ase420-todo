import pytest
from src.InputHandler import InputHandler

# Test input parsing for recording a task.
def test_input_handler_record_task():
    input_handler = InputHandler()
    command = "record 2023/04/01 10:00 11:00 'Coding Session' :WORK"
    args, error = input_handler.parse_input(command)
    assert error is None
    assert args['date'] == '2023/04/01'
    assert args['from_time'] == '10:00'
    assert args['to_time'] == '11:00'
    assert args['task'] == 'Coding Session'
    assert args['tag'] == 'WORK'


# Test input parsing for querying tasks by date.
def test_input_handler_query_by_date():
    input_handler = InputHandler()
    command = "query 2023/04/01"
    args, error = input_handler.parse_input(command)
    assert error is None
    assert args['date'] == '2023/04/01'
    assert args['task'] is None
    assert args['tag'] is None


# Test input parsing for querying tasks by task.
def test_input_handler_query_by_task():
    input_handler = InputHandler()
    command = "query 'Coding Session'"
    args, error = input_handler.parse_input(command)
    assert error is None
    assert args['task'] == 'Coding Session'
    assert args['date'] is None
    assert args['tag'] is None

# Test input parsing with missing parameters for recording a task.
def test_input_handler_record_task_missing_parameters():
    input_handler = InputHandler()
    command = "record 2023/04/01 10:00 'Coding Session' :WORK"  # Missing end time
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid record format" in error

# Test input parsing with non-date strings.
def test_input_handler_record_invalid_date():
    input_handler = InputHandler()
    command = "record not-a-date 10:00 11:00 'Coding Session' :WORK"
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid record format" in error

# Test input parsing with non-time strings for start time.
def test_input_handler_record_invalid_start_time():
    input_handler = InputHandler()
    command = "record 2023/04/01 not-a-time 11:00 'Coding Session' :WORK"
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid record format" in error

# Test input parsing with non-time strings for end time.
def test_input_handler_record_invalid_end_time():
    input_handler = InputHandler()
    command = "record 2023/04/01 10:00 not-a-time 'Coding Session' :WORK"
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid record format" in error

# Test input parsing with missing task string.
def test_input_handler_record_missing_task():
    input_handler = InputHandler()
    command = "record 2023/04/01 10:00 11:00 :WORK"
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid record format" in error

# Test input parsing with incorrect task format (missing quotes).
def test_input_handler_record_incorrect_task_format():
    input_handler = InputHandler()
    command = "record 2023/04/01 10:00 11:00 Coding Session :WORK"
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid record format" in error

# Test input parsing with invalid command (neither record nor query).
def test_input_handler_invalid_command():
    input_handler = InputHandler()
    command = "delete 2023/04/01"
    args, error = input_handler.parse_input(command)
    assert args is None
    assert "Invalid command" in error

# Test input parsing for querying tasks by tag.
def test_input_handler_query_by_tag():
    input_handler = InputHandler()
    command = "query :WORK"
    args, error = input_handler.parse_input(command)
    assert error is None
    assert args['tag'] == 'WORK'
    assert args['date'] is None
    assert args['task'] is None