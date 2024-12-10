import unittest
from services.flashcard_service import flashcard_service
from repositories.user_repository import user_repository


class TestFlashcardService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

    def test_set_message_works(self):
        self.assertIsNone(flashcard_service._message)
        flashcard_service.set_message("message")
        self.assertEqual(flashcard_service._message, "message")

    def test_get_message_returns_message_and_resets(self):
        flashcard_service.set_message("message")
        message = flashcard_service.get_message()
        self.assertEqual(message, "message")
        self.assertIsNone(flashcard_service._message)

    def test_create_user_and_login_works(self):
        flashcard_service.create_user("user1", "password1", "password1")
        flashcard_service.login("user1", "password1")

        self.assertEqual(flashcard_service._user.username, "user1")

    def test_create_user_makes_new_user_and_returns_true(self):
        success = flashcard_service.create_user("user1", "password1", "password1")
        user = user_repository.find_by_username("user1")

        self.assertEqual(success, True)
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "password1")

    def test_create_user_with_different_passwords_fails_and_returns_false(self):
        success = flashcard_service.create_user("user1", "password1", "password2")
        user = user_repository.find_by_username("user1")

        self.assertEqual(success, False)
        self.assertEqual(user, None)

    def test_create_user_with_existing_username_fails(self):
        success1 = flashcard_service.create_user("user1", "password1", "password1")
        success2 = flashcard_service.create_user("user1", "password2", "password2")
        user = user_repository.find_by_username("user1")

        self.assertEqual(success1, True)
        self.assertEqual(success2, False)
        self.assertEqual(user.password, "password1")
