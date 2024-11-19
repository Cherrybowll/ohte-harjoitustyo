class Flashcard:
    def __init__(self, front, back, user, collection, id=None):
        self.id = id
        self.front = front
        self.back = back
        self.user = user
        self.collection = collection