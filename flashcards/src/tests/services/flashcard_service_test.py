import unittest
from services.flashcard_service import flashcard_service


class TestFlashcardService(unittest.TestCase):
    def setUp(self):
        pass

    def test_set_message_works(self):
        self.assertIsNone(flashcard_service._message)
        flashcard_service.set_message("message")
        self.assertEqual(flashcard_service._message, "message")

    def test_get_message_returns_message_and_resets(self):
        flashcard_service.set_message("message")
        message = flashcard_service.get_message()
        self.assertEqual(message, "message")
        self.assertIsNone(flashcard_service._message)
