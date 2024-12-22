from entities.collection import Collection
from database_connection import get_database_connection


class CollectionRepository:
    """Class for flashcard collection related operations between database and application logic.

    Attributes:
        connection: SQLite database connection.
    """

    def __init__(self, connection):
        """Constructor for CollectionRepository

        Args:
            connection (connection): SQLite database connection.
        """
        self._connection = connection

    def find_all_public(self):
        """Fetches all public collections from database.

        Returns:
            list: List of Collection entities.
        """
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM collections WHERE public=TRUE;")
        rows = cur.fetchall()

        return [Collection(
            row["name"], row["creator_id"], row["public"], row["id"]
        ) for row in rows]

    def find_by_creator_id(self, creator_id):
        """Fetches all collection from database with specified creator_id.

        Args:
            creator_id (int): id of User entity that created the collection(s).

        Returns:
            list: List of collection entities.
        """
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM collections WHERE creator_id=:creator_id;",
                    {"creator_id": creator_id})
        rows = cur.fetchall()

        return [Collection(
            row["name"], row["creator_id"], row["public"], row["id"]
        ) for row in rows]

    def create(self, collection):
        """Creates a new collection entry into the database.

        Args:
            collection (Collection): Instance of entity Collection.
        """
        cur = self._connection.cursor()

        cur.execute("INSERT INTO collections (name, creator_id) VALUES (:name, :creator_id);",
                    {"name": collection.name, "creator_id": collection.creator_id})
        self._connection.commit()

    def change_publicity(self, collection_id, public):
        """Changes whether a collection is public or private.

        Args:
            collection_id (int): id of collection to be altered.
            public (bool): Publicity status of collection.
        """
        cur = self._connection.cursor()
        cur.execute("UPDATE collections SET public=:public WHERE id=:id;",
                    {"public": public, "id": collection_id})
        self._connection.commit()

    def delete_all(self):
        """Delete all collections from database.
        """
        cur = self._connection.cursor()

        cur.execute("DELETE FROM collections;")
        self._connection.commit()

    def delete_by_id(self, collection_id):
        """Delete a collection from database with the specified id.

        Args:
            collection_id (int): id of collection to be deleted.
        """
        cur = self._connection.cursor()

        cur.execute("DELETE FROM collections WHERE id=:id",
                    {"id": collection_id})
        self._connection.commit()


collection_repository = CollectionRepository(get_database_connection())
