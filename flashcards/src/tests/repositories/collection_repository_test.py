import unittest
from repositories.collection_repository import collection_repository
from entities.collection import Collection


class TestCollectionRepository(unittest.TestCase):
    def setUp(self):
        collection_repository.delete_all()
        collection_repository.create(Collection("collection", 1))

    def test_find_by_creator_id_returns_one_if_only(self):
        collections = collection_repository.find_by_creator_id(1)
        self.assertEqual(len(collections), 1)
        self.assertEqual(collections[0].name, "collection")

    def test_find_by_creator_id_returns_all_if_many(self):
        collection_repository.create(Collection("collection1", 1))
        collections = collection_repository.find_by_creator_id(1)

        self.assertEqual(len(collections), 2)
        self.assertEqual(collections[0].name, "collection")
        self.assertEqual(collections[1].name, "collection1")

    def test_find_by_creator_id_doesnt_return_from_wrong_user(self):
        collection_repository.create(Collection("collection1", 2))
        collections = collection_repository.find_by_creator_id(1)

        self.assertEqual(len(collections), 1)
        self.assertEqual(collections[0].name, "collection")

    def test_find_by_creator_id_returns_empty_list_if_nonexistent(self):
        collections = collection_repository.find_by_creator_id(2)
        self.assertEqual(len(collections), 0)

    def test_collections_are_always_private_after_creation(self):
        collection_repository.create(Collection("collection1", 1, True))
        public = collection_repository.find_all_public()

        self.assertEqual(len(public), 0)

    def test_find_all_public_returns_only_public_collections(self):
        collection_repository.create(Collection("collection1", 1))
        collection_repository.change_publicity(2, True)
        public = collection_repository.find_all_public()

        self.assertEqual(len(public), 1)
        self.assertEqual(public[0].name, "collection1")

    def test_change_publicity_works(self):
        collection_repository.create(Collection("collection1", 1, True))
        collection_repository.change_publicity(1, True)
        collection_repository.change_publicity(2, False)
        public = collection_repository.find_all_public()

        self.assertEqual(len(public), 1)
        self.assertEqual(public[0].name, "collection")

    def test_delete_by_id_deletes_correct_collection(self):
        collection_repository.create(Collection("collection1", 1))
        collection_repository.delete_by_id(1)
        collections = collection_repository.find_by_creator_id(1)

        self.assertEqual(len(collections), 1)
        self.assertEqual(collections[0].name, "collection1")

    def test_string_representation(self):
        collection = Collection("collection", 1, False, 1)
        self.assertEqual(
            str(collection), "Collection: 1, collection by 1, public=False")
