import sys, os

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QLabel, QGraphicsOpacityEffect
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from peli import Peli
from maa import Maa
from gui_oikea_puoli import Oikea
from gui_vasen_puoli import Vasen



class Gui(QMainWindow):
    """Gui-luokka on käyttöliittymää varten kirjoitettu luokka. Se saa parametriksi Peli-olion, jonka avulla
    se pääsee käsiksi pelin tietoihin esimerkiksi siihen, mikä maa on tällä hetkellä arvattavissa. Tämän avulla
    voidaan näyttää pelaajalle mm. oikea maa ja sitä vastaavat vihjeet ikkunaan."""
    # Tässä moduulissa on käytettä lähteenä suurimmaksi osaksi Y2 kierros 5:n teorioita ja vihjeitä
    # Muut ulkoiset lähteet on kommentoitu normaalisti viereen


    def __init__(self, peli_olio): # parametrina käyttöliittymälle on peli-olio; lähde: Y2 5. kierros, tehtävä RobotWorld (valmiiksi annettu koodi)
        super().__init__()
        self.peli = peli_olio
        self.vasen_puoli = Vasen(peli_olio)
        self.oikea_puoli = Oikea(peli_olio)

        self.paa_widgetti = QWidget() # luodaan pääwidgetti

        self.setWindowTitle("Map Game") # annetaan ikkunalle nimi

        self.setFixedSize(1500, 900) # annetaan ikkunalle tarkka koko
        self.move(100, 80) # liikutetaan ikkunaa keskelle näyttöä

        """Tässä kohtaa luodaan taustakuva, josta tehdään läpinäkyvä"""

        # tässä muodostetaan oikea polku qpixmappia varten maailmankartalle
        tama_kansio = os.path.dirname(os.path.realpath(__file__)) # matkittu maiden_tiedot_parserista, tama_kansio viittaa siis y2_2026_61931_karttapeli -nimiseen kansioonn

        maailmankartta_polku = os.path.join(tama_kansio, "maailmankartta", "world.png")

        # tehdään maailmankartasta ikkunan taustakuva
        self.maailmankartta = QPixmap(f"{maailmankartta_polku}")
        self.maailmankartta =  self.maailmankartta.scaled(1500, 900, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation) # lähde: PySide6.QtGui.QPixmap kohdassa "Scales the pixmap to given size...", https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPixmap.html, ja "Qt resize image with best quality", Stackoverflow, https://stackoverflow.com/questions/22652491/qt-resize-image-with-best-quality

        self.label_maailmankartta = QLabel(self.paa_widgetti) # asetetaan maailmankartta pää_widgettiin
        self.label_maailmankartta.setPixmap(self.maailmankartta)

        # tehdään maailmankartasta yhtä suuri kuin ikkuna
        self.label_maailmankartta.setGeometry(0, 0, 1500, 900)

        # muokataan asetelmaa
        self.label_maailmankartta.setAlignment(Qt.AlignmentFlag.AlignRight) # lähde: "PyQt tutorial... ", Youtube, https://www.youtube.com/watch?v=-aYqBBnSeuc

        # tehdään taustakuvasta läpinäkyvä
        lapinakyvyys = QGraphicsOpacityEffect() # lähde: PyQt - Opacity Effect, TutorialsPoint, https://www.tutorialspoint.com/pyqt/pyqt_opacity_effect.htm
        lapinakyvyys.setOpacity(0.2)
        self.label_maailmankartta.setGraphicsEffect(lapinakyvyys)

        self.setCentralWidget(self.paa_widgetti) # asetetaan pääwidgetti centralwidgetiksi. tämä tehdään tässä kohtaa eikä aiemmin sen takia että halutaan pitää kaikki muut komponentit/elementit taustakuvan päällä

        self.paa_asetelma = QHBoxLayout()
        self.paa_widgetti.setLayout(self.paa_asetelma) # asetetaan sille asetelmaksi tuo self.paa_asetelma

        # yhdistetään pelaajan arvaus ja arvauksen tarkistaminen sekä näkymän päivittäminen (enter-napin painallus)
        self.vasen_puoli.tekstieditori.returnPressed.connect(self.tarkistetaan_tekstikentan_arvaus_ja_paivitetaan_nakyma) # lähde: "Detecting enter on a QLineEdit or QPushButton", Stackoverflow, https://stackoverflow.com/questions/15561608/detecting-enter-on-a-qlineedit-or-qpushbutton

        # lisätään pääasetelmaan vasen ja oikea puoli ja muokataan ikkunan vasemman ja oikean puolen suhdetta
        self.paa_asetelma.addWidget(self.vasen_puoli)
        self.paa_asetelma.addWidget(self.oikea_puoli)

        # ikkunan vasemman ja oikean puolen koon suhde
        self.paa_asetelma.setStretch(0, 5) # muutetaan QHBoxLayoutin vasemman ja oikean puolen suhdetta # lähde: Reddit, "[Qt] Allowing more space for a Widget in a QHBoxLayout", https://www.reddit.com/r/cpp_questions/comments/kiry8r/qt_allowing_more_space_for_a/
        self.paa_asetelma.setStretch(1, 6) # siten että suhde on 5:6 eli oikea puoli saa vähän enemmän tilaa



    def tarkistetaan_tekstikentan_arvaus_ja_paivitetaan_nakyma(self):
        """Tämä metodi tarkistaa pelaajan arvauksen ja päivittää sen mukaan ikkunan näkymän."""

        arvaus = self.vasen_puoli.tekstieditori.text().lower()

        if arvaus in self.peli.lista_kaikkien_maiden_nimista or arvaus in self.peli.lista_kaikkien_maiden_iso3166: # tarkistetaan, että onko pelaajan arvaama sana oikea maa. tällä tavalla pelaajalla ei mene typon takia yhtä arvausyritystä
            self.vasen_puoli.tekstieditori.clear() # koska arvaus oli jokin oikea maa, niin tyhjennetään tekstikenttä seuraavaa arvausta varten

            self.vasen_puoli.varoitus.setText("") # näytetään varoitus tyhjänä koska arvaus on oikea maa

            arvauksen_tulos = self.peli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot(arvaus)

            if arvauksen_tulos == True: # jos arvaus on oikein, niin päivitetään etenemisen tiedot ja näytetään perustiedot
                self.oikea_puoli.paivitetaan_pisteet() # päivitetään pisteiden määrä ikkunaan
                self.oikea_puoli.paivitetaan_kehityspalkki() # jos arvaaja pelaa oikein niin kehitystä tapahtuu
                self.vasen_puoli.piilotetaan_vihjeet_ja_naytetaan_teksti()
                self.vasen_puoli.vihjelaatikko.hide() # piilotetaan vihjelaatikko kun näytetään perustiedot
                self.vasen_puoli.tekstieditori.hide() # piilotetaan arvaustekstikenttä kun näytetään perustiedot
                self.vasen_puoli.naytetaan_perustiedot()
                self.vasen_puoli.seuraava_maa_nappi.show()
                self.oikea_puoli.paivitetaan_arvatut_maat(arvauksen_tulos)

            elif arvauksen_tulos == False: # jos arvaus meni väärin mutta yrityksiä on vielä
                self.vasen_puoli.paivitetaan_vihjelaatikko() # päivitetään silloin kun arvaus on mennyt väärin (ikkuna näyttää siis uuden vihjeen)
                self.oikea_puoli.paivitetaan_pisteet()

            elif arvauksen_tulos is None: # jos pelaaja ei arvannut maata, niin näytetään perustiedot
                self.oikea_puoli.paivitetaan_pisteet()
                self.vasen_puoli.piilotetaan_vihjeet_ja_naytetaan_teksti()
                self.vasen_puoli.vihjelaatikko.hide()
                self.vasen_puoli.tekstieditori.hide()
                self.vasen_puoli.naytetaan_perustiedot()
                self.vasen_puoli.seuraava_maa_nappi.show()
                self.oikea_puoli.paivitetaan_arvatut_maat(arvauksen_tulos)

        else: # tähän tullaan siis jos arvaus ei ole mikään maa (estetään sekä typot että randomien sanojen arvaaminen)
            self.vasen_puoli.varoitus.setText("Not a country, check for typos and guess again.")



