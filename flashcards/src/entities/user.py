class User:
    """Class for storing user account information.

    Attributes:
        username: Name of user account.
        password: Password of user account.
        id: Database id for user account.
    """
    def __init__(self, username, password, user_id=None):
        """Class constructor for creating a new user.

        Args:
            username (str): Name of user account.
            password (str): Password of user account.
            user_id (int, optional): id in DB, DO NOT FILL MANUALLY. Defaults to None.
        """
        self.id = user_id
        self.username = username
        self.password = password
