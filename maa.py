from maiden_tiedot_parser import kaikkien_maiden_data

class Maa:
    def __init__(self, name, iso3166, continent, capital, population, area, languages, independence_year, neighbouring_countries ,hints):
        self.name = name
        self.iso3166 = iso3166
        self.continent = continent
        self.capital = capital
        self.population = population
        self.area = area
        self.languages = languages #tämä on lista, joka sisältää kaikki maan viralliset kielet
        self.independence_year = independence_year
        self.neighbouring_countries = neighbouring_countries #tämäkin on lista, joka sisältää kaikki naapurimaat
        self.hints = hints #tämäkin on lista, joka sisältää kaikki vihjeet tietyssä järjestyksessä

    def get_name(self):
        return self.name

    def get_iso3166(self):
        return self.iso3166

    def get_capital(self):
        return self.capital

    def get_population(self):
        return self.population

    def get_area(self):
        return self.area

    def get_languages(self):
        return self.languages

    def get_independence_day(self):
        return self.independence_year

    def get_hints(self):
        return self.hints

    def get_neighbouring_countries(self):
        return self.neighbouring_countries

    def get_flag_png(self):
        pass       #en tiedä vielä miten tämä tehdään.

    # Tarkistaa onko pelaajan arvaus oikein. Jos arvaus on oikein, niin palautetaan True ja jos ei ole oikein niin False.
    def is_the_guess_right(self, guess):
        arvaus = guess.rstrip()
        if arvaus.upper() == self.name.upper():
            return True
        else:
            return False

    # Palauttaa oikean vinkin sen perusteella montako arvausta pelaaja on tehnyt.
    # Parametriksi annetaan siis kokonaisluku, joka kertoo, kuinka monta arvausta pelaaja on jo tehnyt.
    def give_hint(self, nth_guess):
        if nth_guess == 0:
            return None
        else:
            if 0 < nth_guess <= 5:
                hint = self.hints[nth_guess - 1]
                return hint
            else:
                return None


    def __str__(self):
        country_info = (f"The country is {self.name}. Its ISO-3166 code is {self.iso3166}.\n"
                        f"{self.name}'s capital is {self.capital} and its population is {self.population} people.\n"
                        f"The area of {self.name} is {self.area} km^2. The languages spoken in {self.name} "
                        f"are {self.languages}. The country's independence year is {self.independence_year}.\n"
                        f"The neighbouring countries of {self.name} are {self.neighbouring_countries}.")

        return country_info


#luodaan kaikki Maa-oliot maiden_tiedot_parser.py moduulissa olevan kaikkien_maiden_data -metodin avulla
maiden_tiedot = kaikkien_maiden_data()

def luodaan_maa_oliot(maiden_tiedot):
    lista_maa_olioista = []

    for maa in maiden_tiedot: #tässä maa on siis sanakirjassa yksi maa (tai tarkalleen maan nimi) eli tässä käydään kaikki sanakirjan avaimet läpi.
        nimi = maa #esim ensimmäinen maa sanakirjassa on "Afghanistan"
        iso3166 = maiden_tiedot[maa].get("abbreviation") #lähde: "Python Dictionary get() Method", W3schools, https://www.w3schools.com/python/ref_dictionary_get.asp
        maanosa = maiden_tiedot[maa].get("continent")
        paakaupunki = maiden_tiedot[maa].get("city")
        populaatio = maiden_tiedot[maa].get("population")
        pinta_ala = maiden_tiedot[maa].get("area")
        kielet = maiden_tiedot[maa].get("languages")
        itsenaisyysvuosi = maiden_tiedot[maa].get("independence")
        naapurimaat = maiden_tiedot[maa].get("neighbouring countries")
        vinkit = [maanosa, paakaupunki, kielet, naapurimaat, iso3166]

        uusi_maa_olio = Maa(nimi, iso3166, maanosa, paakaupunki, populaatio, pinta_ala,
                            kielet, itsenaisyysvuosi, naapurimaat, vinkit)
        #lisätään listaan
        lista_maa_olioista.append(uusi_maa_olio)

    return lista_maa_olioista




