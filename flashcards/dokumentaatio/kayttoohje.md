# Käyttöohje

## Repositorion lataaminen

Lataa ohjelman lähdekoodi [release-sivulta](https://github.com/Cherrybowll/ohte-harjoitustyo/releases) valitsemasi releasen *Assets*-osiosta (Source code).

## Ohjelman asennus

1. Navigoi hakemistoon `flashcards` ja asenna riippuvuudet komennolla
```
poetry install
```

2. Siirry virtuaaliympäristöön komennolla
```
poetry shell
```

3. Alusta tietokanta komennolla
```
invoke formatdb
```

Voit lopuksi poistua virtuaaliympäristöstä komennolla
```
exit
```

## Ohjelman käynnistys

Käynnistä sovellus komennolla
```
invoke start
```

## Rekisteröityminen

Paina aloitusnäkymässä painiketta *Rekisteröidy*

Syötä käyttäjänimi, salasana sekä salasanan vahvistus niille osoitettuihin kenttiin.

Lopuksi paina *Rekisteröidy*-painiketta. Sovellus kirjaa sinut automaattisesti sisään, mikäli rekisteröityminen onnistui.

## Kirjautuminen

Aloitusnäkymässä syötä käyttäjänimesi ja salasanasi niille osoitettuihin kenttiin ja paina *Kirjaudu*-painiketta.

## Uloskirjautuminen

Sisäänkirjautumisen jälkeisessä kokoelma-näkymästä voi kirjautua ulos painamalla *Kirjaudu ulos* -painiketta.

## Flashcard-kokoelman luominen, avaaminen ja poistaminen

Kirjoita kokoelman nimi tyhjään tekstikenttään ja paina *Luo kokoelma* -painiketta.
Voit tehdä kokoelmasta julkisen painamalla *Julkinen*-painiketta listanäkymässä.

Voit tarkastella kokoelman sisältöä painamalla painiketta *Avaa* kokoelman nimen vieressä listanäkymässä.

Kokoelman voi poistaa painamalla *Poista*-painiketta kokoelman nimen vieressä listanäkymässä.
Sovellus kysyy, haluatko varmasti jatkaa.

## Uusien flashcardien luominen ja poistaminen

Voit luoda uuden flashcardin kirjoittamalla sen etupuolen ja takapuolen tekstit niille osoitettuihin kenttiin ja painamalla *Lisää flashcard* -painiketta.

Voit poistaa luodun flashcardin painamalla *Poista*-painiketta listanäkymässä.

## Flashcardien harjoittelu

Harjoittelun voi aloittaa painamalla kokoelmassa *Harjoittele kokoelmaa* -painiketta.

Sovellus näyttää yhden flashcardin kerrallaan. Näet ensin yhden kortin etupuolen ja ollessasi valmis näet kortin takapuolen painamalla *Käännä*-painiketta.
Kun näet kortin takapuolen, voit edetä painamalla *Kyllä*- tai *Ei*-painiketta. Valitse painike sen mukaan, tiesitkö kortin takapuolen sille antamasi etupuolen perusteella.

Lopuksi harjoittelusta saa palautteen. Kun olet tarkastellut palautetta riittävästi, voit palata kokoelmaan painamalla *Palaa kokoelmaan* -painiketta.
