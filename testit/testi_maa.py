from maa import Maa

import unittest

class TestiMaa(unittest.TestCase): #perintä kopioitu kierrokselta 6 t. 5

    def setUp(self): #lähde https://realpython.com/python-unittest/
        # Luodaan jokin testiolio, olkoot suomi (tiedot karkeita ja kirjoitettu vain testejä varten)
        self.testiolio = Maa(
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


    def test_onko_arvaus_oikein_toimii_pienilla_kirjaimilla(self):
        # kokeillaan arvata pienellä tekstillä ja välilyönnillä
        kokeilu = self.testiolio.onko_arvaus_oikein("finland ")
        self.assertEqual(kokeilu, True, "Metodi onko_arvaus_oikein ei toimi oikein (tapaus: oikea arvaus)") #tämä toimii ainakin toistaiseksi

    def test_onko_arvaus_oikein_vaara_arvaus(self):
        # kokeillaan arvata väärää maata
        vaara_vastaus = self.testiolio.onko_arvaus_oikein("sweden")
        self.assertEqual(vaara_vastaus, False, "Metodi onko_arvaus_oikein ei toimi oikein (tapaus: väärä arvaus)") #tämä toimii ainakin toistaiseksi

    def test_hae_vihje(self):
        # kokeillaan, että palauttaako metodi hae_vihje oikean vihjeen
        # valitaan esim siten, että pelaaja on arvannut yhden kerran väärin eli vihje pitäisi olla "Europe
        vihje = self.testiolio.hae_vihje(1)
        self.assertEqual(vihje, "Europe", "Metodi hae_vihje ei toimi oikein (tapaus: pos kokonaisluku)") #tämä toimii ainakin toistaiseksi

    def test_hae_vihje_parametrina_0(self):
        # kokeillaan, että palauttaako metodi hae_vihje None, kun sille annetaan parametriksi 0
        vihje = self.testiolio.hae_vihje(0)
        self.assertEqual(vihje, None, "Metodi hae_vihje ei toimi oikein (tapaus: nth_guess = 0)") #tämä toimii ainakin toistaiseksi

    def test_hae_vihje_parametrina_negatiivinen_luku(self):
        # kokeillaan, että palauttaako metodi hae_vihje None, kun sille annetaan parametriksi negatiivinen luku
        vihje = self.testiolio.hae_vihje(-1)
        self.assertEqual(vihje, None, "Metodi hae_vihje ei toimi oikein (tapaus: negatiivinen parametri)") #tämä toimii ainakin toistaiseksi

    def test_hae_vihje_parametrina_luku_suurempi_kuin_5(self):
        # kokeillaan, että palauttaako metodi hae_vihje None, kun sille annetaan parametriksi luku yli viiden
        vihje = self.testiolio.hae_vihje(6)
        self.assertEqual(vihje, None, "Metodi hae_vihje ei toimi oikein (tapaus: kokonaisluku yli 5)") #tämä toimii ainakin toistaiseksi
    
    def test_hae_maan_kuvan_tiedoston_polku(self):
        # kokeillaan, että palauttaako metodi hae_maan_kuvan_tiedoston_polku maiden kuvat/all/fi/512.png
        polku = self.testiolio.hae_maan_kuvan_tiedoston_polku()
        self.assertEqual(polku, "maiden kuvat/all/fi/512.png","Metodi hae_maan_kuvan_tiedoston_polku ei toimi oikein")

    def test_hae_maan_lipun_tiedoston_polku(self):
        # kokeillaan, että palauttaako metodi hae_maan_lipun_tiedoston_polku maiden liput/fi.png
        polku = self.testiolio.hae_maan_lipun_tiedoston_polku()
        self.assertEqual(polku, "maiden liput/fi.png","Metodi hae_maan_lipun_tiedoston_polku ei toimi oikein")

    def test_hae_perustiedot(self):
        # kokeillaan, että palauttaako metodi hae_perustiedot oikeat tiedot
        tiedot = self.testiolio.hae_perustiedot()
        testiolion_tiedot = {
            'nimi': 'Finland',
            'iso3166': 'FI',
            'maanosa': 'Eurooppa',
            'paakaupunki': 'Helsinki',
            'populaatio': 5500000,
            'pinta_ala': 338000,
            'kielet': ['Finnish', 'Swedish'],
            'itsenaisyysvuosi': '6.12.1917',
            'naapurimaat': ['Norway', 'Sweden', 'Russia']
        }
        self.assertEqual(tiedot, testiolion_tiedot, "Metodi hae_perustiedot ei toimi oikein")
