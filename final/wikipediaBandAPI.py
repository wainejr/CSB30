# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import re
import urllib.request
import xml.etree.ElementTree as ET
import wptools
# Instead of pip install psycopg2 try pip install psycopg2-binary
import psycopg2
import psycopg2.extras

tabledef = [
    {
        "url": "music",
        "format": ["person", "bandUri", "rating"],
        "table": "likesArtist"
    },
]

def xml2dict(tabledef):
    dict2ret = {}
    for tableitem in tabledef:
        itemList = []
        conn = urllib.request.urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/"+ tableitem["url"] + ".xml")
        xmltree = ET.parse(conn)
        root = xmltree.getroot()
        for item in root.iter():
            if item.attrib:
                itemObj = item.attrib
                elementList = []
                for attr in tableitem["format"]:
                    elementList.append(itemObj[attr])
                itemList.append(elementList)
        dict2ret[tableitem["table"]] = itemList
    return dict2ret

dictxml = xml2dict(tabledef)

list_bands = []

for key in dictxml.keys():
	for item in dictxml[key]:
			list_bands.append(item[1].split('/')[-1])
 
bands_dicts = []

for band in list_bands:
    try:
        data = requests.get('http://dbpedia.org/data/' + band + '.json').json()
        band_data = data['http://dbpedia.org/resource/' + band]
        band_dict = {
                "id": "https://en.wikipedia.org/wiki/" + band,
                "name": "",
                "hometown": "",
            }
        for key in sorted(band_data):
            if key.split("/")[-1] == "name":
                band_dict["name"] = band_data[key][0]["value"]
            elif (key.split("/")[-1] == "hometown"):
                band_dict["hometown"] = band_data[key][0]["value"].split("/")[-1]
        if band_dict["name"] != "":
            bands_dicts.append(band_dict)
            print(band_dict)
    except:
        pass




        
