def validate_username(username):
    """Validates the given username length.

    Args:
        username (str): The username to be validated.
    """
    if len(username) < 1:
        raise ValueError("Käyttätunnuksen minimipituus on 1 merkki")

    if len(username) > 20:
        raise ValueError("Käyttäjätunnuksen maksimipituus on 20 merkkiä")


def validate_password(password, password_repeat):
    """Validates that the password is withing required limits and matches the verification.

    Args:
        password (str): The password.
        password_repeat (str): Repeat of the password.
    """
    if len(password) < 1:
        raise ValueError("Salasanan minimipituus on 1 merkki")

    if len(password) > 100:
        raise ValueError("Salasanan maksimipituus on 100 merkkiä")

    if password != password_repeat:
        raise ValueError("Salasanat eivät täsmää")


def validate_collection_name(collection_name):
    """Validates the length of the collection name.

    Args:
        collection_name (str): Name of the collection.
    """
    if len(collection_name) < 1:
        raise ValueError("Kokoelman nimen minimipituus on 1 merkki")
    if len(collection_name) > 30:
        raise ValueError("Kokoelman nimen maksimipituus on 30 merkkiä")


def validate_flashcard_side(side):
    """Validates the length of the flashcard side.

    Args:
        side (str): Text from the flashcard side.
    """
    if len(side) < 1:
        raise ValueError("Kortin kentän minimipituus on 1 merkki")
    if len(side) > 100:
        raise ValueError("Kortin kentän maksimipituus on 100 merkkiä")
