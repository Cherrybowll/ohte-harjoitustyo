# (Alustava) Vaatimusmäärittely

## Sovelluksen käyttötarkoitus

Sovelluksella käyttäjä voi luoda *flashcard*-kokoelmia ja harjoitella niiden sisältöjä.
Jokaisella *flashcardilla* on kaksi puolta, joista harjoitellessa ns. etupuoli näytetään käyttäjälle.
Käyttäjä voi kääntää *flashcardin*, jolloin hän näkee *flashcardin* takapuolen ja kertoo sovellukselle, muistiko sisällön oikein.

Harjoittelun päätteeksi käyttäjä saa palautetta (oikeiden vastausten osuus ja mitkä vastaukset olivat väärin).

Sovellukseen voi luoda useita käyttäjiä, jotka ylläpitävät omia *flashcard*-kokoelmiaan.

## Käyttäjät

Sovelluksessa tulee lähtökohtaisesti olemaan vain tavallisia käyttäjiä ellei ylläpitäjäkäyttäjille ilmene tarvetta mahdollisen sovelluksen laajentamisen myötä.

## Toiminnallisuus

### Käyttäjätunnuksen hallinta

- Käyttäjä voi rekisteröidä uuden käyttäjätunnuksen [tehty]
  - Käyttäjätunnuksen tulee olla uniikki ja pituudeltaan 1-20 merkkiä [tehty]
  - Käyttäjätunnukselle tulee määrittää salasana (joka annetaan kahdesti) [tehty]
- Käyttäjä voi kirjautua sisään olemassa olevalle käyttäjälle [tehty]
  - Käyttäjätunnuksen ja salasanan tulee täsmätä olemassa olevaan käyttäjään [tehty]
  - Käyttäjä ei voi tehdä sovelluksessa muuta ennen käyttäjän onnistunutta rekisteröimistä ja sisäänkirjautumista [tehty]
- Käyttäjä voi kirjautua ulos sovelluksesta [tehty]

### Flashcardit

- Käyttäjä voi luoda uuden *flashcard*-kokoelman ja nimetä sen [tehty]
  - Kokoelman nimen tulee olla uniikki ja pituudeltaan 1-30 merkkiä [tehty]
- Käyttäjä voi lisätä kokoelmaan uuden *flashcardin* [tehty]
   - Käyttäjä pystyy kirjoittamaan *flashcardin* etu- ja takapuolelle tekstiä [tehty]
     - Kummankin puolen pituus tulee alustavasti olla väliltä 1-100 merkkiä [tehty]
- Käyttäjä voi harjoitella yksittäistä kokoelmaa [tehty]
  - Käyttäjä näkee aluksi kortin etupuolen ja voi kääntää kortin [tehty]
  - Käyttäjä näkee käännetyn kortin takapuolen ja ilmoittaa osasiko sen [tehty]
  - Käyttäjä näkee harjoitellun edistymisasteen (eli montako korttia jäljellä) [tehty]
  - Kun kaikki *flashcardit* on käyty läpi, sovellus antaa palautteen [tehty]
    - Oikeat vastaukset suhteessa korttien kokonaismäärään [tehty]
    - Yksittäiset kortit (etu- ja takapuoli), jotka menivät väärin [tehty]

## Toteutetut / toteutuvat laajennukset sovellukseen

- Käyttäjä voi merkitä *flashcard*-kokoelman julkiseksi, jolloin muut käyttäjät voivat löytää sen julkisesta valikosta ja tallentaa omaksi kokoelmakseen
  - Kokoelman voi tehdä julkiseksi [tehty]
  - Muut käyttäjät voivat tarkastella toistensa julkisia kokoelmia [tehty]
  - Muut käyttäjät eivät voi poistaa toisten julkisia kokoelmia [tehty]
  - Muut käyttäjät eivät voi muokata toisten julkisia kokoelmia
  - Muiden käyttäjien julkiset kokoelmat voi tallentaa itselleen

## Mahdolliset laajennukset sovellukseen



- Erilaisia *flashcard*-tyyppejä
  - Oikein/väärin -vastausvaihtoehdot
  - Kirjoitettava oikea kortin takapuoli tekstikenttään
