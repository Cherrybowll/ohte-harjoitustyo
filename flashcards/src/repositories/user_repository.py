from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Class for user account related operations between database and application logic.

    Attributes:
        connection: SQLite database connection.
    """
    def __init__(self, connection):
        """Constructor for UserRepository.

        Args:
            connection (connection): SQLite database connection.
        """
        self._connection = connection

    def find_by_username(self, username):
        """Fetches all users from database with specified username.

        Args:
            username (str): Name of user to be found

        Returns:
            User: Instance of entity User. None if user doesn't exist.
        """
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM users WHERE username=:username;",
                    {"username": username})
        row = cur.fetchone()

        return User(row["username"], row["password"], row["id"]) if row else None

    def create(self, user):
        """Stores a new user into the database.

        Args:
            user (User): Instance of entity User.
        """
        cur = self._connection.cursor()

        cur.execute("INSERT INTO users (username, password) VALUES(:username, :password);",
                    {"username": user.username, "password": user.password})
        self._connection.commit()

    def delete_all(self):
        """Deletes all users from database.
        """
        cur = self._connection.cursor()

        cur.execute("DELETE FROM users;")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
