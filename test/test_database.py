import pytest
from datetime import datetime
from src.Database import Database


# Use an in-memory SQLite database for the duration of the test session.
@pytest.fixture
def database():
    database = Database(":memory:")
    yield database


def seed_database(database):
    database.add_task('2023/04/01', '10:00', '11:00', 'Coding Session', 'WORK')
    database.add_task('2023/04/01', '13:00', '14:00', 'Lunch Break', None)
    database.add_task('2023/04/02', '12:00', '13:00', 'Exercise', None)
    database.add_task('2023/04/03', '10:00', '11:00', 'Coding Session', 'WORK')
    database.add_task('2023/04/04', '09:00', '10:00', 'Review Python', 'STUDY')
    database.add_task('2023/04/04', '11:00', '12:00', 'Exercise', 'HEALTH')
    database.add_task('2023/04/05', '10:00', '12:00', 'Coding Session', 'WORK')
    database.add_task('2023/04/05', '13:00', '15:00', 'Reading', 'READING')


@pytest.fixture(autouse=True)
def setup_database(database):
    seed_database(database)
    return database


def test_add_and_query_task(database):
    database.add_task('2023/03/31', '10:00', '11:00', 'Coding Session', 'WORK')
    results = database.query_tasks('2023/03/31', 'Coding Session', 'WORK')
    assert len(results) == 1
    assert results[0][3] == 'Coding Session'


def test_query_by_date(database):
    results = database.query_tasks('2023/04/01')
    assert len(results) == 2
    assert results[0][0] == '2023/04/01'
    assert results[1][0] == '2023/04/01'


def test_query_by_task(database):
    results = database.query_tasks(task='Coding Session')
    assert len(results) >= 1


def test_query_by_tag(database):
    results = database.query_tasks(tag='WORK')
    assert len(results) >= 1


def test_query_with_no_results(database):
    results = database.query_tasks('2025/12/25')
    assert len(results) == 0


def test_query_with_multiple_results(database):
    results = database.query_tasks('2023/04/04')
    assert len(results) == 2


def test_add_task_without_tag(database):
    results = database.query_tasks('2023/04/01', 'Lunch Break')
    assert len(results) == 1
    assert results[0][3] == 'Lunch Break'
    assert results[0][4] is ''


def test_generate_report(database):
    from_date = '2023/04/01'
    to_date = '2023/04/02'
    report = database.generate_report(from_date, to_date)
    assert len(report) == 3


def test_get_priority_tasks(database):
    priority_data = database.get_priority_tasks()
    assert priority_data[0][0] == 'Coding Session' and priority_data[1][0] == 'Reading'
    assert priority_data[0][-1] > priority_data[1][-1]