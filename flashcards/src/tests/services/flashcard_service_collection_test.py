import unittest
from services.flashcard_service import flashcard_service
from repositories.user_repository import user_repository
from repositories.collection_repository import collection_repository

class TestFlashcardServiceCollection(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        collection_repository.delete_all()
        flashcard_service.create_user("user1", "password1", "password1")
        flashcard_service.login("user1", "password1")

    def test_create_collection_works(self):
        flashcard_service.create_collection("collection1")
        collections = collection_repository.find_by_creator_id(flashcard_service._user.id)

        self.assertEqual(len(collections), 1)
        self.assertEqual(collections[0].name, "collection1")
        self.assertEqual(collections[0].creator_id, 1)