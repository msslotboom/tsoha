# tsoha

## Ajanhallintasovellus

Sovelluksessa voi nähdä kuinka paljon tiimin jäsenet käyttää aikaa mihinkä tehtävään. 
Projektissa on seuraavat ominaisuudet:
- Käyttäjä ja ylläpitäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Projektin ylläpitäjä voi tehdä tiimin, ja lisätä tehtäviä ja käyttäjiä sinne
- Ylläpitäjä voi kirjata montako tuntia jokaista tehtävää pitää tehdä per viikko
- Ylläpitäjä voi muokata tehtävien määrää, tuntimäärää ja poistaa käyttäjiä
- Käyttäjä voi kirjata montako tuntia on tehnyt tehtävää päivässä
- Käyttäjä voi nähdä montako tuntia on käyttänyt jokaiseen tehtävään
- Käyttäjät ja ylläpitäjä voi nähdä kuinka paljon tiimi on käyttänyt jokaiseen tehtävään, ja miten se vertaa tavoitteeseen


Ohjelmaan pitää tehdä .env tiedosto jossa on seuraavat tiedot:
`DATABASE_URL=postgresql:///tietokannan_nimi
SECRET_KEY=`
Johon pitää täyttää tietokannan nimi ja salainen koodi minkä saa valita itse. Tietokannan alustaminen onnistuu komennolla psql < schema.sql
