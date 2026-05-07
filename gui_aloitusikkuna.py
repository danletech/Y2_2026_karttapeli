from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox, QRadioButton
from PyQt6.QtCore import Qt

class Aloitusikkuna(QDialog): # lähde: Y2 kierros 5 (esimerkki 3)
    """Tämä luokka vastaa pienen ikkunan avautimesta ja pelimoodien valinnoista."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to play a map game!")
        self.setFixedSize(400, 400)

        # muokataan ikkunan ulkonäköä
        self.setStyleSheet("""
            background-color: #656565; 
            color: white;
        """)

        # asetetaan aluksi valinnoiksi None
        self.valittu_maanosa = None
        self.valittu_pelitila = None
        self.valittu_vaikeustaso = None

        # luodaan vertikaalinen asetelma. asetetaan ikkunan asetelmaksi tämä
        self.paa_asetelma = QVBoxLayout()
        self.setLayout(self.paa_asetelma)

        """Maanosa"""
        # luodaan teksti maanosan valitsemisesta ja muokataan ulkonäköä
        self.maanosa_teksti = QLabel("Choose the continent:")
        self.maanosa_teksti.setStyleSheet("""font-weight: bold""")
        self.maanosa_teksti.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # lisätään tämä teksti ikkunaan
        self.paa_asetelma.addWidget(self.maanosa_teksti)

        # luodaan pudotusvalikko ja lisätään siihen kaikki vaihtoehdot
        self.maanosa_pudotusvalikko = QComboBox() # lähde: Y2 kierros 5 (esimerkki 3)
        self.maanosa_pudotusvalikko.setStyleSheet("""
            background-color: #444444;
            font-size: 15px;
            """)

        self.maanosa_pudotusvalikko.setFixedHeight(30)
        self.maanosat_lista = ["World", "Africa", "Asia", "Europe", "Oceania", "North America", "South America"]
        self.maanosa_pudotusvalikko.addItems(self.maanosat_lista) # lähde: "PyQt5 – How to add multiple items to the ComboBox ?", Geeks for geeks, https://www.geeksforgeeks.org/python/pyqt5-how-to-add-multiple-items-to-the-combobox/

        #lisätään pudotusvalikko ikkunaan
        self.paa_asetelma.addWidget(self.maanosa_pudotusvalikko)

        # lisätään väliä ennen pelitilan valitsemista
        self.paa_asetelma.addSpacing(20)


        """Pelitila"""
        # luodaan valikko pelitilan valinnalle
        self.pelitila_teksti = QLabel("Choose the game mode:")
        self.pelitila_teksti.setStyleSheet("""font-weight: bold""")
        self.pelitila_teksti.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # lisätään tämä teksti ikkunaan
        self.paa_asetelma.addWidget(self.pelitila_teksti)

        # luodaan pudotusvalikko ja lisätäään siihen vaihtoehdot kartan ja lipun välillä
        self.pelitila_pudotusvalikko = QComboBox()
        self.pelitila_pudotusvalikko.setStyleSheet("""
            background-color: #444444;
            font-size: 15px;
            """)
        self.pelitila_pudotusvalikko.setFixedHeight(30)
        self.pelitila_pudotusvalikko.addItems(["Map", "Flag"])
        self.paa_asetelma.addWidget(self.pelitila_pudotusvalikko)

        # lisätään väliä ennen vaikeustason valitsemista
        self.paa_asetelma.addSpacing(20)


        """Vaikeustaso"""
        # luodaan valikko vaikeustason valinnalle
        self.vaikeustaso_teksti = QLabel("Choose the difficulty:")
        self.vaikeustaso_teksti.setStyleSheet("""font-weight: bold""")
        self.vaikeustaso_teksti.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.paa_asetelma.addWidget(self.vaikeustaso_teksti)

        # luodaan nappien asetelmalle vertikaalinen asetelma
        self.vaikeustasonappien_asetelma = QVBoxLayout()

        # luodaan napit
        self.easy_nappi = QRadioButton("Easy (15 min)") # lähde: Y2 kierros 5
        self.medium_nappi = QRadioButton("Medium (10 min)")
        self.hard_nappi = QRadioButton("Hard (5 min)")

        self.easy_nappi.setFixedHeight(25)
        self.medium_nappi.setFixedHeight(25)
        self.hard_nappi.setFixedHeight(25)

        # muokataan niiden ulkonäköä
        self.easy_nappi.setStyleSheet("""
            background-color: #444444;
            font-size: 15px;
            border: 1px solid black; 
            """)
        self.medium_nappi.setStyleSheet("""
            background-color: #444444;
            font-size: 15px;
            border: 1px solid black; 
            """)
        self.hard_nappi.setStyleSheet("""
            background-color: #444444;
            font-size: 15px;
            border: 1px solid black; 
            """)

        # lisätään ne vaikeustasonappien asetelmaan
        self.vaikeustasonappien_asetelma.addWidget(self.easy_nappi)
        self.vaikeustasonappien_asetelma.addWidget(self.medium_nappi)
        self.vaikeustasonappien_asetelma.addWidget(self.hard_nappi)

        # ja lisätään tämä nappien asetelma ikkunan asetelmaan
        self.paa_asetelma.addLayout(self.vaikeustasonappien_asetelma)

        # lisätään väliä ennen cancel ja start nappeja
        self.paa_asetelma.addSpacing(20)

        # luodaan cancel ja start napit aloitusikkunalle
        self.nappi_asetelma = QHBoxLayout() # halutaan ne vierekkäin
        self.nappi_asetelma.addStretch() # työnnetään napit oikeaan alakulmaan

        # annetaan niille nimet
        self.cancel_nappi = QPushButton("Cancel")
        self.start_nappi = QPushButton("Start Game")

        # lisätään asetalmaan cancel ja start napit
        self.nappi_asetelma.addWidget(self.cancel_nappi)
        self.nappi_asetelma.addWidget(self.start_nappi)

        # lisätään tämä horisontaalinen asetelma pääasetelmaan
        self.paa_asetelma.addLayout(self.nappi_asetelma)

        # yhdistetään napit toimintoihin
        self.cancel_nappi.clicked.connect(self.close) # close sulkee ikkunan eli kun pelaaja painaa cancel niin ikkuna sulkeutuu
        self.start_nappi.clicked.connect(self.aloita_nappia_painettu) # yhdistää start-napin painamisen metodiin aloita_nappia_painettu, joka on alla:

        self.varoitus = QLabel()


    def aloita_nappia_painettu(self):
        """Tämä yhdistetaan "Start Game" -napin painallukseen. Lisäksi metodi kerää tiedot pelaajan valinnoista ja sulkee ikkunan."""

        # tallennetaan maanosan tieto
        self.valittu_maanosa = self.maanosa_pudotusvalikko.currentText() # lähde: "How do you get the current text contents of a QComboBox?", Stack Overflow, https://stackoverflow.com/questions/6061893/how-do-you-get-the-current-text-contents-of-a-qcombobox

        # tallennetaan pelitilan tieto
        pelitila = self.pelitila_pudotusvalikko.currentText() # haetaan pelitilan teksti

        if pelitila == "Map": # jos valinnan teksti on "Map" niin tallennetaan pelitilaksi "kartta", muuten "lippu"
            self.valittu_pelitila = "kartta"
        else:
            self.valittu_pelitila = "lippu"

        # katsotaan mikä radiobutton on valittuna
        if self.easy_nappi.isChecked(): # lähde: Y2 kierros 5 esimerkki 3
            self.valittu_vaikeustaso = "Easy (15 min)"

        elif self.medium_nappi.isChecked():
            self.valittu_vaikeustaso = "Medium (10 min)"

        elif self.hard_nappi.isChecked():
            self.valittu_vaikeustaso = "Hard (5 min)"

        else:
            # jos pelaaja ei ole valinnut mitään vaikeustasoa
            return # ei siis anneta metodin suorittaa loppuun asti jolloin accept() ei tapahdu. tällöin myöskään ikkuna ei sulkeudu, eikä pelaaja pääse eteenpäin

        # kun pelaaja on valinnut kaikki peliin liittyvät vaihtoehdot niin accept palauttaa sulkee ikkunan ja palauttaa True. Jos pelaaja painaa cancel niin accept palauttaa False
        self.accept() # lähde: "How to close a QDialog", Stack Overflow, https://stackoverflow.com/questions/31146799/how-to-close-a-qdialog