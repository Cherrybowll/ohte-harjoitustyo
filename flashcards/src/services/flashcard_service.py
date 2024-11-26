from entities.collection import Collection
from entities.flashcard import Flashcard
from entities.user import User

from repositories.user_repository import user_repository as default_user_repository
from repositories.collection_repository import collection_repository as default_collection_repository
from repositories.flashcard_repository import flashcard_repository as default_flashcard_repository


class FlashcardService:
    def __init__(
        self,
        user_repository=default_user_repository,
        collection_repository=default_collection_repository,
        flashcard_repository=default_flashcard_repository
    ):
        self._user_repository = user_repository
        self._collection_repository = collection_repository
        self._flashcard_repository = flashcard_repository
        self._user = None
        self._collection = None
        self._practice_state = [0, 0]


    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user:
            raise ValueError(f"No registered users with name {username}")

        if password != user.password:
            raise ValueError("Wrong username or password")

        self._user = user

        return

    def logout(self):
        self._user = None

    def create_user(self, username, password):
        # note: check username/password criteria
        if self._user_repository.find_by_username(username):
            raise ValueError(f"Username is already taken")

        self._user_repository.create(User(username, password))

        # Logs you in after succesful user creation
        # Needs to fetch user from db for id field
        user = self._user_repository.find_by_username(username)
        self._user = user

        return

    def create_collection(self, name):
        users_collections = self._collection_repository.find_by_creator_id(
            self._user.id)
        of_same_name = list(
            filter(lambda collection: collection.name == name, users_collections))
        if of_same_name:
            raise ValueError(f"You already have a collection named {name}")

        self._collection_repository.create(Collection(name, self._user.id))

        return

    def get_all_collections(self):
        return self._collection_repository.find_all()
    

    def open_collection(self, collection):
        self._collection = collection


    def close_collection(self, collection):
        self._collection = None


    def get_collection(self):
        return self._collection
    

    def create_flashcard(self, front, back):
        self._flashcard_repository.create(Flashcard(front, back, self._collection.id))


    def get_flashcards_from_collection(self):
        return self._flashcard_repository.find_by_collection_id(self._collection.id)


    def start_practice(self):
        self._practice_state[0] = 0
        self._practice_state[1] = len(self._collection.flashcards)


    def progress_practice(self):
        if self._practice_state[0] <= self._practice_state[1]:
            self._practice_state[0] += 1
            return self._practice_state[0]


flashcard_service = FlashcardService()


if __name__ == "__main__":
    pass