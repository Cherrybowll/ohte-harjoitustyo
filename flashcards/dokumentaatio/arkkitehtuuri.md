# Arkkitehtuurikuvaus

## Rakenne

Ohjelmassa on käytössä kuvanmukainen kerrosarkkitehtuuri (UI, sovelluslogiikka, tietokantaliikenne). Kuvasta ilmenee myös pakkausrakenne.

![luokkapakkauskaavio](https://github.com/user-attachments/assets/94e6a492-e709-41d1-b8e6-77e8123ae1b3)

## Käyttöliittymä

Käyttöliittymässä on 7 näkymää:
- Sisäänkirjautuminen (sovelluksen aloitusnäkymä)
- Rekisteröityminen
- Omat flashcard-kokoelmat
- Flashcardit (yksittäisen kokoelman sisältö)
- Harjoittelu
- Palaute
- Julkiset flashcard-kokoelmat

Jokaisella näkymällä on oma luokka sekä joillain näkymillä on apuluokkia näkymien sisäisten "alinäkymien" (esim. listojen) näyttämiseen. UI-luokka hoitaa näkymien vaihtamisen.

Käyttöliittymä kommunikoi sovelluslogiikan (flashcard_service) kanssa, joka toteuttaa sovelluksen varsinaisen toiminnallisuuden.

## Toiminnallisuudet
Sekvenssikaavioita joistain ei täysin itsestään selvistä ydintoiminnallisuuksista

### Uuden käyttäjän luominen
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant FlashcardService
  participant UserRepository
  User->>UI: click "Rekisteröidy" button
  UI->>FlashcardService: create_user("testikayttaja", "salasana123")
  FlashcardService->>UserRepository: find_by_username("testikayttaja")
  UserRepository-->>FlashcardService: None
  create participant testikayttaja
  FlashcardService->>testikayttaja: User("testikayttaja", "salasana123")
  FlashcardService->>UserRepository: create(testikayttaja)
  UserRepository-->>FlashcardService: testikayttaja
  FlashcardService-->>UI: testikayttaja
  UI->>UI: show_collections_view()
```


### Käyttäjän kirjautuminen
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant FlashcardService
  participant UserRepository
  User->>UI: click "Kirjaudu" button
  UI->>FlashcardService: login("testikayttaja", "salasana123")
  FlashcardService->>UserRepository: find_by_username("testikayttaja")
  UserRepository-->>FlashcardService: testikayttaja
  UI->>UI: show_collections_view()
```

### Kokoelman luominen
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant FlashcardService
  participant CollectionRepository
  User->>UI: click "Luo kokoelma" button
  UI->>FlashcardService: create_collection("kokoelmani")
  FlashcardService->>CollectionRepository: find_by_creator_id(User.id)
  CollectionRepository-->>FlashcardService: []
  create participant kokoelmani
  FlashcardService->>kokoelmani: Collection("kokoelmani")
  FlashcardService->>CollectionRepository: create(kokoelmani)
  FlashcardService-->>UI: True
  UI->>UI: _initialize_collection_list()
```

### Flashcardin luominen
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant FlashcardService
  participant FlashcardRepository
  User->>UI: click "Lisää flashcard" button
  UI->>FlashcardService: create_flashcard("etupuoli", "takapuoli")
  create participant etupuoli
  FlashcardService->>etupuoli: Flashcard("etupuoli")
  FlashcardService->>FlashcardRepository: create(etupuoli)
  FlashcardService-->>UI: True
  UI->>UI: _initialize_flashcard_list()
```
