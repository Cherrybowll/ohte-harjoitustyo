class Collection:
    def __init__(self, name, creator_id, collection_id=None):
        self.id = collection_id
        self.name = name
        self.creator_id = creator_id

    def __str__(self):
        return f"Collection: {self.id}, {self.name}, {self.creator_id}"
