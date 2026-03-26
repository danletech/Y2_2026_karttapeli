import random, math
from maa import Maa, luodaan_maa_oliot
from maiden_tiedot_parser import kaikkien_maiden_data

#luodaan ensin kaikki Maa-oliot, jotta Peli-luokka voi hyödyntää maita.
maiden_data = kaikkien_maiden_data()
lista_maa_oliot = luodaan_maa_oliot(maiden_data)

class Peli:
    def __init__(self, lista_maa_oliot):
        self.kaikki_maat = lista_maa_oliot #tämä pysyy muuttumattomana eli tässä listassa on aina KAIKKI maa-oliot
        self.arvattavat_maat = [] #tämä on se lista, josta valitaan randomisti maa
        self.arvausten_maara = {} #sanakirjassa on avaimena maan nimi ja arvona siihen maahan käytetyt arvauskerrat
        self.pisteet = 0
        self.tamanhetkisen_maan_arvausyritykset = 0
        self.nykyinen_maa = None

    def maanosa_jossa_pelataan(self, continent):
        maanosan_maat = []
        if continent == "world": #jos continent parametri on world niin peliin tulee mukaan kaikki maat
            self.arvattavat_maat = self.kaikki_maat.copy() #luodaan kaikki_maat -listasta kopio,
                                                                # jotta ei sitten viitata samaan listaan
        else:
            for maa_olio in self.kaikki_maat:
                maanosa = maa_olio.continent
                if maanosa == continent:
                    maanosan_maat.append(maa_olio)

            self.arvattavat_maat = maanosan_maat #tehdään arvattavista maista kyseisen maanosan kaikki maat


    def arvotaan_maa(self):
        if len(self.arvattavat_maat) > 0:
            arvottu_maa = random.choice(self.arvattavat_maat)
            self.nykyinen_maa = arvottu_maa
            self.arvattavat_maat.remove(arvottu_maa) #poistetaan listalta, jotta sitä ei arvota myöhemmin uudestaan

        else:
            print("Ei enää arvattavia maita.") # jos lista on tyhjä niin silloin pelaaja on arvannut kaikki maat




