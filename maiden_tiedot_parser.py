import os
import json

# Tämän moduulin kaikkien_maiden_data -funktio lukee kaikkien maiden nimet ja tiedot sekä lisää ne sanakirjaan.
# Sanakirjan sisällä on avaimena maan nimi ja sitä vastaava arvo on sanakirja, jossa on sen maan tietoja
# esim: {"Finland" : {"city": ""Helsinki", "population": 5500000, ...}, "Sweden" : {"city": "Stockholm", ...}}


def kaikkien_maiden_data():
    sanakirja_maista_ja_tiedoista = {}


    tarvittavat_tiedostot = ["country-by-abbreviation.json",
                        "country-by-capital-city.json",
                        "country-by-population.json",
                        "country-by-surface-area.json",
                        "country-by-languages.json",
                        "country-by-independence-date.json"]

    tama_kansio = os.path.dirname(os.path.realpath(__file__)) #lähde: https://www.geeksforgeeks.org/python/file-searching-using-python/
    kansion_nimi = os.path.join(tama_kansio, "maiden tiedot") #lähde: https://www.geeksforgeeks.org/python/python-os-path-join-method/

    for tiedoston_nimi in tarvittavat_tiedostot:
        polku_tiedostoon = os.path.join(kansion_nimi, tiedoston_nimi)

        with open(polku_tiedostoon, "r") as tiedosto_maat:
            tiedoston_data = json.load(tiedosto_maat) #lähde: https://www.geeksforgeeks.org/python/read-write-and-parse-json-using-python/

            for sanakirja in tiedoston_data: #tiedoston_data on lista ja sen sisällä on sanakirjoja on esim: {"country": "Afghanistan", "continent": "Asia"}
                #print(maa) #testejä varten
                maan_nimi = sanakirja["country"]

                if maan_nimi not in sanakirja_maista_ja_tiedoista:
                    sanakirja_maista_ja_tiedoista[maan_nimi] = {} #luodaan jokaista maata kohti yksi sanakirja, johon tallennetaan maan tietoja

                # tallennetaan uutta dataa sanakirjana suurempaan sanakirjaan "sanakirja_maista_ja_tiedoista"
                for key, value in sanakirja.items(): #lähde: https://www.w3schools.com/python/trypython.asp?filename=demo_dict_items
                    if key != "country": #nimeä ei haluta tallentaa uudestaan sanakirjaan
                        sanakirja_maista_ja_tiedoista[maan_nimi][key] = value #lähde: https://www.geeksforgeeks.org/python/python-dictionary-items-method/



    # Minulla tuli ongelma tiedoston "bordering-countries.json" kanssa tuossa silmukassa,
    # joten tein sille erillisin silmukan. Tämä tiedosto oli siis eri lähteestä kuin muut, minkä takia
    # naapurimaiden tiedot on tallennettu eri tavalla kuin muut tiedot. Tämä aiheutti silmukkaan ongelman, jota
    # en osannut korjata ja sen takia kirjoitin toisen silmukan vain tälle tiedostolle:

    naapurit_tiedosto = "bordering-countries.json"

    polku_tiedostoon_naapurit = os.path.join(kansion_nimi, naapurit_tiedosto)

    with open(polku_tiedostoon_naapurit, "r") as naapurit:
        naapurit_data = json.load(naapurit)

        for key, value in naapurit_data.items():
            if key in sanakirja_maista_ja_tiedoista: #tarkistetaan varmuuden vuoksi, että onko lisättävä maa suuremmassa listassa
                sanakirja_maista_ja_tiedoista[key]["neighbouring countries"] = value

    # testaamisen jälkeen sanakirjaan jäi vielä paljon maita, jotka eivät ole itsenäisiä valtioita,
    # joten suodatetaan se vielä tässä
    # lähde: https://www.geeksforgeeks.org/python/python-filter-dictionary-values-in-heterogeneous-dictionary/ ja
    # https://www.w3schools.com/python/python_dictionaries_access.asp

    sanakirja_maista_ja_tiedoista2 = {key: val for key, val in sanakirja_maista_ja_tiedoista.items() if val.get("independence") is not None}

    #nyt palautetaan sanakirja, jossa on kaikkien maiden tiedot
    return sanakirja_maista_ja_tiedoista2








