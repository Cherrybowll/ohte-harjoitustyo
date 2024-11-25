class Flashcard:
    def __init__(self, front, back, collection_id, id=None):
        self.id = id
        self.front = front
        self.back = back
        self.collection_id = collection_id
