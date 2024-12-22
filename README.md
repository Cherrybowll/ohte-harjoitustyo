# Flashcard-sovellus

## Kuvaus

Kyseessä on Anki-tyylinen flashcard-sovellus, jossa voi luoda uusia flashcard-kokoelmia ja lisätä niihin flashcardeja. Kokoelmia voi harjoitella ja harjoittelusta saa lopuksi numeerisen palautteen.
Sovelluksessa on myös tavallista käyttäjänhallintaa (käyttäjien rekisteröinti ja sisäänkirjautuminen)

## Release

[Viikon 6 release](https://github.com/Cherrybowll/ohte-harjoitustyo/releases/tag/viikko6)

[Viikon 5 release](https://github.com/Cherrybowll/ohte-harjoitustyo/releases/tag/viikko5)

## Python-versio ja käyttöjärjestelmä

Sovellus on testattu Python-versiolla 3.13.0 käyttäen alustana WSL2.

Sovelluksen asentaminen tarvitsee lisäksi Poetry-asennuksen.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/Cherrybowll/ohte-harjoitustyo/blob/master/flashcards/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/Cherrybowll/ohte-harjoitustyo/blob/master/flashcards/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/Cherrybowll/ohte-harjoitustyo/blob/master/flashcards/dokumentaatio/changelog.md)
- [Luokka/pakkauskaavio](https://github.com/Cherrybowll/ohte-harjoitustyo/blob/master/flashcards/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/Cherrybowll/ohte-harjoitustyo/blob/master/flashcards/dokumentaatio/kayttoohje.md)

## Asennus

1. Hae repositorio laitteellesi joko lataamalla selaimesta tai kloonaamalla jommalla kummalla komennoista (SSH/HTTPS)
```
git@github.com:Cherrybowll/ohte-harjoitustyo.git
git clone https://github.com/Cherrybowll/ohte-harjoitustyo
```

2. Navigoi hakemistoon `flashcards` ja asenna riippuvuudet komennolla
```
poetry install
```

3. Siirry virtuaaliympäristöön komennolla
```
poetry shell
```

4. Alusta tietokanta komennolla
```
invoke formatdb
```

5. Halutessasi käynnistä sovellus komennolla
```
invoke start
```

6. Voit poistua virtuaaliympäristöstä komennolla
```
exit
```

## Komentorivitoiminnot

**HUOM!** Jos olet virtuaaliympäristössä (ks. asennus kohta 3), komentojen alkuosaa `poetry run` ei tarvita.

Tässä oletetaan, että olet navigoinut kansioon `flashcards`

### Ohjelman käynnistäminen

Käynnistä sovellus komennolla
```
poetry run invoke start
```

### Testien suorittaminen
Pytest-testit voi suorittaa komennolla
```
poetry run invoke test
```

### Testikattavuus
Testikattavuusraportin html-tiedostona saa luotua komennolla
```
poetry run invoke coverage-report
```
Raportin polku on `htmlcov/index.html`

### Pylint
Pylint-tarkistukset voi suorittaa komennolla
```
poetry run invoke lint
```
