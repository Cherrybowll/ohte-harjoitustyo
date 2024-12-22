from entities.collection import Collection
from entities.flashcard import Flashcard
from entities.user import User
import util

from repositories.user_repository import user_repository as dflt_user_repository
from repositories.collection_repository import collection_repository as dflt_collection_repository
from repositories.flashcard_repository import flashcard_repository as dflt_flashcard_repository


class FlashcardService:
    """Class for handling application logic.
    Retrieves data from repositories and is called by the UI.
    """
    def __init__(
        self,
        user_repository=dflt_user_repository,
        collection_repository=dflt_collection_repository,
        flashcard_repository=dflt_flashcard_repository
    ):
        """Constructor for the class FlashcardService.

        Args:
            user_repository (UserRepository, optional): Instance of UserRepository.Defaults to dflt_user_repository.
            collection_repository (CollectionRepository, optional): Instance of CollectionRepository. Defaults to dflt_collection_repository.
            flashcard_repository (FlashcardRepository, optional): Instance of FlashcardRepository. Defaults to dflt_flashcard_repository.
        """
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
        self._viewing_public = False
        self._message = None

    def login(self, username, password):
        """Attempts to log the user in. With incorrect credentials calls the set_message method.

        Args:
            username (str): Username of the account.
            password (str): Password of the account.

        Returns:
            bool: Boolean value depicting whether the login was succesful.
        """
        user = self._user_repository.find_by_username(username)

        if not user:
            self.set_message(f"No registered users with name {username}")
            return False

        if password != user.password:
            self.set_message("Wrong username or password")
            return False

        self._user = user
        return True

    def logout(self):
        """Logs the user out.
        """
        self._user = None

    def get_user_id(self):
        """Returns the id of the current user.

        Returns:
            int: id of the current user.
        """
        return self._user.id

    def create_user(self, username, password, password_repeat):
        """Creates a new user if the username isn't already taken and the username and password meet the criteria. Also logs the user in.

        Args:
            username (str): Username of the account to be created.
            password (str): Password of the account to be created.
            password_repeat (str): Verification of the password.

        Returns:
            bool: Boolean value depicting whether the account creation was succesful.
        """
        if self._user_repository.find_by_username(username):
            self.set_message(f"Username {username} is already taken")
            return False

        try:
            util.validate_username(username)
        except ValueError as error:
            self.set_message(error)
            return False
        try:
            util.validate_password(password, password_repeat)
        except ValueError as error:
            self.set_message(error)
            return False

        self._user_repository.create(User(username, password))

        # Logs you in after succesful user creation
        # Needs to fetch user from db for id field
        user = self._user_repository.find_by_username(username)
        self._user = user

        return True

    def create_collection(self, name):
        """Creates a new flashcard collection.

        Args:
            name (str): Name of the collection to be created.

        Returns:
            bool: Boolean value depicting whether creating the collection was succesful.
        """
        if self.get_collection_from_user_with_name(self._user.id, name):
            self.set_message(f"You already have a collection named {name}")
            return False

        try:
            util.validate_collection_name(name)
        except ValueError as error:
            self.set_message(error)
            return False

        self._collection_repository.create(Collection(name, self._user.id))
        return True

    def get_all_public_collections(self):
        """Returns all public collections.

        Returns:
            list: list of Collection entities.
        """
        return self._collection_repository.find_all_public()

    def get_collections_from_user(self):
        """Returns all collections from the current user.

        Returns:
            list: list of Collection entities.
        """
        return self._collection_repository.find_by_creator_id(self._user.id)

    def get_collection_from_user_with_name(self, user_id, collection_name):
        """Returns collection with the specified name and creator.

        Args:
            user_id (int): id of the user that created the collection.
            collection_name (str): Name of the collection.

        Returns:
            Collection: a Collection entity or None if nothing was found.
        """
        users_collections = self._collection_repository.find_by_creator_id(
            user_id)
        of_same_name = list(
            filter(lambda collection: collection.name == collection_name, users_collections))
        if of_same_name:
            return of_same_name[0]
        return None

    def delete_collection(self, collection):
        """Deletes the specified collection.

        Args:
            collection (Collection): a Collection entity.
        """
        self._collection_repository.delete_by_id(collection.id)
        self._flashcard_repository.delete_by_collection_id(collection.id)

    def open_collection(self, collection):
        """Opens the collection as the current collection.

        Args:
            collection (Collection): a Collection entity.
        """
        self._collection = collection

    def close_collection(self):
        """Closes the current collection.
        """
        self._collection = None

    def get_collection(self):
        """Returns the current collection.

        Returns:
            Collection: a Collection entity.
        """
        return self._collection

    def collection_toggle_public(self, collection):
        """Toggles the given collection's publicity status.

        Args:
            collection (Collection): a Collection entity
        """
        if collection.public:
            self._collection_repository.change_publicity(collection.id, False)
        else:
            self._collection_repository.change_publicity(collection.id, True)

    def set_public_view_state(self, view: bool):
        """Sets whether the current user is viewing public or private collections.

        Args:
            view (bool): True, if setting the view to public collections. False for private.
        """
        self._viewing_public = view

    def get_public_view_state(self):
        """Returns whether the user is viewing public or private collections.

        Returns:
            bool: True if viewing public, False if viewing private.
        """
        return self._viewing_public

    def create_flashcard(self, front, back, collection_id):
        """Creates a new flashcard into the specified collection.

        Args:
            front (str): The front side of the flashcard.
            back (str): The back side of the flashcard.
            collection_id (int): id of the parent collection.

        Returns:
            bool: Boolean value depicting whether creating the flashcard was succesful.
        """
        try:
            util.validate_flashcard_side(front)
        except ValueError as error:
            self.set_message(error)
            return False
        try:
            util.validate_flashcard_side(back)
        except ValueError as error:
            self.set_message(error)
            return False

        self._flashcard_repository.create(
            Flashcard(front, back, collection_id))
        return True

    def get_flashcards_from_collection(self, collection):
        """Returns the flashcards from the specified collection.

        Args:
            collection (Collection): a Collection entity.

        Returns:
            list: list of Flashcard entities.
        """
        return self._flashcard_repository.find_by_collection_id(collection.id)

    def delete_flashcard(self, flashcard):
        """Deletes the given flashcard.

        Args:
            flashcard (Flashcard): a Flashcard entity.
        """
        self._flashcard_repository.delete_by_id(flashcard.id)

    def collection_not_empty(self):
        """Returns whether the current collection is empty.

        Returns:
            bool: True if the collection has at least one flashcard in it.
        """
        return len(self.get_flashcards_from_collection(self._collection)) > 0

    def start_practice(self):
        """Initializes the data structures for progress and results in practice mode.
        """
        self._practice_state["current_card"] = 0
        self._practice_state["total_cards"] = len(
            self.get_flashcards_from_collection(self._collection))-1
        self._practice_state["results_list"] = [False] * \
            (self._practice_state["total_cards"]+1)

    def progress_practice(self, correct):
        """Progresses the practice state and stores the last answer.

        Args:
            correct (bool): Value depicting whether the answer for the card before progressing was correct.

        Returns:
            bool: Value depicting if there are more flashcards in the collection being practiced.
        """
        if self._practice_state["current_card"] < self._practice_state["total_cards"]:
            self._practice_state["results_list"][self._practice_state["current_card"]] = correct
            self._practice_state["current_card"] += 1
            return True

        self._practice_state["results_list"][self._practice_state["current_card"]] = correct
        return False

    def current_flashcard(self):
        """Returns the ordinal number of the flashcard in the collection being practiced.

        Returns:
            int: Ordinal number of the flashcard in the collection being practiced.
        """
        return self._practice_state["current_card"]

    def get_practice_results(self, correct: bool):
        """Returns the correct or incorrect answers (flashcards) from the practice state.

        Args:
            correct (bool): True for correct results, False for incorrect results.

        Returns:
            list: list of Flashcard entities.
        """
        results = []
        flashcards = self.get_flashcards_from_collection(self._collection)
        for i in range(self._practice_state["total_cards"]+1):
            if self._practice_state["results_list"][i] == correct:
                results.append(flashcards[i])
        return results

    # USELESS ???
    def reset_practice_state(self):
        """Resets the practice state.
        """
        self._practice_state["current_card"] = 0
        self._practice_state["total_cards"] = 0
        self._practice_state["results_list"] = []

    def get_message(self):
        """Returns the message attribute and sets it to None. Used for flashing messages.

        Returns:
            str: Message.
        """
        returned_message = self._message
        self._message = None
        return returned_message

    def set_message(self, message):
        """Sets the message attribute. Used for flashing messages.

        Args:
            message (str): Message.
        """
        self._message = message


flashcard_service = FlashcardService()


if __name__ == "__main__":
    pass
