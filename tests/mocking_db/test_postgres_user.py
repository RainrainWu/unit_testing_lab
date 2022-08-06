
class TestPostgresUser:
    def test_postgres_connection(self, fixture_postgres_user):

        fixture_postgres_user.execute("SELECT 1")

    def test_postgres_migration(
        self,
        fixture_postgres_students_table_name,
        fixture_postgres_test_students_amount,
        fixture_postgres_user,
        fixture_postgres_migration,
        fixture_postgres_test_students_data,
    ):

        amount = fixture_postgres_user.get_records_amount(
            fixture_postgres_students_table_name,
        )
        assert amount == fixture_postgres_test_students_amount
