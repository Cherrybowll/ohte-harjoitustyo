from entities.collection import Collection
from entities.flashcard import Flashcard
from entities.user import User

from repositories.user_repository import user_repository as dflt_user_repository
from repositories.collection_repository import collection_repository as dflt_collection_repository
from repositories.flashcard_repository import flashcard_repository as dflt_flashcard_repository


class FlashcardService:
    def __init__(
        self,
        user_repository=dflt_user_repository,
        collection_repository=dflt_collection_repository,
        flashcard_repository=dflt_flashcard_repository
    ):
        self._user_repository = user_repository
        self._collection_repository = collection_repository
        self._flashcard_repository = flashcard_repository
        self._user = None
        self._collection = None
        self._practice_state = {
            "current_card": 0,
            "total_cards": 0,
            "result_list": []
        }

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user:
            raise ValueError(f"No registered users with name {username}")

        if password != user.password:
            raise ValueError("Wrong username or password")

        self._user = user

    def logout(self):
        self._user = None

    def create_user(self, username, password):
        # note: check username/password criteria
        if self._user_repository.find_by_username(username):
            raise ValueError(f"Username {username} is already taken")

        self._user_repository.create(User(username, password))

        # Logs you in after succesful user creation
        # Needs to fetch user from db for id field
        user = self._user_repository.find_by_username(username)
        self._user = user

    def create_collection(self, name):
        users_collections = self._collection_repository.find_by_creator_id(
            self._user.id)
        of_same_name = list(
            filter(lambda collection: collection.name == name, users_collections))
        if of_same_name:
            raise ValueError(f"You already have a collection named {name}")

        self._collection_repository.create(Collection(name, self._user.id))

    def get_all_collections(self):
        return self._collection_repository.find_all()

    def open_collection(self, collection):
        self._collection = collection

    def close_collection(self):
        self._collection = None

    def get_collection(self):
        return self._collection

    def create_flashcard(self, front, back):
        # note: add validation
        self._flashcard_repository.create(
            Flashcard(front, back, self._collection.id))

    def get_flashcards_from_collection(self):
        return self._flashcard_repository.find_by_collection_id(self._collection.id)

    def collection_not_empty(self):
        return len(self.get_flashcards_from_collection()) > 0

    def start_practice(self):
        self._practice_state["current_card"] = 0
        self._practice_state["total_cards"] = len(
            self.get_flashcards_from_collection())-1
        self._practice_state["results_list"] = [False] * \
            (self._practice_state["total_cards"]+1)

    def progress_practice(self, correct):
        if self._practice_state["current_card"] < self._practice_state["total_cards"]:
            self._practice_state["results_list"][self._practice_state["current_card"]] = correct
            self._practice_state["current_card"] += 1
            return True

        self._practice_state["results_list"][self._practice_state["current_card"]] = correct
        return False

    def current_flashcard(self):
        return self._practice_state["current_card"]

    # Useless?
    def total_flashcards(self):
        return self._practice_state["total_cards"]

    def get_practice_results_correct(self):
        correct_results = []
        flashcards = self.get_flashcards_from_collection()
        for i in range(self._practice_state["total_cards"]+1):
            if self._practice_state["results_list"][i]:
                correct_results.append(flashcards[i])
        return correct_results

    def get_practice_results_incorrect(self):
        incorrect_results = []
        flashcards = self.get_flashcards_from_collection()
        for i in range(self._practice_state["total_cards"]+1):
            if not self._practice_state["results_list"][i]:
                incorrect_results.append(flashcards[i])
        return incorrect_results

    def reset_practice_state(self):
        self._practice_state["current_card"] = 0
        self._practice_state["total_cards"] = 0
        self._practice_state["results_list"] = []


flashcard_service = FlashcardService()


if __name__ == "__main__":
    pass
