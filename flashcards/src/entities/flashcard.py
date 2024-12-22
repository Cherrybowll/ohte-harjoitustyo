class Flashcard:
    """Class for storing flashcards.

    Attributes:
        front: Front side of flashcard.
        back: Back side of flashcard.
        collection_id: DB id for the collection that the flashcard is a part of.
        id: id in DB.
    """

    def __init__(self, front, back, collection_id, flashcard_id=None):
        """Class constructor for creating new flashcards.

        Args:
            front (str): Front side of flashcard.
            back (str): Back side of flashcard.
            collection_id (int): DB id for the collection that the flashcard is a part of.
            flashcard_id (int, optional): id in DB. DO NOT FILL MANUALLY. Defaults to None.
        """
        self.id = flashcard_id
        self.front = front
        self.back = back
        self.collection_id = collection_id
        self.correct = False
