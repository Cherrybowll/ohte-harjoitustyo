# Arkkitehtuurikuvaus

## Rakenne

Ohjelmassa on käytössä kuvanmukainen kerrosarkkitehtuuri (UI, sovelluslogiikka, tietokantaliikenne). Kuvasta ilmenee myös pakkausrakenne.

![luokkapakkauskaavio](https://github.com/user-attachments/assets/94e6a492-e709-41d1-b8e6-77e8123ae1b3)

## Käyttöliittymä

Käyttöliittymässä on 6 näkymää:
- Sisäänkirjautuminen (sovelluksen aloitusnäkymä)
- Rekisteröityminen
- Flashcard-kokoelmat (voi vaihtaa yksityisten ja kaikkien julkisten välillä)
- Flashcardit (yksittäisen kokoelman sisältö)
- Harjoittelu
- Palaute

Jokaisella näkymällä on oma luokka sekä joillain näkymillä on apuluokkia näkymien sisäisten "alinäkymien" (esim. listojen) näyttämiseen. UI-luokka hoitaa näkymien vaihtamisen.

Käyttöliittymä kommunikoi sovelluslogiikan (`flashcard_service`) kanssa, joka toteuttaa sovelluksen varsinaisen toiminnallisuuden.

## Sovelluslogiikka

Sovelluslogiikasta vastaa täysin (tai niin pitkälti kuin se on saatu käyttöliittymästä erotettua), luokka `FlashcardService`.
Käyttöliittymä kutsuu sovelluslogiikan metodeja, jotka taas muuttavat sovelluksen tilaa ja kutsuvat edelleen repositorioita tietokantaoperaatioita varten.

Sovelluslogiikan metodit vastaavasti palauttavat tarvittaessa tietoa kutsujen onnistumisesta, jotta käyttöliittymä tietää, mitä muutoksia näkymässä tulisi tapahtua.

## Tietojen tallennus

Sovellus käyttää kaikkeen tiedon tallentamiseen ja hakemiseen SQLite-tietokantaa, jossa on kolme (3) taulua:
- `users`, joka sisältää käyttäjien tunnusten tiedot
- `collections`, joka sisältää flashcard-kokoelmien tiedot
- `flashcards`, joka sisältää flashcardien tiedot

Vastaavasti repositoriot `UserRepository`, `CollectionRepository` ja `FlashcardRepository` hoitavat tietokantoihin liittyvät kyselyt.

Tietokantataulut määritellään tiedostossa `flashcards/src/initialize_database.py`, joka löytyy [täältä](https://github.com/Cherrybowll/ohte-harjoitustyo/blob/master/flashcards/src/initialize_database.py).

Tietokantatiedosto määritellään tiedostossa `flashcards/.env`, muuttujassa `DATABASE_FILENAME` (oletuksena `database.sqlite`).
Tiedoston sijaitsee hakemistossa `flashcards/data/`

## Toiminnallisuudet

Sekvenssikaavioita ydintoiminnallisuuksista.

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

### Muut toiminnallisuudet

Sovelluksesta löytyy paljon muitakin ominaisuuksia, joiden sekvenssikaaviot toistavat samaa logiikkaa:
- Käyttäjä yrittää tehdä jonkin toiminnon käyttöliittymän kautta
- Käyttöliittymä kutsuu toiminnosta vastaavaa metodia sovelluslogiikan palvelusta `FlashcardService`
- Sovelluslogiikka kutsuu tarvittaessa repositorioiden metodeja datan hakemista tai tallentamista varten
- Repositoriot tekevät tietokantakyselyt ja palauttavat tiedon sovelluslogiikalle
- Sovelluslogiikka käsittelee dataa toivotulla tavalla
- Sovelluslogiikka palauttaa käyttöliittymälle tietoa, jonka perusteella käyttöliittymä päättelee, pitääkö näkymän muuttua

### Rakenteelliset heikkoudet

Välttääkseni todella copy-pastettuja UI-näkymiä, jouduin lisäämään jonkin verran tarkistuksia käyttöliittymäkoodiin, joka osaltaan,
vaikkakin melko pienissä määrin, kaventaa eroa käyttöliittymän ja sovelluslogiikan välillä.

Tietoa hakevissa metodeissa saattaa olla vielä pientä copy-pasten tuntua, vaikka sain niitä loppupalautusta varten paljon siivottua.
