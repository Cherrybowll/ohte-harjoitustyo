from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_all(self):
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        return [User(row["username"], row["password"]) for row in rows]
    
    def find_by_username(self, username):
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM users WHERE username=:username",
                    {"username":username})
        row = cur.fetchone()

        return User(row["username"], row["password"]) if row else None
    
    def create(self, user):
        cur = self._connection.cursor()

        cur.execute("INSERT INTO users VALUES(:username, :password)",
                    {"username":user.username, "password":user.password})
        self._connection.commit()

user_repository = UserRepository(get_database_connection())