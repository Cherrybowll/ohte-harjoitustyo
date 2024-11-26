from entities.flashcard import Flashcard
from database_connection import get_database_connection


class FlashcardRepository:
    def __init__(self, connection):
        self._connection = connection


    def find_all(self):
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM flashcards;")
        rows = cur.fetchall()

        return [Flashcard(row["front"], row["back"], row["collection_id"], row["id"]) for row in rows]


    def find_by_collection_id(self, collection_id):
        cur = self._connection.cursor()

        cur.execute("SELECT * FROM flashcards WHERE collection_id=:collection_id;",
                    {"collection_id":collection_id})
        rows = cur.fetchall()

        return [Flashcard(row["front"], row["back"], row["collection_id"], row["id"]) for row in rows]


    def create(self, flashcard):
        cur = self._connection.cursor()

        sql = ("INSERT INTO flashcards (front, back, collection_id) "
               "VALUES (:front, :back, :collection_id)")
        cur.execute(sql, {
            "front":flashcard.front,
            "back": flashcard.back,
            "collection_id": flashcard.collection_id
            })

        self._connection.commit()


flashcard_repository = FlashcardRepository(get_database_connection())
