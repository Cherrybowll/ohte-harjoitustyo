from database_connection import get_database_connection


def create_tables(connection):
    """Creates the tables for the database.

    Args:
        connection (connection): SQLite database connection.
    """
    cur = connection.cursor()

    sql = ("CREATE TABLE users("
           "id INTEGER PRIMARY KEY,"
           "username TEXT UNIQUE,"
           "password TEXT"
           ");")
    cur.execute(sql)

    sql = ("CREATE TABLE flashcards("
           "id INTEGER PRIMARY KEY,"
           "front TEXT,"
           "back TEXT,"
           "collection_id"
           ");")
    cur.execute(sql)

    sql = ("CREATE TABLE collections("
           "id INTEGER PRIMARY KEY,"
           "name TEXT,"
           "creator_id,"
           "public BOOLEAN DEFAULT FALSE"
           ");")
    cur.execute(sql)
    connection.commit()


def drop_tables(connection):
    """Removes all tables from the database.

    Args:
        connection (connection): SQLite database connection.
    """
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS flashcards;")
    cur.execute("DROP TABLE IF EXISTS collections;")
    cur.execute("DROP TABLE IF EXISTS users;")
    connection.commit()


def initialize_database():
    """Drops all existing tables and creates new ones.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
