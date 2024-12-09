from entities.collection import Collection
from database_connection import get_database_connection


class CollectionRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM collections;")
        rows = cur.fetchall()

        return [Collection(row["name"], row["creator_id"], row["id"]) for row in rows]

    def find_by_creator_id(self, creator_id):
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM collections WHERE creator_id=:creator_id;",
                    {"creator_id": creator_id})
        rows = cur.fetchall()

        return [Collection(row["name"], row["creator_id"], row["id"]) for row in rows]

    def create(self, collection):
        cur = self._connection.cursor()

        cur.execute("INSERT INTO collections (name, creator_id) VALUES (:name, :creator_id);",
                    {"name": collection.name, "creator_id": collection.creator_id})
        self._connection.commit()

    def delete_all(self):
        cur = self._connection.cursor()

        cur.execute("DELETE FROM collections;")
        self._connection.commit()

    def delete_by_id(self, id):
        cur = self._connection.cursor()

        cur.execute("DELETE FROM collections WHERE id=:id", {"id":id})
        self._connection.commit()

collection_repository = CollectionRepository(get_database_connection())
