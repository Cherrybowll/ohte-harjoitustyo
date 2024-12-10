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

## Viikko 4 (20.11-26.11)

### Käyttäjää koskevat ominaisuudet/muutokset
- Käyttäjä voi luoda uusia flashcardeja kokoelmaan ja näkee listauksen kokoelman sisältämistä flashcardeista
- Käyttäjä voi "harjoitella" kokoelmaa näkemällä flashcardit yksitellen
  - Harjoittelusta ei vielä saa mitään palautetta

### Sovelluksen koodia/arkkitehtuuria koskevat ominaisuudet/muutokset
- Luokka FlashcardRepository käsittelee flashcardeja sovelluslogiikan ja tietokannan välillä

## Viikko 5 (27.11-3.12)

### Käyttäjää koskevat ominaisuudet/muutokset
- Käyttäjä näkee harjoitellessa, paljonko harjoiteltavaa on jäljellä
- Harjoittelun päätteeksi käyttäjä näkee palautteen harjoittelusta
  - Oikein ja väärin menneiden määrät
  - Epäonnistuneet flashcardit
- UI-parannuksia: paremmat otsikot, kokoelma-näkymä, flashcardien separaattorit...

### Sovelluksen koodia/arkkitehtuuria koskevat ominaisuudet/muutokset
- Harjoittelun tilan säilyttämisen refaktorointi
- Testit CollectionRepositorylle: kaikkien haku, haku tekijän perusteella, luominen...
- Testit FlashcardRepositorylle, kaikkien haku, haku kokoelman perusteella, luominen...

## Viikko 5 (3.12-10.12)

### Käyttäjää koskevat ominaisuudet/muutokset
- Käyttäjä voi tehdä kokoelmasta julkisen ja näkee muiden julkiset kokoelmat
- Flashcardien ja kokoelmien poistaminen

### Sovelluksen koodia/arkkitehtuuria koskevat ominaisuudet/muutokset
- Lisää testejä flashcard_repository:lle
