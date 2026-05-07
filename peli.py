import random
from maa import Maa
from maiden_tiedot_parser import kaikkien_maiden_data,  luodaan_maa_oliot

class Peli:
    #luodaan ensin kaikki Maa-oliot, jotta Peli-luokka voi hyödyntää maita.
    maiden_data = kaikkien_maiden_data()
    lista_maa_oliot = luodaan_maa_oliot(maiden_data)

    def __init__(self, lista_maa_oliot):
        self.kaikki_maat = lista_maa_oliot #tämä pysyy muuttumattomana eli tässä listassa on aina kaikki maa-oliot
        self.arvattavat_maat = [] #lista, josta valitaan umpimähkään jokin maa. listan alkiot on Maa-olioita
        self.arvausten_maarat = {} #sanakirjassa on avaimena maan nimi ja arvona siihen maahan käytetyt arvauskerrat
        self.kokonaispisteet = 0
        self.tamanhetkisen_maan_arvausyritykset = 0
        self.tamanhetkisen_arvauksen_pisteet = 120
        self.pelitila = None # tämä on joko Karttamoodi tai lippumoodi riippuen pelaajan valinnasta.
        self.nykyinen_maa = None #Maa-olio
        self.arvauksen_tila = False #False edustaa väärää arvausta eli sitä että maata ei ole vielä arvattu ja True että maa on arvattu
        self.aika_loppunut = False #False edustaa sitä, että aikaa on vielä jäljellä
        self.lista_kaikkien_maiden_nimista = [] # käyttöliittymää varten
        self.lista_kaikkien_maiden_iso3166 = [] # käyttöliittymää varten
        self.listataan_kaikki_maiden_nimet_ja_iso()


    def maanosa_jossa_pelataan(self, continent):
        """Suodattaa halutut maat listaan ja palauttaa tämän listan. Tästä listasta voidaan sitten arpoa pelaajalle umpimähkään jokin maa arvattavaksi."""
        maanosan_maat = []

        continent = continent.lower()

        if continent == "world": #jos continent parametri on world niin peliin tulee mukaan kaikki maat
            self.arvattavat_maat = self.kaikki_maat.copy() #luodaan kaikki_maat -listasta kopio,
                                                                # jotta ei viitata samaan listaan
        else:
            for maa_olio in self.kaikki_maat:
                maanosa = maa_olio.hae_maanosa()
                if maanosa.lower() == continent:
                    maanosan_maat.append(maa_olio)

            self.arvattavat_maat = maanosan_maat #tehdään arvattavista maista kyseisen maanosan maat


    def arvotaan_maa(self):
        """Arpoo yhden maan ja palauttaa oletustiedot yhdelle arvaukselle"""
        if len(self.arvattavat_maat) > 0:
            arvottu_maa = random.choice(self.arvattavat_maat)
            self.nykyinen_maa = arvottu_maa #nyt nykyinen maa on jokin Maa-olioda
            self.arvattavat_maat.remove(arvottu_maa) #poistetaan listalta, jotta sitä ei arvota myöhemmin uudestaan

            # sen jälkeen kun maa on arvottu niin varmistetaan, ettei juuri arvotulle maalle jää edellisen maan tietoja:
            self.tamanhetkisen_maan_arvausyritykset = 0 #nollataan maan yritykset, jotta meille ei jää edellisen arvauksen yritykset voimaan
            self.tamanhetkisen_arvauksen_pisteet = 120 #palautetaan default pisteet, jotta meille ei jää edellisen arvauksen pisteet voimaan
            self.arvauksen_tila = False #nollataan arvauksen tila, jotta seuraava arvaus ei ole vahingossa jo valmiiksi oikein
            return True # palautetaan True, eli maan arpominen tapahtui

        else:
            return False # palautetaan False, eli arpominen ei tapahtunut, eli pelaaja on arvannut kaikki maat


    def tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot(self, arvaus):
        """ Tämä tarkistaa yhden arvausyrityksen ja huolehtii pisteiden lisäämisestä kokonaispisteisiin"""
        if self.tamanhetkisen_maan_arvausyritykset <= 5 and self.arvauksen_tila == False: # jos pelaaja ei ole arvannut vielä kuusi kertaa eikä ole arvannut oikein:
            if not self.nykyinen_maa.onko_arvaus_oikein(arvaus): # Jos arvaus meni väärin
                self.tamanhetkisen_arvauksen_pisteet -= 20 #, vähennetään 20p default pisteistä
                self.tamanhetkisen_maan_arvausyritykset += 1 #, lisätään arvausyritysten määrään yksi arvaus

                if self.tamanhetkisen_maan_arvausyritykset == 6: # jos arvauksia on nyt kuusi eli jos tuon ylemmän += 1 jälkeen arvaus oli viimeinen, niin tallennetaan arvausten määrä sanakirjaan lukuna 0
                    self.arvausten_maarat[self.nykyinen_maa.hae_nimi()] = 0
                    return None

                return False # palautetaan False eli arvaus meni väärin

            else: # Jos arvaus meni oikein,
                self.tamanhetkisen_maan_arvausyritykset += 1
                self.kokonaispisteet += self.tamanhetkisen_arvauksen_pisteet # niin lisätään kokonaispisteisiin ansaitut pisteet
                self.arvauksen_tila = True
                self.arvausten_maarat[self.nykyinen_maa.hae_nimi()] = self.tamanhetkisen_maan_arvausyritykset # , merkitään sanakirjaan, kuinka monta arvausta maan arvaamiseen meni

                return True # palautetaan True eli arvaus meni oikein

        return None # jos pelaaja on tehnyt jo 5 arvausta tai saanut arvauksen oikein


    def haetaan_vihje(self):
        """Antaa maata vastaavan vihjeen sen perusteella, montako arvausta pelaaja on tehnyt tätä maata kohden"""
        if not self.arvauksen_tila and self.tamanhetkisen_maan_arvausyritykset <= 5: #eli jos arvaus on tällä hetkellä väärin eikä hän ole arvannut vielä viisi kertaa
            arvausyritysten_maara = self.tamanhetkisen_maan_arvausyritykset
            vihje = self.nykyinen_maa.hae_vihje(arvausyritysten_maara) #Maa-luokan metodi hae_vihje palauttaa oikean vihjeen
            return vihje
        else: # eli on arvannut jo viisi kertaa
            return None

    def hae_maan_perustiedot(self):
        maan_perustiedot = self.nykyinen_maa.hae_perustiedot()
        return maan_perustiedot


    def hae_maan_iso3166(self):
        maan_iso3166 = self.nykyinen_maa.hae_iso()
        return maan_iso3166


    def hae_maan_lippu(self):
        maan_lippu = self.nykyinen_maa.hae_lippu_png()
        return maan_lippu

    def asetetaan_aika_loppuneeksi(self):
        """Asettaa ajan loppuneeksi kun tätä kutsutaan. """
        self.aika_loppunut = True

    def listataan_kaikki_maiden_nimet_ja_iso(self):
        for maa_olio in self.kaikki_maat:
            maan_nimi = maa_olio.nimi.lower()
            maan_iso3166 = maa_olio.iso3166.lower()

            self.lista_kaikkien_maiden_nimista.append(maan_nimi)
            self.lista_kaikkien_maiden_iso3166.append(maan_iso3166)

    def maa_skipattu(self):
        """Asettaa maan arvausyritykset kuuteen, jotta skipattu maa menisi Failed to guess -listaan"""
        self.tamanhetkisen_maan_arvausyritykset = 6
        self.arvausten_maarat[self.nykyinen_maa.hae_nimi()] = 6

        # skippaus vähentää 10p pisteistä niin vähennetään se kokonaispisteistä
        self.kokonaispisteet -= 10


    def peli_loppui(self):
        if self.aika_loppunut: # jos pelin aika loppui niin palautetaan True
            return True # peli loppui
        else:
            return False # peli jatkuu

