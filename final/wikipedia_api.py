# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from xml2dict import xml2dict


def generateWikipediaTuples():
    bands_url_names = []
    band_related_tuples = {"bands": []}
    seen_bands = set()

    band_dict = xml2dict("music")

    for key in band_dict.keys():
        for item in band_dict[key]:
            bands_url_names.append(item[1].split("/")[-1])

    for band_url_name in bands_url_names:
        if band_url_name not in seen_bands:
            seen_bands.add(band_url_name)
            try:
                data = requests.get(
                    "http://dbpedia.org/data/" + band_url_name + ".json"
                ).json()
                band_data = data["http://dbpedia.org/resource/" + band_url_name]

                band_dict = {
                    "id": "https://en.wikipedia.org/wiki/" + band_url_name,
                    "name": None,
                    "hometown": None,
                }
                for key in sorted(band_data):
                    if key.split("/")[-1] == "name":
                        band_dict["name"] = band_data[key][0]["value"]
                    elif key.split("/")[-1] == "hometown":
                        band_dict["hometown"] = band_data[key][0]["value"].split("/")[-1]

                band_related_tuples["bands"].append(
                    {
                        "values": [
                            band_dict["id"],
                            band_dict["name"],
                            band_dict["hometown"],
                        ]
                    }
                )
                print(band_related_tuples["bands"][-1])
            except:
                print("DBPedia failed at getting band...")

    return band_related_tuples
