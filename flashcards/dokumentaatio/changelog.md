# Changelog

## Viikko 3 (13.11-19.11)

### Käyttäjää koskevat ominaisuudet/muutokset
- Käyttäjä voi luoda uuden tunnuksen sekä kirjautua sisään ja ulos olemassa olevalla tunnuksella
- Käyttäjä voi luoda uusia flashcard-kokoelmia (tyhjiä) ja näkee listan kaikista tallennetuista kokoelmista
- Alkeellinen graafinen käyttöliittymä mahdollistaa yllä mainitut toiminnot

### Sovelluksen koodia/arkkitehtuuria koskevat ominaisuudet/muutokset
- Luokka UserRepository käsittelee käyttäjien tietoja sovelluslogiikan ja tietokannan välillä
- Luokka CollectionRepository käsittelee luotuja flashcard-kokoelmia sovelluslogiikan ja tietokannan välillä
- Luokka FlashcardService toteuttaa sovelluslogiikkaa
- Testit UserRepositorylle: kaikkien käyttäjien haku, käyttäjien haku nimellä, kaikkien käyttäjien poistaminen
