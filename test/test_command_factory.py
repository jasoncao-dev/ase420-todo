import pytest
from src.CommandFactory import CommandFactory
from src.RecordCommand import RecordCommand
from src.QueryCommand import QueryCommand
from src.ReportCommand import ReportCommand
from src.PriorityCommand import PriorityCommand


def test_command_factory():
    factory = CommandFactory()

    record = factory.get_command('record')
    assert isinstance(record, RecordCommand)

    query = factory.get_command('query')
    assert isinstance(query, QueryCommand)

    report = factory.get_command('report')
    assert isinstance(report, ReportCommand)

    priority = factory.get_command('priority')
    assert isinstance(priority, PriorityCommand)

    none = factory.get_command('nonexistent')
    assert none is None