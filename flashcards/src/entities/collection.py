class Collection:
    def __init__(self, name, creator_id, public=False, collection_id=None):
        self.id = collection_id
        self.name = name
        self.creator_id = creator_id
        self.public = public

    def __str__(self):
        return f"Collection: {self.id}, {self.name} by {self.creator_id}, public={self.public}"
