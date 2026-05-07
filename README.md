# Kartta-arvauspeli (2026)
* Kartta-arvauspeli on interaktiivinen peli, jossa pelaaja arvaa maita, saa vinkkejä väärien vastausten jälkeen, saa lukea maan perustiedot, ansaita pisteitä ja haastaa itseään aikaa vastaan. 

## Tekijä
* Dan Le
* dan.le@aalto.fi



## Pelin ominaisuudet
Olen rakentanut Olio-ohjelmoinnilla Interaktiivisen karttapelin. Pelissä
* Luetaan ja yhdistetään maailman maiden tiedot eri JSON-tiedostosta parserin avulla (maiden_tiedot_parser). 
* Luodaan näistä tiedoista Maa-olioita, joilla on omat attribuutit (esim. pääkaupunki, kielet, naapurit).
* Peli-luokkassa metodit mm. arpoo pelin maat, tarkistaa arvaukset ja päivittää yhden arvauksen tietoja. 
* Käyttöliittymän puolella aloitusikkuna antaa pelaajan valita mitä pelimoodeja pelaaja haluaa pelata.
* Gui-luokka on vastuussa pelin visuaalisesta puolesta eli se näyttää ja päivittää peli-ikkunan.
* Lopetusikkuna ilmoittaa pelin loputtua, kuinka paljon pisteitä pelaaja keräsi ja kuinka monta maata hän arvasi
* Yksityiskohtaisempia asioita: ajastin ja sen värin vaihtuminen, skip-nappi, vihjeboksi, listat (jotka luokittelee maat yritysten perusteella), 
* virheilmoitus olemassaolemattomasta maasta (eli tod näk typosta), kehityspalkki ja sen värit, pisteboksi ja sen värit

## Ohjelman rakenne selkokielellä
* maiden_tiedot_parser.py lukee datan useammasta JSON-tiedostosta ja tallentaa näistä jokaisen maan datan 
* main.py käynnistää pelin
* peli.py hoitaa pelin sisäisen logiikan. 
* gui_aloitusikkuna.py näyttää aloitusikkunan, jossa pelaaja valitsee pelimoodit
* gui.py (sekä gui_vasen_puoli.py ja gui_oikea_puoli.py) hoitaa peli-ikkunan näkymän
* gui_lopetusikkuna näyttää lopetusikkunan, jossa näkyy pisteet ja arvatuiden maiden määrän
* testi-kansiossa testimoduulit varmistavat parserin, maa-olion ja peli-olion oikean toiminnan

## Käyttöohje
* Pelin toiminta vaatii Python 3:sta ja sinulla pitää olla ladattuna PyQt6. Ks. Pyqt6 asennus: https://pypi.org/project/PyQt6/
* Karttapeliä voi pelata hyvin yksinkertaisesti. Sinun pitää ladata zip-tiedosto, joka sisältää kaikki peliin tarvittavat tiedostot.
* Sieltä sinun pitää avata main.py ja ajaa tämä moduuli, mikä käynnistää pelin. 

## Pelin säännöt
* Pelaaja saa arvata, mitä pelimoodeja hän haluaa pelata. Voit valita maanosan, jossa pelaat; haluatko pelata karttakuvilla vai lipuilla ja vaikeustason, joka muuttaa ajastimen pituutta.
* Pelin alettua pelaajan on arvattava maata. Jos pelaaja arvaa maan ensimmäisellä yrityksellä, hän saa 120p. Toisella 100p, kolmannella 80p, neljännellä 60, viidennellä 40 ja kuudennella 20. 
* Jos pelaaja ei saa arvattua maata niin hän saa siitä 0p. Jos pelaaja päättää skipata maan niin hänen pisteistään vähennetään jokasita skippausta kohti -10p.
* Peli loppuu, kun aika loppuu tai kun pelaaja on saanut arvattua kaikki maat. 

## Aikataulu
* Käytin pelin tekemiseen varmaankin n. 85 - 90 h
* Suunnitelmaan tuli pieniä muutoksia, koska en aluksi osannut ajatella, että minun pitäisi alussa kirjoittaa parseri, mikä vei melko kauan aikaa tehdä. 
* Tenttien takia käyttöliittymän tekeminen on jäi hetkellisesti sivuun.
* En osannut odottaa, että käyttöliittymän kirjoittamisessa ja visuaaliseen estetiikkaan menisi näin paljon aikaa. 
* Minulla meni käyttöliittymän kirjoittamiseen ja muokkaamiseen varmaankin lähelle 45 - 50 h.
* Olin suunnitellut, että palautan projektin viikkoa ennen DL, mutta palauttaminen siirtyi selkeästi (hyvin lähelle DL) käyttöliittymän takia. 

# Puutteet
* Peli-ikkunan näkymässä Itävallan karttakuva skaalautuu, jostain syystä todella hassusti ja vie huomattavasti enemmän ikkunan tilaa kuin muut maat. Tällöin näkymä on melko kökkö ja huono. 
* Peli-ikkuna on asetettu tietynsuuruiseksi eikä sen kokoa voi muuttaa. Ikkuna ei siis välttämättä näytä kaikilla monitoreilla samalta.
* Peli ei sisällä kaikkia maailman maita: Oseanian kolmella saarimaalla (Marshall Island, Micronesia ja Tuvalu) ei ollut karttakuvaa, joten päätin poistaa ne täysin pelistä poistamalla kaikki niiden tiedot JSON-tiedostoista.
* Jotkut Afrikan maat aiheuttavat vihjebokissa sellaisen tilanteen, että perustiedoissa lukevat naapurimaiden nimet ovat liian pitkiä mahtuakseen boksiin jolloin boksi suurentuu ja ikkunan asetelma muuttuu. Usein tämä johtuu nimestä pitkästä nimestä: Democratic Republic of the Congo
* Joidenkin maiden nimet ovat hassuja esim Vatican City on "Holy See (Vatican City State)" jolloin oikeankirjoituksen takia sitä on hyvin vaikeaa arvata oikein. 
* Pelissä "pelaajat voivat klikata maita ja sitten ohjelma kertoo perustiedot maasta" ei varsinaisesti toteudu vaan perustiedot näytetään vain silloin kun pelaaja on tehnyt siitä maasta arvauksen. Maata ei voi siis klikata. Tämä on korvattu sillä, että pelissä on useampi oma ominaisuus kuten: virheilmoitus typosta, selkeä näkymä, pistesysteemi, listat arvatuista maista, skip nappi ja todella suurella määrällä yksikkötestejä