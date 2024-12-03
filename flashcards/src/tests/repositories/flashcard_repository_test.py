import unittest
from repositories.flashcard_repository import flashcard_repository
from entities.flashcard import Flashcard


class TestFlashcardRepository(unittest.TestCase):
    def setUp(self):
        flashcard_repository.delete_all()
        flashcard_repository.create(Flashcard("front", "back", 1))

    def test_find_by_collection_id_returns_one_if_only(self):
        flashcards = flashcard_repository.find_by_collection_id(1)

        self.assertEqual(len(flashcards), 1)
        self.assertEqual(flashcards[0].front, "front")

    def test_find_by_collection_id_returns_all_if_many(self):
        flashcard_repository.create(Flashcard("front1", "back1", 1))
        flashcards = flashcard_repository.find_by_collection_id(1)

        self.assertEqual(len(flashcards), 2)
        self.assertEqual(flashcards[0].front, "front")
        self.assertEqual(flashcards[1].front, "front1")

    def test_find_by_collection_id_doesnt_return_from_wrong_collection(self):
        flashcard_repository.create(Flashcard("front1", "back1", 1))
        flashcard_repository.create(Flashcard("front2", "back2", 2))
        flashcards = flashcard_repository.find_by_collection_id(1)

        self.assertEqual(len(flashcards), 2)
        self.assertEqual(flashcards[0].front, "front")
        self.assertEqual(flashcards[1].front, "front1")

    def test_find_all_returns_all(self):
        flashcard_repository.create(Flashcard("front1", "back1", 1))
        flashcard_repository.create(Flashcard("front2", "back2", 2))
        flashcards = flashcard_repository.find_all()

        self.assertEqual(len(flashcards), 3)
        self.assertEqual(flashcards[0].front, "front")
        self.assertEqual(flashcards[1].front, "front1")
        self.assertEqual(flashcards[2].front, "front2")

    def test_find_by_collection_id_returns_empty_list_if_nonexistent(self):
        flashcard_repository.delete_all()
        flashcards = flashcard_repository.find_by_collection_id(1)

        self.assertEqual(len(flashcards), 0)

    def test_find_all_returns_empty_list_if_nonexistent(self):
        flashcard_repository.delete_all()
        flashcards = flashcard_repository.find_all()

        self.assertEqual(len(flashcards), 0)
