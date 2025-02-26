"""This module will retrive and store data from the database."""

from sqlite3 import connect, Connection, Cursor, Error

CREATE_TEST_TABLE: str = (
    "CREATE TABLE IF NOT EXISTS test "
    "(id INTEGER PRIMARY KEY, text1 TEXT, "
    "text2 TEXT);"
)


async def test_data() -> None:
    """Creates a dummy table."""
    try:
        data_con: Connection = connect("data/data.db")
    except Error as e_msg:
        raise e_msg
    data_cursor: Cursor = data_con.cursor()

    data_cursor.execute(CREATE_TEST_TABLE)

    if (
        len(data_cursor.execute("SELECT * FROM test;").description) == 3
    ):
        print("Successfully made a test table!")

    else:
        data_con.close()
        raise Exception("User Database has not been configured successfully.")

    data_cursor.execute(
        "INSERT INTO test VALUES (0, 'hello', 'world');"
    )

    data_cursor.execute(
        "SELECT * FROM test WHERE id = 0;"
    )

    data: list[tuple[int]] = data_cursor.fetchall()

    print(data)

    if True:
        data_con.commit()
        data_con.close()
    return


if __name__ == "__main__":
    print("This is a module, please run 'main.py'. Exiting...")
