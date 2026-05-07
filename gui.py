import sys, os

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QLabel, QGraphicsOpacityEffect, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer

from peli import Peli
from maa import Maa
from gui_oikea_puoli import Oikea
from gui_vasen_puoli import Vasen
from gui_aloitusikkuna import Aloitusikkuna




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

        # yhdistetään skip-napin painallus sitä vastaaville metodeille, jotka päivättävät näkymää ja pisteitä
        self.vasen_puoli.skip_nappi.clicked.connect(self.skip_nappia_painettu)

        # lisätään pääasetelmaan vasen ja oikea puoli ja muokataan ikkunan vasemman ja oikean puolen suhdetta
        self.paa_asetelma.addWidget(self.vasen_puoli)
        self.paa_asetelma.addWidget(self.oikea_puoli)

        # ikkunan vasemman ja oikean puolen koon suhde
        self.paa_asetelma.setStretch(0, 5) # muutetaan QHBoxLayoutin vasemman ja oikean puolen suhdetta # lähde: Reddit, "[Qt] Allowing more space for a Widget in a QHBoxLayout", https://www.reddit.com/r/cpp_questions/comments/kiry8r/qt_allowing_more_space_for_a/
        self.paa_asetelma.setStretch(1, 6) # siten että suhde on 5:6 eli oikea puoli saa vähän enemmän tilaa

        # vaikeustaso
        self.valittu_vaikeustaso = None
        self.aikaa_jaljella = 0

        self.lopetusruutu = QMessageBox()


        """Ajastin"""
        # ajastimen teko on lähetulkoon kokonaan matkittu tästä foorumista:
        # lähde: "PyQt countdown timer in mm:ss format", Stack Overflow, https://stackoverflow.com/questions/62006303/pyqt-countdown-timer-in-mmss-format

        self.ajastin = QTimer(self)

        # yhdistetään next-country nappi siihen, että se laittaa ajastimen takaisin päälle (tai sitten jos peli on loppunut niin ei laita ajastinta vaan antaa loppuikkunan)
        self.vasen_puoli.seuraava_maa_nappi.clicked.connect(self.jatketaan_tai_lopetetaan_peli)



    """Metodit"""
    def kysy_valinnat_aloitusikkunalta_ja_aloita_karttapeli(self):
        aloitus_ikkuna = Aloitusikkuna()
        if aloitus_ikkuna.exec(): # jatkaa tältä riviltä eteenpäin vain kun accept() on suoritettu: self.accept() suoritetaan aloitusikkunan moduulissa vain sitten kun jokin vaikeustaso on valittu
            # lähde: PyQt QDialog - returning a value and closing from dialog, Stack Overflow, https://stackoverflow.com/questions/28706651/pyqt-qdialog-returning-a-value-and-closing-from-dialog

            # tallennetaan mitä pelaaja on valinnut aloitusikkunassa
            maanosa = aloitus_ikkuna.valittu_maanosa
            pelitila = aloitus_ikkuna.valittu_pelitila
            self.valittu_vaikeustaso = aloitus_ikkuna.valittu_vaikeustaso

            # syötetään tieto maanosasta peli-oliolle
            self.peli.maanosa_jossa_pelataan(maanosa)
            self.peli.pelitila = pelitila

            pelattavien_maiden_maara = len(self.peli.arvattavat_maat)
            self.oikea_puoli.kehityspalkki.setMaximum(pelattavien_maiden_maara) # annetaan kehityspalkille maksimiksi maanosan arvattavien maiden määrä

            # kun maanosa on kerrottu pelille niin arvotaan maa ja näytetään maan joko kartta tai lippu riippuen pelaajan valinnasta
            self.peli.arvotaan_maa()
            self.vasen_puoli.naytetaan_karttakuva_tai_lippu(self.peli.pelitila)

            # aloitetaan ajastin heti
            self.aloitetaan_ajastin()

        else: # jos pelaaja painoi cancel tai x nappia niin ohjelma suljetaan
            sys.exit()

    def aloitetaan_ajastin(self):
        if self.valittu_vaikeustaso == "Easy (15 min)":
            self.aikaa_jaljella = 900 # 15 min
        elif self.valittu_vaikeustaso == "Medium (10 min)":
            self.aikaa_jaljella = 600 # 10 min
        elif self.valittu_vaikeustaso == "Hard (5 min)":
            self.aikaa_jaljella = 300 # 5 min

        self.ajastin.timeout.connect(self.ajastin_tikittaa)
        self.ajastin.start(1000)
        self.paivitetaan_ajastimen_gui()

    def ajastin_tikittaa(self):
        self.aikaa_jaljella -= 1

        if self.aikaa_jaljella <= 0: # jos aika on loppunut
            self.ajastin.stop()
            self.peli.asetetaan_aika_loppuneeksi() # annetaan peli-olion tietää että aika on loppunut
            self.naytetaan_pelin_lopetusruutu() # eli kun ajastin saavuttaa arvon nolla (self.aikaa_jaljellä myös tällöin nolla) niin kutsutaan metodia joka luo lopetusruudun

        elif self.peli.peli_loppui(): # jos maita ei ole enää arvattavana
            self.ajastin.stop()
            self.naytetaan_pelin_lopetusruutu()

        self.paivitetaan_ajastimen_gui()

    def paivitetaan_ajastimen_gui(self):
        minsec = self.secs_to_minsec(self.aikaa_jaljella)
        self.oikea_puoli.aikarajoitus.setText(f"Time left: {minsec}")

        if self.aikaa_jaljella <= 60: # muutetaan ajastimen väri punaiseksi kun aikaa on enää alle minutti
            self.oikea_puoli.aikarajoitus.setStyleSheet("""
                color: #ff2800;
                background-color: #555555;
                border: 2px solid #a9a9a9; 
                border-radius: 7px;
                border-color: #ff2800;
                font-size: 16px;
                font-weight: bold;
            """)

        else:
            self.oikea_puoli.aikarajoitus.setStyleSheet("""
                color: white;
                background-color: #555555;
                border: 2px solid #a9a9a9; 
                border-radius: 7px;
                font-size: 16px;
                font-weight: bold;
            """)


    def secs_to_minsec(self, secs):
        mins = secs // 60
        secs = secs % 60
        minsec = f'{mins:02}:{secs:02}'
        return minsec


    def jatketaan_tai_lopetetaan_peli(self):
        peli_jatkuu = self.vasen_puoli.siirrytaan_seuraavaan_maahan()

        # jos siirrytään_seuraavaan_maahan() antaa True niin se tarkoittaa, että maita on vielä arvattavana, joten laitetaan ajastin päälle
        if peli_jatkuu:
            self.ajastin.start(1000)

        # jos siirrytään_seuraavaan_maahan() antaa False niin se tarkoittaa, ettei maita ole enää arvattavana. päätetään siis peli.
        else:
            self.naytetaan_pelin_lopetusruutu()


    def tarkistetaan_tekstikentan_arvaus_ja_paivitetaan_nakyma(self):
        """Tämä metodi tarkistaa pelaajan arvauksen ja päivittää sen mukaan ikkunan näkymän."""

        arvaus = self.vasen_puoli.tekstieditori.text().lower()

        if arvaus in self.peli.lista_kaikkien_maiden_nimista or arvaus in self.peli.lista_kaikkien_maiden_iso3166: # tarkistetaan, että onko pelaajan arvaama sana oikea maa. tällä tavalla pelaajalla ei mene typon takia yhtä arvausyritystä
            self.vasen_puoli.tekstieditori.clear() # koska arvaus oli jokin oikea maa, niin tyhjennetään tekstikenttä seuraavaa arvausta varten

            self.vasen_puoli.varoitus.setText("") # näytetään varoitus tyhjänä koska arvaus on oikea maa

            arvauksen_tulos = self.peli.tarkistetaan_arvaus_ja_paivitetaan_arvaustiedot(arvaus)

            if arvauksen_tulos == True: # jos arvaus on oikein, niin päivitetään etenemisen tiedot, näytetään perustiedot ja pysäytetään ajastin
                self.oikea_puoli.paivitetaan_pisteet() # päivitetään pisteiden määrä ikkunaan
                self.oikea_puoli.paivitetaan_kehityspalkki() # jos arvaaja pelaa oikein niin kehitystä tapahtuu
                self.vasen_puoli.piilotetaan_vihjeet_ja_naytetaan_teksti()
                self.vasen_puoli.vihjelaatikko.hide() # piilotetaan vihjelaatikko kun näytetään perustiedot
                self.vasen_puoli.tekstieditori.hide() # piilotetaan arvaustekstikenttä kun näytetään perustiedot
                self.vasen_puoli.skip_nappi.hide()
                self.vasen_puoli.naytetaan_perustiedot()
                self.ajastin.stop()
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
                self.vasen_puoli.skip_nappi.hide()
                self.vasen_puoli.naytetaan_perustiedot()
                self.ajastin.stop()
                self.vasen_puoli.seuraava_maa_nappi.show()
                self.oikea_puoli.paivitetaan_arvatut_maat(arvauksen_tulos)

        else: # tähän tullaan siis jos arvaus ei ole mikään maa (estetään sekä typot että randomien sanojen arvaaminen)
            self.vasen_puoli.varoitus.setText("Not a country, check for typos and guess again.")


    def skip_nappia_painettu(self):
        """Ajetaan kun pelaaja on painanut Skip-nappia. Tämä metodi päivittää näkymän."""
        self.vasen_puoli.tekstieditori.clear()
        self.vasen_puoli.varoitus.setText("")

        # kerrotaan peli-oliolle, että maa skipattiin. tämä vähentää kokonaispisteistä 10p
        self.peli.maa_skipattu()

        # päivitetään näkymä siten että näytetään perustiedot
        # tismalleen sama päivitys kuin tarkistetaan_tekstikentan_arvaus_ja_paivitetaan_nakyma elif None haara
        # (tätähän se oikeastaan edustaa sillä skippaus on samaa kuin että arvaus ei onnistu 6 arvauksella mutta erona on että miinustetaan 10p kokonaispisteistä)
        self.oikea_puoli.paivitetaan_pisteet() # päivitetään se että pisteitä lähti -10p
        self.vasen_puoli.piilotetaan_vihjeet_ja_naytetaan_teksti() # piilotetaan vihjeboksi
        self.vasen_puoli.vihjelaatikko.hide() # sekä vihjelaatikot
        self.vasen_puoli.tekstieditori.hide() # piilotetaan tekstieditori
        self.vasen_puoli.skip_nappi.hide() # piilotetaan skip-nappi, ettei sitä voi painaa vielä
        self.vasen_puoli.naytetaan_perustiedot() # näytetään pelaajalle skipatun maan perustiedot
        self.ajastin.stop() # pysäytetään ajastin koska pelaaja katsoo perustietoja
        self.vasen_puoli.seuraava_maa_nappi.show() # näytetään nappi, jolla pääsee arvaamaan seuraavaa maata
        self.oikea_puoli.paivitetaan_arvatut_maat(False)

    def naytetaan_pelin_lopetusruutu(self):
        """Tätä kutsutaan silloin kun aika loppuu tai jos pelaaja saa arvattua kaikki maat."""

        self.ajastin.stop()

        sanakirja = self.peli.arvausten_maarat

        lista_oikein_arvatuista_maista = []
        for maa in sanakirja:
            if sanakirja[maa] > 0:
                lista_oikein_arvatuista_maista.append(maa)

        arvattujen_maiden_maara = len(lista_oikein_arvatuista_maista)

        self.lopetusruutu.setWindowTitle("Game Over!") # lopetusruutu on qmessagebox
        self.lopetusruutu.setText(f"The game ended. Good job!\n You got {self.peli.kokonaispisteet} points and guessed {arvattujen_maiden_maara} countries")

        self.lopetusruutu.exec()

        self.close()
