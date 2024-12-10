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

    def test_find_all_returns_all(self):
        collection_repository.create(Collection("collection1", 1))
        collection_repository.create(Collection("collection2", 2))
        collections = collection_repository.find_all()

        self.assertEqual(len(collections), 3)
        self.assertEqual(collections[0].name, "collection")
        self.assertEqual(collections[1].name, "collection1")
        self.assertEqual(collections[2].name, "collection2")

    def test_find_by_creator_id_returns_empty_list_if_nonexistent(self):
        collections = collection_repository.find_by_creator_id(2)
        self.assertEqual(len(collections), 0)

    def test_find_all_returns_empty_list_if_nonexistent(self):
        collection_repository.delete_all()
        collections = collection_repository.find_all()
        self.assertEqual(len(collections), 0)

    def test_string_representation(self):
        collection = Collection("collection", 1, False, 1)
        self.assertEqual(str(collection), "Collection: 1, collection by 1, public=False")
