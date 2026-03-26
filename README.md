# Kartta-arvauspeli

## Checkpoint 3

## Tämänhetkiset ominaisuudet
Olen rakentanut peliin tarvittavat Maa-oliot ja osan pelilogiikasta. Tällä hetkellä ohjelmassa:
* Luetaan ja yhdistetään maailman maiden tiedot eri JSON-tiedostosta parserin avulla (maiden_tiedot_parser). 
* Luodaan näistä tiedoista "Maa"-olioita, joilla on omat attribuutit (esim. pääkaupunki, kielet, naapurit).
* "Peli"-luokka osaa vasta suodattaa maat maanosittain ja arpoa satunnaisen kohdemaan. Peli-luokka on siis kesken.
* En ole aloittanut vielä graafista käyttöliittymää, eli peli pyörii toistaiseksi vain taustalla. 

## Käyttöohje
* Ohjelmaa ei voi vielä varsinaisesti ajaa, mutta koodin logiikkka voi testata. 
* Voit esimerkiksi ajaa testitiedoston "testi_maiden_tiedot_parser.py", joka tulostaa kaikkien maiden nimet ja sitä maata vastaavat tiedot. Lisäksi lopussa tulostetaan "Finland" -maaolion "str". 

## Aikataulu
* Olen käyttänyt projektiin tähän mennessä noin 15 h.
* Suunnitelmaan tuli pieniä muutoksia, koska en aluksi osannut ajatella, että minun pitäisi alussa kirjoittaa parseri, mikä vei melko kauan aikaa tehdä. 

## Muuta
* Olisin halunnut saada tähän mennessä Peli-luokan valmiiksi, mutta se on vasta melko alussa, joten pieni muutos tässä. 