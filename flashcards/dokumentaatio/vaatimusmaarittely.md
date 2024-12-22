# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus

Sovelluksella käyttäjä voi luoda *flashcard*-kokoelmia ja harjoitella niiden sisältöjä.
Jokaisella *flashcardilla* on kaksi puolta, joista harjoitellessa ns. etupuoli näytetään käyttäjälle.
Käyttäjä voi kääntää *flashcardin*, jolloin hän näkee *flashcardin* takapuolen ja kertoo sovellukselle, muistiko sisällön oikein.

Harjoittelun päätteeksi käyttäjä saa palautetta (oikeiden vastausten osuus ja mitkä vastauksista olivat väärin).

Sovellukseen voi luoda useita käyttäjiä, jotka ylläpitävät omia *flashcard*-kokoelmiaan. Omia kokoelmia voi asettaa julkisiksi ja muiden käyttäjien julkisia kokoelmia voi tarkastella ja harjoitella.

Sekä omia että muiden julkisia kokoelmia voi kopioida, jos ne haluaa omiksi kokoelmikseen. Kopioituja kokoelmia voi edelleen muokata.

## Käyttäjät

Sovelluksessa on vain tavallisia käyttäjiä.

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
- Käyttäjä voi poistaa luomaansa *flashcard*-sisältöä [tehty]
  - Käyttäjä voi poistaa kokoelmasta yksittäisiä *flashcardeja* [tehty]
  - Käyttäjä voi poistaa kokonaisen *flashcard*-kokoelman [tehty]
    - Kokoelman poistaminen edellyttää erillisen vahvistuksen [tehty]
- Käyttäjä voi harjoitella yksittäistä kokoelmaa [tehty]
  - Käyttäjä näkee aluksi kortin etupuolen ja voi kääntää kortin [tehty]
  - Käyttäjä näkee käännetyn kortin takapuolen ja ilmoittaa osasiko sen [tehty]
  - Käyttäjä näkee harjoitellun edistymisasteen (eli montako korttia jäljellä) [tehty]
  - Kun kaikki *flashcardit* on käyty läpi, sovellus antaa palautteen [tehty]
    - Oikeat vastaukset suhteessa korttien kokonaismäärään [tehty]
    - Yksittäiset kortit (etu- ja takapuoli), jotka menivät väärin [tehty]
- Käyttäjä voi merkitä *flashcard*-kokoelman julkiseksi, jolloin muut käyttäjät voivat löytää sen julkisesta valikosta ja tallentaa omaksi kokoelmakseen [tehty]
  - Käyttäjä voi vaihtaa kokoelman näkyvyyttä yksityisen ja julkisen välillä [tehty]
  - Käyttäjä voi tarkastella toisten käyttäjien julkisia kokoelmia [tehty]
  - Käyttäjä ei voi poistaa toisten käyttäjien julkisia kokoelmia [tehty]
  - Käyttäjä ei voi poistaa tai lisätä *flashcardeja* toisten käyttäjien julkisiin kokoelmiin [tehty]
- Käyttäjä voi kopioida kokoelmia [tehty]
  - Kopioidessa sovellus pyytää nimen uudelle kokoelmalle ja validoi sen tavallisesti [tehty]
  - Kopio sisältää samat *flashcardit* kuin alkuperäinen kokoelma [tehty]
  - Käyttäjä voi kopioida sekä omiaan että muiden julkisia kokoelmia [tehty]
