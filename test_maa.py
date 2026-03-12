from maa import Maa

import unittest

class TestMaa(unittest.TestCase): #perintä kopioitu kierrokselta 6 t. 5

    def setUp(self): #lähde https://realpython.com/python-unittest/
        # luodaan jokin testiolio, olkoot suomi (tiedot karkeita ja kirjoitettu vain testejä varten)
        self.testiolio = Maa(
            name = "Finland",
            iso3166 = "FI",
            capital = "Helsinki",
            population = 5500000,
            area = 338000,
            languages = ["Finnish", "Swedish"],
            independence_day = "6.12.1917",
            neighbouring_countries = ["Norway", "Sweden", "Russia"],
            hints = ["Europe", "Helsinki", "kielet", "naapurit", "F"]
        )

    def test_is_the_guess_right_toimii_pienilla_kirjaimilla(self):
        # kokeillaan arvata pienellä tekstillä ja välilyönnillä
        kokeilu = self.testiolio.is_the_guess_right("finland ")
        self.assertEqual(kokeilu, True, "Metodi is_the_guess_right ei toimi oikein (tapaus: oikea arvaus)") #tämä toimii ainakin toistaiseksi

    def test_is_the_guess_right_vaara_arvaus(self):
        # kokeillaan arvata väärää maata
        vaara_vastaus = self.testiolio.is_the_guess_right("sweden")
        self.assertEqual(vaara_vastaus, False, "Metodi is_the_guess_right ei toimi oikein (tapaus: väärä arvaus)") #tämä toimii ainakin toistaiseksi

    def test_give_hint(self):
        # kokeillaan, että palauttaako metodi give_hint oikean vihjeen
        # valitaan esim siten, että pelaaja on arvannut yhden kerran väärin eli vihje pitäisi olla "Europe
        vihje = self.testiolio.give_hint(1)
        self.assertEqual(vihje, "Europe", "Metodi give_hint ei toimi oikein (tapaus: pos kokonaisluku)") #tämä toimii ainakin toistaiseksi

    def test_give_hint_parametrina_0(self):
        # kokeillaan, että palauttaako metodi give_hint None, kun sille annetaan parametriksi 0
        vihje = self.testiolio.give_hint(0)
        self.assertEqual(vihje, None, "Metodi give_hint ei toimi oikein (tapaus: nth_guess = 0)") #tämä toimii ainakin toistaiseksi

    def test_give_hint_parametrina_negatiivinen_luku(self):
        # kokeillaan, että palauttaako metodi give_hint None, kun sille annetaan parametriksi negatiivinen luku
        vihje = self.testiolio.give_hint(-1)
        self.assertEqual(vihje, None, "Metodi give_hint ei toimi oikein (tapaus: negatiivinen parametri)") #tämä toimii ainakin toistaiseksi

    def test_give_hint_parametrina_luku_suurempi_kuin_5(self):
        # kokeillaan, että palauttaako metodi give_hint None, kun sille annetaan parametriksi luku yli viiden
        vihje = self.testiolio.give_hint(6)
        self.assertEqual(vihje, None, "Metodi give_hint ei toimi oikein (tapaus: kokonaisluku yli 5)") #tämä toimii ainakin toistaiseksi

