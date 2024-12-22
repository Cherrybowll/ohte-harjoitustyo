from entities.flashcard import Flashcard
from database_connection import get_database_connection


class FlashcardRepository:
    """Class for flashcard related operations between database and application logic.

    Attributes:
        connection: SQLite database connection.
    """
    def __init__(self, connection):
        """Constructor for CollectionRepository

        Args:
            connection (connection): SQLite database connection.
        """
        self._connection = connection

    def find_all(self):
        """Fetches all flashcards from database.

        Returns:
            list: List of Flashcard entities.
        """
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM flashcards;")
        rows = cur.fetchall()

        return [Flashcard(row["front"],
                          row["back"],
                          row["collection_id"],
                          row["id"]) for row in rows]

    def find_by_collection_id(self, collection_id):
        """Fetches all flashcards from database with specified collection_id.

        Args:
            collection_id (int): id of the parent collection.

        Returns:
            list: List of flashcard entities.
        """
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM flashcards WHERE collection_id=:collection_id;",
                    {"collection_id": collection_id})
        rows = cur.fetchall()

        return [Flashcard(row["front"],
                          row["back"],
                          row["collection_id"],
                          row["id"]) for row in rows]

    def find_by_id(self, flashcard_id):
        """Fetches flashcard from database by specified id.

        Args:
            flashcard_id (int): id of the flashcard.

        Returns:
            Flashcard: a Flashcard entity.
        """
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM flashcards WHERE id=:id",
                    {"id": flashcard_id})
        row = cur.fetchone()

        return Flashcard(
            row["front"],
            row["back"],
            row["collection_id"],
            row["id"]
        )

    def create(self, flashcard):
        """Creates a new flashcard entry in the database.

        Args:
            flashcard (Flashcard): a Flashcard entity.
        """
        cur = self._connection.cursor()

        sql = ("INSERT INTO flashcards (front, back, collection_id) "
               "VALUES (:front, :back, :collection_id)")
        cur.execute(sql, {
            "front": flashcard.front,
            "back": flashcard.back,
            "collection_id": flashcard.collection_id
        })

        self._connection.commit()

    def delete_all(self):
        """Deletes all flashcard entries from the database.
        """
        cur = self._connection.cursor()

        cur.execute("DELETE FROM flashcards;")
        self._connection.commit()

    def delete_by_collection_id(self, collection_id):
        """Deletes all flashcard entries from the database with the specified collection_id.

        Args:
            collection_id (int): id of the parent collection.
        """
        cur = self._connection.cursor()

        sql = "DELETE FROM flashcards WHERE collection_id=:collection_id;"
        cur.execute(sql, {"collection_id": collection_id})
        self._connection.commit()

    def delete_by_id(self, flashcard_id):
        """Delete a flashcard entry from the database with the specified flashcard_id.

        Args:
            flashcard_id (int): id of the flashcard.
        """
        cur = self._connection.cursor()

        sql = "DELETE FROM flashcards WHERE id=:id;"
        cur.execute(sql, {"id": flashcard_id})
        self._connection.commit()


flashcard_repository = FlashcardRepository(get_database_connection())
