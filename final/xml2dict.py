# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.request import urlopen
import xml.etree.ElementTree as ET

tabledef = {
    "person": {
        "url": "person",
        "format": ["uri", "name", "hometown"],
        "table": "users",
    },
    "knows": {"url": "knows", "format": ["person", "colleague"], "table": "friends"},
    "movie": {
        "url": "movie",
        "format": ["person", "movieUri", "rating"],
        "table": "likes_movie",
    },
    "music": {
        "url": "music",
        "format": ["person", "bandUri", "rating"],
        "table": "likesArtist",
    },
}


def xml2dict(table_name):
    dict2ret = {}
    itemList = []
    conn = urlopen(
        "http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/" + table_name + ".xml"
    )
    xmltree = ET.parse(conn)
    root = xmltree.getroot()
    for item in root.iter():
        if item.attrib:
            itemObj = item.attrib
            elementList = []
            for attr in tabledef[table_name]["format"]:
                elementList.append(itemObj[attr])
            itemList.append(elementList)
    dict2ret[tabledef[table_name]["table"]] = itemList

    return dict2ret
