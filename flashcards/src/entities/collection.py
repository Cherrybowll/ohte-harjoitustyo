class Collection:
    """Class for storing flashcard collections.

    Attributes:
        name: Name of collection.
        creator_id: id of user that created the collection.
        public: Collection's publicity status.
        id: id in DB.
    """

    def __init__(self, name, creator_id, public=False, collection_id=None):
        """Class constructor for creating new collections.

        Args:
            name (str): Name of collection.
            creator_id (int): id of user that created the collection.
            public (bool, optional): Collection's publicity status. Defaults to False.
            collection_id (int, optional): id in DB. DO NOT FILL MANUALLY. Defaults to None.
        """
        self.id = collection_id
        self.name = name
        self.creator_id = creator_id
        self.public = public

    def __str__(self):
        """String representation for class Collection
        """
        return f"Collection: {self.id}, {self.name} by {self.creator_id}, public={self.public}"
