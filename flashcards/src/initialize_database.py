from database_connection import get_database_connection

def create_tables(connection):
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
           "collection_id REFERENCES collections"
           ");")
    cur.execute(sql)

    sql = ("CREATE TABLE collections("
           "id INTEGER PRIMARY KEY,"
           "name TEXT,"
           "creator_id REFERENCES users"
           ");")
    cur.execute(sql)
    connection.commit()

def drop_tables(connection):
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("DROP TABLE IF EXISTS flashcards;")
    cur.execute("DROP TABLE IF EXISTS collections;")
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()