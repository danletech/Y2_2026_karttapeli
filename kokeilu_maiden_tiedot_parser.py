from maiden_tiedot_parser import kaikkien_maiden_data

maiden_tiedot = kaikkien_maiden_data()

lkm = len(maiden_tiedot)
print(f"Maiden lukumäärä on {lkm}.\n")

#print(maiden_tiedot)

print("Maat ja niiden tiedot:")
for maa in maiden_tiedot:
    tulostus = f"{maa} : {maiden_tiedot[maa]}"
    print(tulostus)