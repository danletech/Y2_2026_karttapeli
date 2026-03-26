from maiden_tiedot_parser import kaikkien_maiden_data
from maa import Maa, luodaan_maa_oliot

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
    if maa.get_name() == "Finland":
        print(maa)

