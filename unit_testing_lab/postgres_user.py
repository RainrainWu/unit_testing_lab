import warnings

import psycopg2

warnings.simplefilter("ignore")


class PostgresUser:
    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        dbname: str,
    ) -> None:

        self.__connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=dbname,
        )
        self.__cursor = self.__connection.cursor()

    def execute(
        self,
        sql: str,
        data: tuple[str | int | float, ...] = (),
    ) -> None:

        self.__cursor.execute(sql, data)

    def get_records_amount(self, table_name: str) -> int:

        self.__cursor.execute(f"SELECT COUNT(1) FROM {table_name}")
        return self.__cursor.fetchone()[0]
