import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        user_repository.create(User("username", "password"))

    def test_find_by_username_returns_user(self):
        user = user_repository.find_by_username("username")

        self.assertEqual(user.username, "username")

    def test_find_by_username_returns_none_if_nonexistent_user(self):
        user = user_repository.find_by_username("nonexistent_name")

        self.assertEqual(user, None)

    def test_find_all_returns_all_users(self):
        user_repository.create(User("username1", "password"))
        user_repository.create(User("username2", "passpass"))
        users = user_repository.find_all()

        self.assertEqual(len(users), 3)
        self.assertEqual(users[0].username, "username")
        self.assertEqual(users[1].username, "username1")
        self.assertEqual(users[2].username, "username2")

    def test_find_all_returns_only_user(self):
        user = user_repository.find_all()

        self.assertEqual(len(user), 1)
        self.assertEqual(user[0].username, "username")

    def test_delete_all_clears_database(self):
        user_repository.delete_all()
        users = user_repository.find_all()

        self.assertEqual(len(users), 0)
