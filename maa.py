
class Maa:
    def __init__(self, nimi, iso3166, maanosa, paakaupunki, populaatio, pinta_ala, kielet, itsenaisyysvuosi, naapurimaat, vihjeet):
        self.nimi = nimi
        self.iso3166 = iso3166
        self.maanosa = maanosa
        self.paakaupunki = paakaupunki
        self.populaatio = populaatio
        self.pinta_ala = pinta_ala
        self.kielet = kielet #tämä on lista, joka sisältää kaikki maan viralliset kielet
        self.itsenaisyysvuosi = itsenaisyysvuosi
        self.naapurimaat = naapurimaat #tämäkin on lista, joka sisältää kaikki naapurimaat
        self.vihjeet = vihjeet #tämäkin on lista, joka sisältää kaikki vihjeet tietyssä järjestyksessä

    def hae_nimi(self):
        return self.nimi

    def hae_iso(self):
        return self.iso3166

    def hae_paakaupunki(self):
        return self.paakaupunki

    def hae_populaatio(self):
        return self.populaatio

    def hae_pinta_ala(self):
        return self.pinta_ala

    def hae_kielet(self):
        return self.kielet

    def hae_itsenaisyyspaiva(self):
        return self.itsenaisyysvuosi

    def hae_vihjeet(self):
        return self.vihjeet

    def hae_naapurimaat(self):
        return self.naapurimaat

    def hae_lippu_png(self):
        pass       #en tiedä vielä miten tämä tehdään.


    def onko_arvaus_oikein(self, guess):
        """Tarkistaa onko pelaajan arvaus oikein. Jos arvaus on oikein, niin palautetaan True ja jos ei ole oikein niin False.
        Parametrina on pelaajan arvaus tekstinä"""
        arvaus = guess.rstrip()
        if arvaus.upper() == self.nimi.upper() or arvaus.upper() == self.iso3166.upper():
            return True
        else:
            return False


    def hae_vihje(self, nth_guess):
        """Palauttaa oikean vinkin sen perusteella montako arvausta pelaaja on tehnyt.
        Parametriksi annetaan kokonaisluku, joka kertoo, kuinka monta arvausta pelaaja on jo tehnyt."""
        if nth_guess == 0:
            return None
        else:
            if 0 < nth_guess <= 5:
                hint = self.vihjeet[nth_guess - 1]
                return hint
            else:
                return None


    def hae_perustiedot(self):
        """ Hakee maan perustiedot, mutta jättää vihjeet pois, koska niitä on turha näyttää pelaajalle enää lopuksi."""
        sanakirja_maan_perustiedoista = self.__dict__.copy() #  lähde: "Can I get all attributes that were defined in the __init__ method of a class? [duplicate]", Stackoverflow, https://stackoverflow.com/questions/68384788/can-i-get-all-attributes-that-were-defined-in-the-init-method-of-a-class
        sanakirja_maan_perustiedoista.pop("vihjeet") # poistetaan vihjeet #lähde: "Python Removing Items from a Dictionary", https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
        return sanakirja_maan_perustiedoista


    def __str__(self):
        tiedot_maasta = (f"The country is {self.nimi}. Its ISO-3166 code is {self.iso3166}.\n"
                        f"{self.nimi}'s capital is {self.paakaupunki} and its population is {self.populaatio} people.\n"
                        f"The area of {self.nimi} is {self.pinta_ala} km^2. The languages spoken in {self.nimi} "
                        f"are {self.kielet}. The country's independence year is {self.itsenaisyysvuosi}.\n"
                        f"The neighbouring countries of {self.nimi} are {self.naapurimaat}.")

        return tiedot_maasta





