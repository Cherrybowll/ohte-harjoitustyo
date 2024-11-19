from database_connection import get_database_connection

def create_tables(connection):
    cur = connection.cursor()

    sql = ("CREATE TABLE users("
           "username TEXT PRIMARY KEY,"
           "password TEXT"
            ");")
    cur.execute(sql)

    sql = ("CREATE TABLE flashcards("
           "id SERIAL PRIMARY KEY,"
           "front TEXT,"
           "back TEXT,"
           "collection TEXT"
           ");")
    connection.commit()

def drop_tables(connection):
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("DROP TABLE IF EXISTS flashcards;")
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()