from entities.flashcard import Flashcard
from entities.user import User

from repositories.user_repository import user_repository as default_user_repository

class FlashcardService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
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

        return

flashcard_service = FlashcardService()