
class Maa:
    def __init__(self, name, iso3166, capital, population, area, languages, independence_day, neighbouring_countries ,hints):
        self.name = name
        self.iso3166 = iso3166
        self.capital = capital
        self.population = population
        self.area = area
        self.languages = languages #tämä on lista, joka sisältää kaikki maan viralliset kielet
        self.independence_day = independence_day
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
        return self.independence_day

    def get_hints(self):
        return self.hints

    def get_neighbouring_countries(self):
        return self.neighbouring_countries

    def get_flag_png(self):
        pass       #en tiedä vielä miten tämä tehdään.

    # Tarkistaa onko pelaajan arvaus oikein. Jos arvaus on oikein, niin palautetaan True ja jos ei ole oikein niin False.
    def is_the_guess_right(self, guess):
        arvaus = guess.rstrip() #poistetaan mahdolliset välilyönnit
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
            if 0 <= nth_guess <= 5:
                hint = self.hints[nth_guess - 1]
                return hint
            else:
                return None


    def __str__(self):
        country_info = (f"The country is {self.name}. Its ISO-3166 code is {self.iso3166}.\n"
                        f"{self.name}'s capital is {self.capital} and its population is {self.population}.\n"
                        f"The area of {self.name} is {self.area}, the official languages are {self.languages}\n"
                        f"and the country's independence day is on {self.independence_day}.\n"
                        f"The neighbouring countries of {self.name} are {self.neighbouring_countries}.")

        return country_info

