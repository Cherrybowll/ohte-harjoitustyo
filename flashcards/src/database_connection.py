import os
import sqlite3
from config import DATABASE_FILE_PATH

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    """Returns the SQLite database connection object.

    Returns:
        connection: SQLite database connection.
    """
    return connection
