from maiden_tiedot_parser import kaikkien_maiden_data, luodaan_maa_oliot
from PyQt6.QtWidgets import QApplication
from peli import Peli
from gui import Gui
import sys


def main():
    # luodaan applikaatio
    applikaatio = QApplication(sys.argv)

    # ensin luodaan lista Maa-olioista, jotka sitten annetaan Peli-oliolle parametriksi
    maiden_tiedot = kaikkien_maiden_data()
    maa_oliot_lista = luodaan_maa_oliot(maiden_tiedot)
    peli_olio = Peli(maa_oliot_lista)

    # luodaan käyttöliittymä, jolle annetaan peli-olio:
    kayttoliittyma = Gui(peli_olio)

    # avataan aloitusikkuna, jossa pelaaja maanosan, kartan/lipun ja pelin vaikeustason
    kayttoliittyma.kysy_valinnat_aloitusikkunalta_ja_aloita_karttapeli()

    # näytetään ikkuna ja käynnistetään peli
    kayttoliittyma.show()
    sys.exit(applikaatio.exec())


if __name__ == '__main__':
    main()
