# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import urllib.request
import xml.etree.ElementTree as ET
import wptools

tabledef = [
    # {
    #     "url": "person",
    #     "format": ["uri", "name", "hometown"],
    #     "table": "users"
    # },
    # {
    #     "url": "knows",
    #     "format": ["person", "colleague"],
    #     "table": "friends"
    # },
    {
        "url": "movie",
        "format": ["person", "movieUri", "rating"],
        "table": "likesMovie"
    },
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

list_artist = []
list_movies = []

for key in dictxml.keys():
	for item in dictxml[key]:
		if key == "likesArtist":
			list_artist.append(item[1].split("/")[-1])

		if key == "likesMovie":
			list_movies.append(item[1])

dict_artist = {}


for index,artist in enumerate(list_artist) :
	if index == 3:
		break
	dict_artist[artist] = {}
	page = wptools.page(str(artist))
	page.get_parse()
	try:
		# years_active = re.findall('[0-9]{4}|present{1}', page.data['infobox']['years_active'])
		# print(years_active)
		# year_initial = years_active.split("–")[0]
		# year_final = years_active.split("–")[1] # pode parecer um traco mas nao eh
		# dict_artist[artist]['year_initial'] = year_initial
		# dict_artist[artist]['year_final'] = year_final
		
	except Exception as e:
		print(e)


	
print(dict_artist)





