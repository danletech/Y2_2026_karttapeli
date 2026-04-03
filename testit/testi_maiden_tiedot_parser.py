from maiden_tiedot_parser import kaikkien_maiden_data, luodaan_maa_oliot
from maa import Maa

# Tämä moduuli on puhtaasti omaa kokeiluani varten. Näiden kokeilujen avulla nään nopeasti toimiiko
# ohjelma oikein sekä palautetaanko ja tallennetaanko tiedot oikein. Voit kokeilla ajamalla tämän koodin.

maiden_tiedot = kaikkien_maiden_data()

lkm = len(maiden_tiedot)
print(f"Maiden lukumäärä on {lkm}.\n")

#print(maiden_tiedot)

print("Maat ja niiden tiedot:")
for maa in maiden_tiedot:
    tulostus = f"{maa} : {maiden_tiedot[maa]}"
    print(tulostus)
    #print(maa)
    #print(maiden_tiedot[maa])
    print()

maa_oliot_lista = luodaan_maa_oliot(maiden_tiedot)

for maa in maa_oliot_lista:
    if maa.hae_nimi() == "Finland":
        print(maa)
        print()
        kaikkitiedot = maa.hae_perustiedot()
        for tieto in kaikkitiedot:
            print(tieto)
            print(kaikkitiedot[tieto])
            print()



