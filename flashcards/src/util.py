def validate_username(username):
    if len(username) < 1:
        raise ValueError("Käyttätunnuksen minimipituus on 1 merkki")

    if len(username) > 20:
        raise ValueError("Käyttäjätunnuksen maksimipituus on 20 merkkiä")

def validate_password(password):
    if len(password) < 1:
        raise ValueError("Salasanan minimipituus on 1 merkki")

    if len(password) > 100:
        raise ValueError("Salasanan maksimipituus on 100 merkkiä")

def validate_collection_name(collection_name):
    if len(collection_name) < 1:
        raise ValueError("Kokoelman nimen minimipituus on 1 merkki")
    if len(collection_name) > 30:
        raise ValueError("Kokoelman nimen maksimipituus on 30 merkkiä")

def validate_flashcard_side(side):
    if len(side) < 1:
        raise ValueError("Kortin kentän minimipituus on 1 merkki")
    if len(side) > 100:
        raise ValueError("Kortin kentän maksimipituus on 100 merkkiä")