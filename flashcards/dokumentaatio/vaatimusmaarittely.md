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

- Käyttäjä voi rekisteröidä uuden käyttäjätunnuksen
  - Käyttäjätunnuksen tulee olla uniikki ja pituudeltaan vähintään yksi (1) merkki (saattaa muuttua myöhemmin)
  - Käyttäjätunnukselle tulee määrittää salasana (joka annetaan kahdesti)
- Käyttäjä voi kirjautua sisään olemassa olevalle käyttäjälle
  - Käyttäjätunnuksen ja salasanan tulee täsmätä olemassa olevaan käyttäjään
  - Käyttäjä ei voi tehdä sovelluksella muuta ennen käyttäjän onnistunutta rekisteröimistä ja sisäänkirjautumista
- Käyttäjä voi kirjautua ulos sovelluksesta

### Flashcardit

- Käyttäjä voi luoda uuden *flashcard*-kokoelman ja nimetä sen
  - Kokoelman nimen tulee olla uniikki ja pituudeltaan vähintään yksi (1) merkki
- Käyttäjä voi lisätä kokoelmaan uuden *flashcardin*
   - Käyttäjä pystyy kirjoittamaan *flashcardin* etu- ja takapuolelle tekstiä
     - Kummankin puolen pituus tulee alustavasti olla väliltä 1-100 merkkiä
- Käyttäjä voi harjoitella yksittäistä kokoelmaa
  - Käyttäjä näkee aluksi kortin etupuolen ja voi kääntää kortin
  - Käyttäjä näkee käännetyn kortin takapuolen ja ilmoittaa osasiko sen
  - Kun kaikki *flashcardit* on käyty läpi, sovellus antaa palautteen
    - Oikeat vastaukset suhteessa korttien kokonaismäärään
    - Yksittäiset kortit (etu- ja takapuoli), jotka menivät väärin

## Mahdolliset laajennukset sovellukseen

- Käyttäjä voi merkitä *flashcard*-kokoelman julkiseksi, jolloin muut käyttäjät voivat löytää sen julkisesta valikosta ja tallentaa omaksi kokoelmakseen
- Erilaisia *flashcard*-tyyppejä
  - Oikein/väärin -vastausvaihtoehdot
  - Kirjoitettava oikea kortin takapuoli tekstikenttään