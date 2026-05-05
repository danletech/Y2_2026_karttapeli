import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class Vasen(QWidget):
    """Tässä luodaan ikkunan vasen puoli eli karttakuva/lippu, tekstieditoti, vihjeboksi ja perustiedoille boksi"""

    def __init__(self, peli_olio):
        super().__init__()

        self.peli = peli_olio

        self.kuva = QLabel() #label karttakuvaa/lippua varten

        # määritetään ikkunan oikean puolen asetelman tyyli
        self.vasen_asetelma = QVBoxLayout()

        # asetetaan luokalle tyyliksi tämä self.vasen_asetelma
        self.setLayout(self.vasen_asetelma)

        # vasen puoli ikkunaa
        self.vasen_asetelma.addSpacing(30) # lähde: "QBoxLayout Class", Qt Group, https://doc.qt.io/qt-6/qboxlayout.html
        self.vasen_asetelma.addWidget(self.kuva)
        self.vasen_asetelma.addStretch() # työnnetään asetelmat ylöspäin, lähde: How to attach a changing list of widgets to the top of the QVBoxLayout in PyQT6?, Stackoverflow, https://stackoverflow.com/questions/77291072/how-to-attach-a-changing-list-of-widgets-to-the-top-of-the-qvboxlayout-in-pyqt6

        # luodaan tekstikenttä johon pelaaja syötää arvauksensa
        self.tekstieditori = QLineEdit(self)
        self.tekstieditori.setAlignment(Qt.AlignmentFlag.AlignHCenter) # teksti lähtee keskeltä eikä vasemmalta
        self.tekstieditori.setFixedSize(300,30) # lähde: [Solved] How to change initial size of QLineEdit, Qt Forum, https://forum.qt.io/topic/37280/solved-how-to-change-initial-size-of-qlineedit/5

        # muokataan tekstieditorin ulkonäköä
        self.tekstieditori.setStyleSheet("""
            border-radius: 7px;
        """)

        # lisätään tekstieditori asetelmaan
        self.vasen_asetelma.addWidget(self.tekstieditori, alignment=Qt.AlignmentFlag.AlignHCenter) # lähde: "How do you change label alignment in PyQt6?", Stack Overflow, https://stackoverflow.com/questions/71756088/how-do-you-change-label-alignment-in-pyqt6

        # luodaan nappi, jolla siirrytään arvaamaan seuraavaa maata
        self.seuraava_maa_nappi = QPushButton("Next country")
        self.seuraava_maa_nappi.setFixedSize(300, 30)
        self.vasen_asetelma.addWidget(self.seuraava_maa_nappi, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.seuraava_maa_nappi.clicked.connect(self.siirrytaan_seuraavaan_maahan) # kun pelaaja painaa nappia niin pelissä siirrytään seuraavaan maahan
        self.seuraava_maa_nappi.hide() # ei näytetä nappia vielä (vasta sitten kun arvaus menee oikein tai maata ei saada arvattua ollenkaan)

        # luodaan varoitus siitä, että maata ei ole olemassa
        self.varoitus = QLabel("")
        self.varoitus.setStyleSheet("color: #ff2800") # lähde: "QLabel: set color of text and background", Stackoverflow, https://stackoverflow.com/questions/2749798/qlabel-set-color-of-text-and-background
        self.vasen_asetelma.addWidget(self.varoitus)

        # luodaan vihjelaatikko
        self.vihjelaatikko = QWidget()
        self.vihjelaatikko.setFixedHeight(270)

        # ja tehdään vihjelaatikosta hienompi
        self.vihjelaatikko.setStyleSheet("""
            background-color: grey;
            border: 4px solid #444444;
            border-radius: 7px;
            font-size: 16px;
            font-weight: bold;
        """)
        # lähde: "Styling the Widgets Application", Qt for Python, https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
        # ja "Qt Style Sheets Examples, Qt group", https://doc.qt.io/qt-6/stylesheet-examples.html
        # ja "Qt Style Sheets, Python tutorial", https://www.pythontutorial.net/pyqt/qt-style-sheets/

        self.vasen_asetelma.addWidget(self.vihjelaatikko) # lisätään vasemmalle puolelle QVboxlayouttia tuo vihjelaatikko

        # luodaan vihjelaatikon sisään asetelmaksi QVBoxlayout
        self.vihjelaatikon_sisapuoli = QVBoxLayout()

        # luodaan teksti, joka näytetään kun pelaaja ei ole vielä arvannut kertaakaan
        self.vihjelaatikon_teksti = QLabel("Guess the country!")
        self.vihjelaatikon_teksti.setAlignment(Qt.AlignmentFlag.AlignCenter) # asetetaan tämä teksti keskelle
        self.vihjelaatikon_teksti.setMinimumHeight(220) # annetaan korkeus jotta teksti osuisi laatikon keskelle
        self.vihjelaatikon_teksti.setStyleSheet("""
            border: 0px;
            font-size: 20px;
            """)

        # luodaan jokaiselle vihjeelle yksi oma laatikko:
        self.eka_vihje = QLabel("")
        self.toka_vihje = QLabel("")
        self.kolmas_vihje = QLabel("")
        self.neljas_vihje = QLabel("")
        self.viides_vihje = QLabel("")

        # määritellään vihjebokseille tietty koko
        self.eka_vihje.setFixedHeight(43)
        self.toka_vihje.setFixedHeight(43)
        self.kolmas_vihje.setFixedHeight(43)
        self.neljas_vihje.setFixedHeight(43)
        self.viides_vihje.setFixedHeight(43)

        # muutetaan vihjeboksien ulkonäköä
        self.eka_vihje.setStyleSheet("""
            color: #f5fefd;
            background-color: #48cae4;
            border-radius: 7px;
            border: 2px solid white;
            font-size: 18px;
        """)

        self.toka_vihje.setStyleSheet("""
            color: #f5fefd;
            background-color: #00b4d8;
            border-radius: 7px;
            border: 2px solid white;
            font-size: 18px;
        """)

        self.kolmas_vihje.setStyleSheet("""
            color: #f5fefd;
            background-color: #0096c7;
            border: 2px solid white;
            font-size: 18px;
        """)

        self.neljas_vihje.setStyleSheet("""
            color: #f5fefd;
            background-color: #023e8a;
            border: 2px solid white;
            font-size: 18px;
        """)

        self.viides_vihje.setStyleSheet("""
            color: #f5fefd;
            background-color: #03045e;
            border: 2px solid white;
            font-size: 18px;
        """)


        # laitetaan kaikki labelit asetteluun
        self.vihjelaatikon_sisapuoli.addWidget(self.vihjelaatikon_teksti)
        self.vihjelaatikon_sisapuoli.addWidget(self.eka_vihje)
        self.vihjelaatikon_sisapuoli.addWidget(self.toka_vihje)
        self.vihjelaatikon_sisapuoli.addWidget(self.kolmas_vihje)
        self.vihjelaatikon_sisapuoli.addWidget(self.neljas_vihje)
        self.vihjelaatikon_sisapuoli.addWidget(self.viides_vihje)

        self.vihjelaatikon_sisapuoli.addStretch() # työnnetään asetelmat ylöspäin, lähde: How to attach a changing list of widgets to the top of the QVBoxLayout in PyQT6?, Stackoverflow, https://stackoverflow.com/questions/77291072/how-to-attach-a-changing-list-of-widgets-to-the-top-of-the-qvboxlayout-in-pyqt6

        # piilotetaan vihjeet ja annetaan aluksi vain sen "Guess the country" tekstin näkyä
        self.eka_vihje.hide()
        self.toka_vihje.hide()
        self.kolmas_vihje.hide()
        self.neljas_vihje.hide()
        self.viides_vihje.hide()

        self.vihjelaatikko.setLayout(self.vihjelaatikon_sisapuoli) # laitetaan tuo QHBoxlayout vihjeboksin sisään

        # luodaan perustiedoille laatikko, joka menee vihjelaatikon päälle
        # kun arvaus menee oikein tai kun maata ei saanut arvattua ollenkaan
        self.perustiedot_laatikko = QWidget()
        self.perustiedot_laatikon_asetelma = QVBoxLayout()
        self.perustiedot_laatikko.setLayout(self.perustiedot_laatikon_asetelma)

        # asetetaan perustiedot laatikko samankokoiseksi kuin vihjelaatikko
        self.perustiedot_laatikko.setFixedHeight(270)

        # ja muokataan perustietojen laatikon tyyliä
        self.perustiedot_laatikko.setStyleSheet("""
            QWidget {
                background-color: grey;
                border: 4px solid #444444;
                border-radius: 7px;
            }
            QLabel {
                border: none;
                font-size: 17.4px;
                font-weight: bold;
            }
        """)

        # lisätään vasempaan asetelmaan perustiedot
        self.vasen_asetelma.addWidget(self.perustiedot_laatikko)
        self.perustiedot_laatikko.hide() # ei näytetä heti perustietoja

        self.hover_kielet = QLabel("")
        self.hover_naapurimaat = QLabel("")

        # luodaan perustiedoista kaikkille kohdille qlabel
        self.perustiedot_maan_nimi = QLabel("")
        self.perustiedot_maan_iso3166 = QLabel("")
        self.perustiedot_maan_maanosa = QLabel("")
        self.perustiedot_maan_pk = QLabel("")
        self.perustiedot_maan_populaatio = QLabel("")
        self.perustiedot_maan_ala = QLabel("")
        self.perustiedot_maan_itsenaisyysvuosi = QLabel("")

        # luodaan qlabelit kielille ja naapurimaille. näiden viereen tulee tooltip elementti jolla voi nähdä kaikki lopuista kielistä/maista
        self.perustiedot_maan_kielet = QLabel("")
        self.perustiedot_maan_naapurit = QLabel("")

        # lisätään kaikki paitsi kielet ja naapurimaat asetelmaan
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_nimi)
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_iso3166)
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_maanosa)
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_pk)
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_populaatio)
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_ala)
        self.perustiedot_laatikon_asetelma.addWidget(self.perustiedot_maan_itsenaisyysvuosi)

        # luodaan kielille oma qhboxlayout johon vasemmalle tulee viisi ekaa kieltä ja oikealla hover elementti
        self.kielten_asetelma = QHBoxLayout()
        self.kielten_asetelma.addWidget(self.perustiedot_maan_kielet) # tämä on siis teksti
        self.kielten_asetelma.addWidget(self.hover_kielet) # ja tämä on hover elementti
        self.kielten_asetelma.addStretch() # työnnetään elementit vasempaan reunaan, jotta ne näyttäisi yhtenäisiltä
        self.perustiedot_laatikon_asetelma.addLayout(self.kielten_asetelma)

        # tehdään sama naapurimaille
        self.naapurien_asetelma = QHBoxLayout()
        self.naapurien_asetelma.addWidget(self.perustiedot_maan_naapurit)
        self.naapurien_asetelma.addWidget(self.hover_naapurimaat)
        self.naapurien_asetelma.addStretch()
        self.perustiedot_laatikon_asetelma.addLayout(self.naapurien_asetelma)


    def naytetaan_karttakuva_tai_lippu(self, pelitila):
        """Näyttää vasemmalle puolelle ikkunaa joko karttakuvan tai lipun"""

        maan_iso3166_koodi = self.peli.hae_maan_iso3166().lower()
        tama_kansio = os.path.dirname(os.path.realpath(__file__))

        if pelitila == "kartta":
            polku = os.path.join(tama_kansio, "maiden kuvat", "all", f"{maan_iso3166_koodi}", "512.png")

        elif pelitila == "lippu":
            polku = os.path.join(tama_kansio, "maiden liput", f"{maan_iso3166_koodi}.png")

        kuva = QPixmap(polku)
        kuva = kuva.scaledToHeight(500) # lähde: Y2 kierros 5

        self.kuva.setPixmap(kuva) # lähde: Y2 kierros 5


    def siirrytaan_seuraavaan_maahan(self):
        """Tämä metodi näyttää seuraavan arvattavan maan (kun pelaaja klikkaa ."""

        self.seuraava_maa_nappi.hide() # ei näytetä nappia silloin kun ollaan siirrytty uuteen arvattavaan maahan
        self.perustiedot_laatikko.hide() # ei näytetä maan perustietoja silloin kun pelaaja on arvaamassa
        self.tekstieditori.show() # näytetään tekstieditori jotta pelaaja voi arvata
        self.tekstieditori.setFocus() # laitetaan hiiri heti takaisin tekstieditoriin, jotta pelaajan ei itse tarvitse tehdä sitä manuaalisesti
        self.vihjelaatikko.show() # näytetään vihjelaatikko
        self.piilotetaan_vihjeet_ja_naytetaan_teksti() # ei näytetä vihjeitä vielä vaan vasta se "Guess the country" teksti

        # arvotaan uusi maa ja näytetään se
        self.peli.arvotaan_maa()
        self.naytetaan_karttakuva_tai_lippu(self.peli.pelitila)


    def piilotetaan_vihjeet_ja_naytetaan_teksti(self):

        """Tämä metodi piilottaa vanhat vihjeet ja näyttää tekstin "Guess the country".
        Tätä metodia käytetään silloin, kun maa on arvattu tai kun maata ei arvattu viidellä yrityksellä
        jolloin pelaajalle arvotaan uusi maa ja ikkunassa halutaan näkyvän teksti guess the country"""

        self.eka_vihje.hide()
        self.toka_vihje.hide()
        self.kolmas_vihje.hide()
        self.neljas_vihje.hide()
        self.viides_vihje.hide()

        self.vihjelaatikon_teksti.show()


    def paivitetaan_vihjelaatikko(self):
        """Tämä metodi asettaa vihjelaatikkoon oikeat vihjeet sen mukaan,
        kuinka monta arvausta pelaaja on arvannut tiettyä maata kohden.
        Tätä metodia kutsutaan vain silloin kun arvaus on mennyt väärin.
        Ks. metodin tarkistetaan_tekstikentan_arvaus... True ja False kohdat."""

        arvausten_maara = self.peli.tamanhetkisen_maan_arvausyritykset
        seuraava_vihje = self.peli.haetaan_vihje()

        if arvausten_maara == 0 or arvausten_maara is None: # jos arvauksia ei ole tehty vielä tai jos kaikki arvaukset on käytetty
            self.vihjelaatikon_sisapuoli.addWidget(self.vihjelaatikon_teksti)

        elif arvausten_maara == 1:
            # tässä kohtaa pelaaja on siis arvannut yhden kerran (väärin), joten näytetään eka vihje
            self.vihjelaatikon_teksti.hide()  # piilotetaan Guess the country -teksti
            self.eka_vihje.setText(f"Continent: {seuraava_vihje}") # asetetaan ekan vihjeen teksti ekaan boksiin
            self.eka_vihje.show()

        elif arvausten_maara == 2:
            self.toka_vihje.setText(f"Capital city: {seuraava_vihje}")
            self.toka_vihje.show()

        elif arvausten_maara == 3:
            self.kolmas_vihje.setText(f"Languages spoken: {seuraava_vihje}")
            self.kolmas_vihje.show()

        elif arvausten_maara == 4:
            self.neljas_vihje.setText(f"Neighbouring countries: {seuraava_vihje}")
            self.neljas_vihje.show()

        elif arvausten_maara == 5:
            self.viides_vihje.setText(f"First letter: {seuraava_vihje}")
            self.viides_vihje.show()


    def naytetaan_perustiedot(self):
        """Muuttaa maan populaation ja pinta-alan arvot sellaiseen muotoon, että se ne helpompi lukea.
        Muuttaa maan kielet-lista ja naapurimaat-listan merkkijonoiksi siten, että listan viisi ensimmäistä
        näkyy pelaajalle tekstinä ja jos maita on sitä enemmän niin loput tooltipin viestikentässä.
        Nämä tiedot päivitetään tietysti perustiedot-boksiin, joka lopulta näytetään .show()-metodin avulla."""

        populaatio = int(self.peli.nykyinen_maa.hae_populaatio()) # lähde: "Space as a thousands separator in the format specification mini-language" (kohta: Nice Zombies -käyttäjän vastaus), Python.org, https://discuss.python.org/t/space-as-a-thousands-separator-in-the-format-specification-mini-language/72918/3
        populaatio = f"{populaatio:_}".replace("_", " ")

        pinta_ala = int(self.peli.nykyinen_maa.hae_pinta_ala())
        pinta_ala = f"{pinta_ala:_}".replace("_", " ")

        self.perustiedot_maan_nimi.setText(f"Country: {self.peli.nykyinen_maa.hae_nimi()}") # asetaan qlabel tekstiin maan nimi
        self.perustiedot_maan_iso3166.setText(f"ISO 3166 code: {self.peli.nykyinen_maa.hae_iso()}")
        self.perustiedot_maan_maanosa.setText(f"Continent: {self.peli.nykyinen_maa.hae_maanosa()}")
        self.perustiedot_maan_pk.setText(f"Capital city: {self.peli.nykyinen_maa.hae_paakaupunki()}")
        self.perustiedot_maan_populaatio.setText(f"Population: {populaatio}")
        self.perustiedot_maan_ala.setText(f"Area: {pinta_ala} km^2")
        self.perustiedot_maan_itsenaisyysvuosi.setText(f"Independence: {self.peli.nykyinen_maa.hae_itsenaisyysvuosi()}")

        kielet = self.peli.nykyinen_maa.hae_kielet()
        naapurit = self.peli.nykyinen_maa.hae_naapurimaat()



        # jos maassa puhutaan yli viittä kieltä niin näytetään niistä ensimmäiset viisi ja loput tooltip avulla

        if len(kielet) > 5:
            lista_viisi_kielta = kielet[:5]
            merkkijono_kielista = ",  ".join(lista_viisi_kielta)

            lista_loput_kielista = kielet[5:]
            merkkijono_lopuista_kielista = ", ".join(lista_loput_kielista)
            loput_kielet_maara = len(lista_loput_kielista)

            # näytetaan jäljelle jäävät numerot tooltip elementtinä
            self.hover_kielet.setText(f" + {loput_kielet_maara}")
            self.hover_kielet.setToolTip(merkkijono_lopuista_kielista)
            self.hover_kielet.setCursor(Qt.CursorShape.PointingHandCursor)
            # lähde: PyQt: "Changing cursor when hovering a button", Stack Overflow, https://stackoverflow.com/questions/36725245/pyqt-changing-cursor-when-hovering-a-button
            # ja "How to use Different Cursors in PyQt (Default and Custom)", YouTube, https://www.youtube.com/watch?v=nVDR7TEAeyc


        else:
            # tehdään tooltipin tekstistä tyhjä koska kieliä on alle viisi
            merkkijono_kielista = ",  ".join(kielet) # How would you make a comma-separated string from a list of strings?, Stack Overflow, https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
            self.hover_kielet.setText("")
            self.hover_kielet.setToolTip("")

        self.perustiedot_maan_kielet.setText(f"Languages: {merkkijono_kielista}")


        # jos maalla on yli viisi naapurimaata niin näytetään ensimmäiset viisi niistä ja loput tooltip avulla
        if len(naapurit) > 5:
            lista_viisi_naapurimaata = naapurit[:5]
            merkkijono_naapureista = ",  ".join(lista_viisi_naapurimaata)

            lista_loput_naapurimaista = naapurit[5:]
            merkkijono_lopuista_naapurimaista = ", ".join(lista_loput_naapurimaista)
            loput_naapurimaat_maara = len(lista_loput_naapurimaista)

            self.hover_naapurimaat.setText(f"+ {loput_naapurimaat_maara}")
            self.hover_naapurimaat.setToolTip(merkkijono_lopuista_naapurimaista)
            self.hover_naapurimaat.setCursor(Qt.CursorShape.PointingHandCursor)

        else:
            merkkijono_naapureista = ",  ".join(naapurit)
            self.hover_naapurimaat.setText("")
            self.hover_naapurimaat.setToolTip("")

        self.perustiedot_maan_naapurit.setText(f"Neighbouring countries: {merkkijono_naapureista}")

        self.perustiedot_laatikko.show() # perustiedot-boksi pitää manuaalisesti näyttää koska se alunperin piilotettin .hide() metodilla.



