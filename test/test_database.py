import pytest
from datetime import datetime
from src.Database import Database


# Use an in-memory SQLite database for the duration of the test session.
@pytest.fixture
def database():
    database = Database(":memory:")
    yield database


def seed_database(database):
    # Add a task for querying.
    database.add_task('2023/04/01', '10:00', '11:00', 'Coding Session', 'WORK')
    database.add_task('2023/04/02', '12:00', '13:00', 'Exercise', None)


@pytest.fixture(autouse=True)
def setup_database(database):
    # It seeds the database before each test.
    seed_database(database)
    return database


def test_add_and_query_task(database):
    # Add a task and then query it by the same criteria to ensure it exists.
    database.add_task('2023/04/03', '10:00', '11:00', 'Coding Session', 'WORK')
    results = database.query_tasks('2023/04/03', 'Coding Session', 'WORK')
    assert len(results) == 1
    assert results[0][3] == 'Coding Session'  # Check the 'task' field


def test_query_by_date(database):
    # Assuming that test_add_and_query_task has run and added a task.
    results = database.query_tasks('2023/04/01')
    assert len(results) == 1
    assert results[0][0] == '2023/04/01'  # Check the 'date' field


def test_query_by_task(database):
    # Query by task name.
    results = database.query_tasks(task='Coding Session')
    assert len(results) >= 1  # Assuming at least one 'Coding Session' task was added.


def test_query_by_tag(database):
    # Query by tag.
    results = database.query_tasks(tag='WORK')
    assert len(results) >= 1  # Assuming at least one 'WORK' tagged task was added.


def test_query_with_no_results(database):
    # Query for a non-existing record.
    results = database.query_tasks('2025/12/25')
    assert len(results) == 0


def test_query_with_multiple_results(database):
    # Add multiple tasks and query to ensure all are returned.
    database.add_task('2023/04/01', '09:00', '10:00', 'Review Python', 'STUDY')
    database.add_task('2023/04/01', '11:00', '12:00', 'Exercise', 'HEALTH')
    results = database.query_tasks('2023/04/01')
    assert len(results) == 3  # Including the task from test_add_and_query_task


def test_add_task_without_tag(database):
    # The tag should be optional.
    database.add_task('2023/04/01', '13:00', '14:00', 'Lunch Break', None)
    results = database.query_tasks('2023/04/01', 'Lunch Break')
    assert len(results) == 1
    assert results[0][3] == 'Lunch Break'
    assert results[0][4] is ''  # Tag should be None
