class Flashcard:
    def __init__(self, front, back, collection_id, flashcard_id=None):
        self.id = flashcard_id
        self.front = front
        self.back = back
        self.collection_id = collection_id
        self.correct = False
