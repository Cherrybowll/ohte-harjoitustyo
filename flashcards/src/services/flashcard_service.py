from entities.collection import Collection
from entities.flashcard import Flashcard
from entities.user import User

from repositories.user_repository import user_repository as default_user_repository
from repositories.collection_repository import collection_repository as default_collection_repository

class FlashcardService:
    def __init__(
        self,
        user_repository=default_user_repository,
        collection_repository=default_collection_repository
    ):
        self._user_repository = user_repository
        self._collection_repository = collection_repository
        self._user = None
    
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
        #note: check username/password criteria
        if self._user_repository.find_by_username(username):
            raise ValueError(f"Username is already taken")
        
        self._user_repository.create(User(username, password))

        #Logs you in after succesful user creation
        #Needs to fetch user from db for id field
        user = self._user_repository.find_by_username(username)
        self._user = user

        return
    
    def create_collection(self, name):
        users_collections = self._collection_repository.find_by_creator_id(self._user.id)
        of_same_name = list(filter(lambda collection: collection.name==name, users_collections))
        if of_same_name:
            raise ValueError(f"You already have a collection named {name}")
        
        self._collection_repository.create(Collection(name, self._user.id))

        return
    
    def get_all_collections(self):
        return self._collection_repository.find_all()

flashcard_service = FlashcardService()