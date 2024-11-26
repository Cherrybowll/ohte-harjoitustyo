class Collection:
    def __init__(self, name, creator_id, id=None):
        self.id = id
        self.name = name
        self.creator_id = creator_id

    def __str__(self):
        return f"Collection: {self.id}, {self.name}, {self.creator_id}, {self.flashcards}"