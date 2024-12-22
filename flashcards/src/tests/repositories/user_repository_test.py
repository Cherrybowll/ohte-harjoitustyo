import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        user_repository.create(User("username1", "password"))

    def test_find_by_username_returns_user(self):
        user = user_repository.find_by_username("username1")

        self.assertEqual(user.username, "username1")

    def test_find_by_username_returns_none_if_nonexistent_user(self):
        user = user_repository.find_by_username("nonexistent_name")

        self.assertIsNone(user)

    def test_find_by_username_returns_correct_user(self):
        user_repository.create(User("username2", "password"))
        user1 = user_repository.find_by_username("username1")
        user2 = user_repository.find_by_username("username2")

        self.assertEqual(user1.username, "username1")
        self.assertEqual(user2.username, "username2")

    def test_delete_all_clears_database(self):
        user_repository.create(User("username2", "password"))
        user_repository.delete_all()
        user1 = user_repository.find_by_username("username1")
        user2 = user_repository.find_by_username("username2")

        self.assertIsNone(user1)
        self.assertIsNone(user2)
