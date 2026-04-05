from peli import Peli
from maa import Maa

import unittest

class TestPeli(unittest.TestCase):

    def setUp(self): #lähde https://realpython.com/python-unittest/
        # Luodaan jokin testiolio, olkoot suomi (tiedot karkeita ja kirjoitettu vain testejä varten)
        # Kopioin tämän testi_maa moduulista. Tässä setup:issa luona yhden maan peliä varten ja tässä se on taas Suomi
        # Luon pelin, jossa lista_maa_oliot -paremetri saa lista, jossa on vain yksi maa eli siis Suomen.
        # Näin saan testattua metodeja Peli-luokan sisällä

        self.testiolio_peli = Maa(
            nimi = "Finland",
            iso3166 = "FI",
            maanosa = "Eurooppa",
            paakaupunki = "Helsinki",
            populaatio = 5500000,
            pinta_ala = 338000,
            kielet = ["Finnish", "Swedish"],
            itsenaisyysvuosi = "6.12.1917",
            naapurimaat = ["Norway", "Sweden", "Russia"],
            vihjeet = ["Europe", "Helsinki", "kielet", "naapurit", "F"])

        lista_maista_jossa_vain_suomi = [self.testiolio_peli]

        self.testipeli = Peli(lista_maista_jossa_vain_suomi)


    def test_maanosa_jossa_pelataan_euroopalla(self):
        # kokeillaan saadaanko Suomi, kun parametrina on Eurooppa
        maanosa = self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        lista = self.testipeli.arvattavat_maat
        self.assertEqual(lista, [self.testiolio_peli], "Metodi maanosa_jossa_pelataan ei toimi oikein.")

    def test_maanosa_jossa_pelataan_aasialla(self):
        # kokeillaan saadaanko tyhjä lista, kun parametrina on Aasia
        maanosa = self.testipeli.maanosa_jossa_pelataan("Asia")
        lista = self.testipeli.arvattavat_maat
        self.assertEqual(lista, [], "Metodi maanosa_jossa_pelataan ei toimi oikein.")

    def test_arvotaan_maa(self):
        # kokeillaan toimiiko metodi arvotaan_maa oikein
        self.testipeli.maanosa_jossa_pelataan("Eurooppa") #tämä tehtävä, jotta self.arvattavat_maat -listalla olisi jokin alkio
        testi = self.testipeli.arvotaan_maa()
        self.assertEqual(testi, True, "Metodi arvotaan_maa ei toimi oikein.")

    def test_tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot_oikea_arvaus(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa() #tämä tehtävä, jotta self.nykyine_maa -attribuutti olisi jokin oikea Maa-olio
        arvaus = self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland")
        self.assertEqual(arvaus, True, "Metodi tarkistetaan_arvaus ei toimi oikein (tapaus: oikea arvaus).")

    def test_tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot_vaara_arvaus(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        arvaus = self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.assertEqual(arvaus, False, "Metodi tarkistetaan_arvaus ei toimi oikein (tapaus: väärä arvaus).")

    def test_tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot_kuusi_arvausta(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        arvaus = self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.assertEqual(arvaus, None, "Metodi tarkistetaan_arvaus ei toimi oikein (tapaus: kuusi arvausta.")

    def test_tarkistetaan_tamanhetkisen_maan_arvausyritykset_yhdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland") #yksi ja ainoa arvaus
        arvausten_maara = self.testipeli.tamanhetkisen_maan_arvausyritykset
        self.assertEqual(arvausten_maara, 1, "Tämänhetkisen maan arvausyritysten laskeminen ei toimi oikein")

    def test_tarkistetaan_tamanhetkisen_maan_arvausyritykset_kahdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden") #eka arvaus
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland") #toinen arvaus eli arvauksia pitäisi olla kaksi
        arvausten_maara = self.testipeli.tamanhetkisen_maan_arvausyritykset
        self.assertEqual(arvausten_maara, 2, "Tämänhetkisen maan arvausyritysten laskeminen ei toimi oikein")

    def test_tarkistetaan_arvausten_maarat_sanakirja_yhdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland") # yksi ja ainoa arvaus
        arvausten_maarat = self.testipeli.arvausten_maarat
        self.assertEqual(arvausten_maarat, {"Finland" : 1}, "Metodi tarkistetaan_arvaus ei toimi oikein. (tapaus: arvauksia on tehty 2)")

    def test_tarkistetaan_arvausten_maarat_sanakirja_kahdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden") #eka arvaus
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland") #toinen arvaus eli arvauksia pitäisi olla kaksi
        arvausten_maarat = self.testipeli.arvausten_maarat
        self.assertEqual(arvausten_maarat, {"Finland" : 2}, "Metodi tarkistetaan_arvaus ei toimi oikein (tapaus: arvauksia on tehty 2).")

    def test_tarkistetaan_kokonaispisteet_yhdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland") # yksi ja ainoa arvaus
        pisteiden_maara = self.testipeli.kokonaispisteet
        self.assertEqual(pisteiden_maara, 100, "Kokonaispisteiden lasku ei toimi oikein (tapaus: yksi arvaus).")

    def test_tarkistetaan_kokonaispisteet_kahdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden") #eka arvaus
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland") # yksi ja ainoa arvaus
        pisteiden_maara = self.testipeli.kokonaispisteet
        self.assertEqual(pisteiden_maara, 80, "Kokonaispisteiden lasku ei toimi oikein (tapaus: yksi arvaus).")

    def test_haetaan_vihje_kahdella_arvauksella(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        vihje = self.testipeli.haetaan_vihje()
        self.assertEqual(vihje, "Europe", "Vihjeiden haku ei toimi oikein (tapaus: maata on arvattu kerran väärin).")

    def test_haetaan_vihje_kun_arvaus_on_jo_oikein(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("sweden")
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland")
        vihje = self.testipeli.haetaan_vihje()
        self.assertEqual(vihje, None, "Vihjeiden haku ei toimi oikein (tapaus: maa on arvattu jo oikein).")

    def test_peli_loppui_maita_ei_ole_enaa_arvattavana(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot("Finland")
        pelin_tila = self.testipeli.peli_loppui()
        self.assertEqual(pelin_tila, True, "Metodi peli_loppui ei toimi oikein (tapaus: maita ei ole enää arvattavana)")

    def test_peli_loppui_maita_on_arvattavana(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        pelin_tila = self.testipeli.peli_loppui()
        self.assertEqual(pelin_tila, False, "Metodi peli_loppui ei toimi oikein (tapaus: maita on arvattavana)")

    def test_peli_loppui_asettamalla_aika_loppuneeksi(self):
        self.testipeli.maanosa_jossa_pelataan("Eurooppa")
        self.testipeli.arvotaan_maa()
        self.testipeli.asetetaan_aika_loppuneeksi()
        pelin_tila = self.testipeli.peli_loppui()
        self.assertEqual(pelin_tila, True, "Metodi peli_loppui ei toimi oikein (tapaus: aika asetettu loppuneeksi)")


    # Metodeja hae_maan_perustiedot ja hae_maan_lippu ei tarvitse testata, koska ne on testattu jo testi_maa -moduulissa