if __name__ == '__main__':
    applikaatio = QApplication(sys.argv)

    testi_maa = Maa(
                nimi = "Finland",
                iso3166 = "FI",
                maanosa = "Eurooppa",
                paakaupunki = "Helsinki",
                populaatio = 5500000,
                pinta_ala = 338000,
                kielet = ["Finnish", "Swedish"],
                itsenaisyysvuosi = "6.12.1917",
                naapurimaat = ["Norway", "Sweden", "Russia", "Russia", "Russia", "Russia", "Russia", "Russia", "Russia", "Russia"],
                vihjeet = ["Europe", "Helsinki", "kielet", "naapurit", "F"])

    testi_maa_2 = Maa(
                nimi = "Sweden",
                iso3166 = "SE",
                maanosa = "Eurooppa",
                paakaupunki = "Tukholma",
                populaatio = 10000000,
                pinta_ala = 450000,
                kielet = ["Swedish"],
                itsenaisyysvuosi = "1523",
                naapurimaat = ["Norway", "Finland"],
                vihjeet = ["Europe", "Stockholm", "Swedish", "naapurit", "S"])


    # testi-peli, jolle annetaan listaan vain yksi maa testaamista varten (testimaana siis nyt Suomi)
    testi_peli = Peli([testi_maa, testi_maa_2])

    testi_peli.pelitila = "kartta"

    # annetaan pelattavaksi alueeksi maailma
    testi_peli.maanosa_jossa_pelataan("world")

    # arvotaan yksi maa
    testi_peli.arvotaan_maa()

    #syötetään testi_peli käyttöliittymälle
    ikkuna = Gui(testi_peli) # lähde: Y2 5. kierros, tehtävä RobotWorld

    ikkuna.vasen_puoli.naytetaan_karttakuva_tai_lippu(testi_peli.pelitila)

    ikkuna.show()
    sys.exit(applikaatio.exec())