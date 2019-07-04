# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from xml2dict import xml2dict
from urllib.parse import unquote
from unidecode import unidecode

def generateWikipediaTuples(verbose=False):
    bands_url_names = []
    band_related_list = []
    seen_bands = set()

    band_dict = xml2dict("music")

    for key in band_dict.keys():
        for item in band_dict[key]:
            bands_url_names.append(unidecode(unquote(item[1].split("/")[-1])))

    for band_url_name in bands_url_names:
        if band_url_name not in seen_bands:
            seen_bands.add(band_url_name)
            try:
                data = requests.get(
                    "http://dbpedia.org/data/" + band_url_name + ".json"
                    ).json()
                # treats redirecting
                redir_k = "http://dbpedia.org/ontology/wikiPageRedirects"
                if redir_k in data: 
                    data = requests.get(
                        data[redir_k]["value"]+".json"
                        ).json()
                    
                band_data = data["http://dbpedia.org/resource/"+band_url_name]

                band_dict = {
                    "id": "https://en.wikipedia.org/wiki/" + band_url_name,
                    "name": None,
                    "hometown": None,
                }
                try:
                    for key in sorted(band_data):
                        if key.split("/")[-1] == "name":
                            band_dict["name"] = band_data[key][0]["value"]
                        elif key.split("/")[-1] == "hometown":
                            band_dict["hometown"] = band_data[key][0]["value"].split("/")[-1]
                except Exception as e:
                    print(e)
                    print("Unable to get name/hometown of band id", band_dict["id"])
                if band_dict["name"] is None:
                    band_dict["name"] = band_url_name
                band_related_list.append(
                    {
                        "values": [
                            band_dict["id"],
                            band_dict["name"],
                            band_dict["hometown"],
                        ]
                    }
                )
                if(verbose):
                    print(band_related_list[-1])
            except Exception as e:
                print(e)
                print("DBPedia failed at getting bands information\nURL:", band_url_name)

    return band_related_list
