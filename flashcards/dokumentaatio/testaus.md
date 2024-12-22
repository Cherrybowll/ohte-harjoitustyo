# Testausdokumentti

Ohjelma on testattu yksikkö- ja integraatiotasolla unittestillä ja end-to-end -testit on tehty kokeilevalla testaamisella käyttöliittymän kautta. Käyttöliittymää ei testata automaattisesti.

##  Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikan eli `FlashcardService`-luokan testaamisesta vastaa hakemistossa `tests/services/` sijaitsevat testitiedostot. Testejä on jaettu eri tiedostoihin selkeyden vuoksi.

### Repositoriot

Datan hakemisesta ja tallentamisesta tietokannan ja sovelluslogiikan välillä vastaavien repositorioluokkien `UserRepository`, `CollectionRepository` ja `FlashcardRepository` testit sijaitsevat
hakemistossa `tests/repositories`. Testit käyttävät `.env.test`-tiedostossa määriteltyä testitietokantaa, joten testit eivät vaikuta käyttäjän omaan tietokantaan.

### Testauskattavuus

tähän kuva

## Järjestelmätestaus

Järjestelmätestaus tehtiin kokeilevasti.

Järjestelmätestauksen perusteella sovelluksessa toimii:
- Lataaminen/hakeminen Githubista ja asennus dokumentaation ohjeiden perusteella
- `.env`-tiedoston ympäristömuuttujien vaihtaminen
- Määrittelydokumentissa mainitut ominaisuudet

## Tunnettuja ongelmia

- Sovellus ei toimi kunnolla, jos tietokantaa ei ole alustettu ohjeiden mukaisesti
- Sovellus ei todennäköisesti toimi, jos tietokantatiedostoon ei ole luku- tai kirjoitusoikeuksia
- Tkinterin `simpledialog.askstring`-dialogilaatikko ei vastaa sovelluksen muuta visuaalista teemaa
