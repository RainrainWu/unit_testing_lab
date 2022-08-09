import os

import pytest
from testcontainers.postgres import PostgresContainer
from unit_testing_lab.postgres_user import PostgresUser


@pytest.fixture(scope="session")
def fixture_postgres_username():

    yield "test"


@pytest.fixture(scope="session")
def fixture_postgres_password():

    yield "test"


@pytest.fixture(scope="session")
def fixture_postgres_dbname():

    yield "test"


@pytest.fixture(scope="session")
def fixture_postgres_students_table_name():

    yield "students"


@pytest.fixture(scope="session")
def fixture_postgres_test_students_amount():

    yield 1000


@pytest.fixture(scope="session", autouse=True)
def fixture_postgres():

    with PostgresContainer("postgres:14.4") as postgres:
        yield postgres


@pytest.fixture(scope="session")
def fixture_postgres_port(fixture_postgres):

    yield int(fixture_postgres.get_exposed_port(fixture_postgres.port_to_expose))


@pytest.fixture(scope="session")
def fixture_postgres_user(
    fixture_postgres_username,
    fixture_postgres_password,
    fixture_postgres_dbname,
    fixture_postgres_port,
):

    yield PostgresUser(
        "127.0.0.1",
        fixture_postgres_port,
        fixture_postgres_username,
        fixture_postgres_password,
        fixture_postgres_dbname,
    )


@pytest.fixture(scope="session")
def fixture_postgres_migration(fixture_postgres_user):

    for file in os.listdir("../../migrations"):

        if not file.endswith(".sql"):
            continue

        file_path = os.path.join("../../migrations", file)
        with open(file_path, "r") as read_file:

            commands = read_file.read().split(";")
            for command in commands[:-1]:
                fixture_postgres_user.execute(command)


@pytest.fixture(scope="session")
def fixture_postgres_test_students_data(
    fixture_postgres_students_table_name,
    fixture_postgres_test_students_amount,
    fixture_postgres_user,
):

    command = (
        f"INSERT INTO {fixture_postgres_students_table_name} ("
        "   name,"
        "   address,"
        "   grade"
        ")"
        "SELECT"
        "   left(md5(i::text), 20),"
        "   left(md5(i::text), 50),"
        "   floor(random() * 10 + 1)::int "
        "from generate_series(1, %s) s(i)"
    )
    fixture_postgres_user.execute(
        command,
        (fixture_postgres_test_students_amount,),
    )
