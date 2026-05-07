from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QListWidget
from PyQt6.QtCore import Qt


class Oikea(QWidget):
    """Tässä luodaan ikkunan oikea puoli eli pistelaskuri, progress bar, lista arvattavasti maista ja aikarajoitus"""
    def __init__(self, peli_olio):
        super().__init__()

        self.peli = peli_olio

        # määritetään ikkunan oikean puolen asetelman tyyli
        self.oikea_asetelma = QVBoxLayout()

        # asetetaan luokalle tyyliksi tämä self.oikea_asetelma
        self.setLayout(self.oikea_asetelma)

        # varataan tilaa ajastimelle
        self.aikarajoitus = QLabel("Tähän tulee ajastin.")
        self.aikarajoitus.setStyleSheet("""
                color: white;
                background-color: #555555;
                border: 2px solid #a9a9a9; 
                border-radius: 7px;
                font-size: 16px;
                font-weight: bold;
        """)
        self.oikea_asetelma.addWidget(self.aikarajoitus, alignment=Qt.AlignmentFlag.AlignLeft)

        """Pisteboksi"""
        # luodaan pisteille näkymä
        self.pisteet = QLabel("Points: 0")
        self.pisteet.setFixedSize(150, 40)
        self.pisteet.setStyleSheet("""
                color: white;
                background-color: #555555;
                border: 2px solid #a9a9a9; 
                border-radius: 7px;
                font-size: 16px;
                font-weight: bold;
            """)

        # lisätään pisteboksi asetelmaan
        self.oikea_asetelma.addWidget(self.pisteet, alignment=Qt.AlignmentFlag.AlignRight)

        """Progressbar"""
        # luodaan kehityspalkki ja lisätään asetelmaa
        self.kehityspalkki = QProgressBar()
        self.kehityspalkki.setFixedSize(300, 30)
        self.kehityspalkki.setMaximum(len(self.peli.lista_kaikkien_maiden_nimista))  # asetetaan maksimiksi kaikkien maiden lukumäärä
        self.oikea_asetelma.addWidget(self.kehityspalkki, alignment=Qt.AlignmentFlag.AlignCenter)

        self.kehityspalkki.setStyleSheet("""
                QProgressBar {
                    color: white;
                    border-style: solid;
                    border-color: grey;
                    border-radius: 7px;
                    border-width: 2px;
                    text-align: center;
                    font-weight: bold;
                    background-color: #555555;
                }
                QProgressBar::chunk {
                    width: 2px;
                    background-color: orange;
                    margin: 1px;
                    border-radius: 3px;
                }
            """)
        # lähde: Create a Modern Style ProgressBar in PyQt6 | PyQt6 Tutorial, YouTube, https://www.youtube.com/watch?v=ms2Ey_SzZZc

        # asetetaan kehityspalkin aluksi nolla, jolloin siinä lukee 0%
        self.kehityspalkki.setValue(0)

        """Lista arvatuista maista"""
        # luodaan laatikko jossa on qlistawidget elementtejä ja lisätään asetelmaan
        self.lista_arvatuista_boksi = QWidget()
        self.lista_arvatuista_boksi.setFixedHeight(615)
        self.oikea_asetelma.addWidget(self.lista_arvatuista_boksi, alignment=Qt.AlignmentFlag.AlignCenter)

        # luodaan pääasetelma, jonka sisälle tulee kolme saraketta
        self.lista_arvatuista_boksi_asetelma = QHBoxLayout()
        self.lista_arvatuista_boksi.setLayout(self.lista_arvatuista_boksi_asetelma)

        # luodaan erilliset laatikot
        self.sarake1_laatikko = QWidget()
        self.sarake2_laatikko = QWidget()
        self.sarake3_laatikko = QWidget()

        # luodaan kolme erillistä asetelmaa, jotka jokainen menee erilliseen sarakelaatikkoon
        self.sarake1_asetelma = QVBoxLayout()
        self.sarake2_asetelma = QVBoxLayout()
        self.sarake3_asetelma = QVBoxLayout()

        # laitetaan laatikon asetelmaksi tuo vertical asetelma
        self.sarake1_laatikko.setLayout(self.sarake1_asetelma)
        self.sarake2_laatikko.setLayout(self.sarake2_asetelma)
        self.sarake3_laatikko.setLayout(self.sarake3_asetelma)

        # ja lisätään nämä laatikot horisontaaliseen asetelmaan
        self.lista_arvatuista_boksi_asetelma.addWidget(self.sarake1_laatikko)
        self.lista_arvatuista_boksi_asetelma.addWidget(self.sarake2_laatikko)
        self.lista_arvatuista_boksi_asetelma.addWidget(self.sarake3_laatikko)

        # ja muokataan niiden ulkonäköä
        self.sarake1_laatikko.setStyleSheet("""
                    border: 5px solid grey;
                    border-radius: 7px;
                    background-color: rgba(0,0,0,40);
            """)

        self.sarake2_laatikko.setStyleSheet("""
                    border: 5px solid grey;
                    border-radius: 7px;
                    background-color: rgba(0,0,0,40);
            """)

        self.sarake3_laatikko.setStyleSheet("""
                    border: 5px solid grey;
                    border-radius: 7px;
                    background-color: rgba(0,0,0,40);
            """)
        # lähde: "How to set QTableWidget background transparent in Qt?", Stack Overflow, https://stackoverflow.com/questions/10314157/how-to-set-qtablewidget-background-transparent-in-qt

        # luodaan otsikkoelementit
        self.otsikko1 = QLabel("✅ 1st try")
        self.otsikko2 = QLabel("🟨 2-6 tries")
        self.otsikko3 = QLabel("❌ Failed to guess")

        # ja muokataan niiden ulkonäköä
        self.otsikko1.setStyleSheet("""
                border-color: #00000000; 
                background-color: #00000000; 
                color: white; 
                font-size: 16px;
                font-weight: bold;
            """)
        # lähde: Googlaus "transparent color hex code"

        self.otsikko2.setStyleSheet("""
                border-color: #00000000; 
                background-color: #00000000; 
                color: white; 
                font-size: 16px;
                font-weight: bold;
            """)

        self.otsikko3.setStyleSheet("""
                border-color: #00000000; 
                background-color: #00000000;
                color: white; 
                font-size: 16px;
                font-weight: bold;
            """)

        # luodaan sitten listaelementit
        self.yksi_arvaus_boksi = QListWidget()
        self.kaksi_viiva_viisi_arvausta_boksi = QListWidget()
        self.ei_arvattu_boksi = QListWidget()

        # asetetaan QListWidgettien sort päälle, jotta listassa maiden nimet asettuisivat aakkosjärjestykseen
        self.yksi_arvaus_boksi.setSortingEnabled(True) # lähde: PyQt5 QListWidget - Making Sorting Enabled, Geeks for geeks,  https://www.geeksforgeeks.org/python/pyqt5-qlistwidget-making-sorting-enabled/
        self.kaksi_viiva_viisi_arvausta_boksi.setSortingEnabled(True)
        self.ei_arvattu_boksi.setSortingEnabled(True)

        # ja muokataan niiden ulkonäköä
        self.yksi_arvaus_boksi.setStyleSheet("""
                border-color: #00000000; 
                background-color: #00000000; 
                color: white; 
                font-size: 16px;
            """)

        self.kaksi_viiva_viisi_arvausta_boksi.setStyleSheet("""
                border-color: #00000000; 
                background-color: #00000000; 
                color: white; 
                font-size: 16px;
            """)
        # lähde: Googlaus "transparent color hex code"

        self.ei_arvattu_boksi.setStyleSheet("""
                border-color: #00000000; 
                background-color: #00000000; 
                color: white; 
                font-size: 16px;
            """)

        # laitetaan luodut otsikot ja listaelementit sarakebokseihin

        # eka boksi
        self.sarake1_asetelma.addWidget(self.otsikko1, alignment=Qt.AlignmentFlag.AlignHCenter) # laitetaan otsikot boksin keskelle
        self.sarake1_asetelma.addWidget(self.yksi_arvaus_boksi)

        # toka boksi
        self.sarake2_asetelma.addWidget(self.otsikko2, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.sarake2_asetelma.addWidget(self.kaksi_viiva_viisi_arvausta_boksi)

        # kolmas boksi
        self.sarake3_asetelma.addWidget(self.otsikko3, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.sarake3_asetelma.addWidget(self.ei_arvattu_boksi)

        self.oikea_asetelma.addSpacing(50)


    def paivitetaan_pisteet(self):
        """Päivittää pistenäkymän."""
        tamanhetkiset_pisteet = self.peli.kokonaispisteet

        if tamanhetkiset_pisteet < 0:
            self.pisteet.setStyleSheet("""
                color: #ff2800;
                background-color: #555555;
                border: 2px solid #a9a9a9; 
                border-radius: 7px;
                border-color: #ff2800;
                font-size: 16px;
                font-weight: bold;
            """)

        else:
            self.pisteet.setStyleSheet("""
                color: white;
                background-color: #555555;
                border: 2px solid #a9a9a9; 
                border-radius: 7px;
                font-size: 16px;
                font-weight: bold;
            """)
        self.pisteet.setText(f"Points: {tamanhetkiset_pisteet}")


    def paivitetaan_kehityspalkki(self):
        """Päivittää kehityspalkin ulkonäköä. tarkistetaan_tekstikentan_arvaus_ja_paivitetaan_nakyma -metodi kutsuu tätä sitä mukaan kun pelaaja on arvannut maan"""
        uusi_arvo = self.kehityspalkki.value() + 1
        maksimi = self.kehityspalkki.maximum()

        if uusi_arvo == maksimi:
            # jos pelaaja on arvannut kaikki maat
            # niin muutetaan palkin näkymää siten, että koko palkki on ns. täynnä vihreää väriä
            self.kehityspalkki.setStyleSheet("""
            QProgressBar {
                color: white;
                border-style: solid;
                border-color: grey;
                border-radius: 7px;
                border-width: 2px;
                text-align: center;
                font-weight: bold;
                background-color: grey;
            }
            QProgressBar::chunk {
                background-color: green;
                border-radius: 3px;
            }
        """)

        elif uusi_arvo > (maksimi // 2):
            # muutetaan kehityksen väri vihreäksi kun puolet kehityksestä on tehty
            self.kehityspalkki.setStyleSheet("""
            QProgressBar {
                color: white;
                border-style: solid;
                border-color: grey;
                border-radius: 7px;
                border-width: 2px;
                text-align: center;
                font-weight: bold;
                background-color: grey;
            }
            QProgressBar::chunk {
                width: 2px;
                background-color: green; 
                margin: 1px;
                border-radius: 3px;
            }
        """)
        # lähde: Create a Modern Style ProgressBar in PyQt6 | PyQt6 Tutorial, YouTube, https://www.youtube.com/watch?v=ms2Ey_SzZZc

        self.kehityspalkki.setValue(uusi_arvo) # annetaan kehityspalkin prosenttiarvoksi uusi arvo


    def nollataan_kehityspalkki(self):
        """Nollaa kehityspalkin. """
        self.kehityspalkki.setValue(0)


    def paivitetaan_arvatut_maat(self, arvaus_oikein):
        """ Lisää QListWidgetteihin maan sen mukaan, kuinka monta arvausta maan arvaamiseen meni"""
        yrityskerrat = self.peli.tamanhetkisen_maan_arvausyritykset
        maan_nimi = f"{self.peli.nykyinen_maa.hae_nimi()}"

        if arvaus_oikein and yrityskerrat == 1: # jos maa arvattiin oikein ekalla yrityksellä
            merkkijono = f"- {maan_nimi}"
            self.yksi_arvaus_boksi.addItem(merkkijono)

        elif arvaus_oikein and 2 <= yrityskerrat <= 6: # jos maa arvattaan oikein 2-5 arvauksen välillä
            merkkijono = f"- {maan_nimi} ({yrityskerrat} tries)"
            self.kaksi_viiva_viisi_arvausta_boksi.addItem(merkkijono)

        else: # jos maata ei onnistuttu arvaamaan
            merkkijono = f"- {maan_nimi}"
            self.ei_arvattu_boksi.addItem(merkkijono)

