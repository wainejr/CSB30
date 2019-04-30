# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib2 import urlopen
import xml.etree.ElementTree as ET

tabledef = [
    {
        "url": "person",
        "format": ["uri", "name", "hometown"],
        "table": "users"
    },
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
    {
        "url": "knows",
        "format": ["person", "colleague"],
        "table": "friends"
    },
]

command_body = "INSERT INTO {} VALUES (\'{}\');"

def xml2dict(tabledef):
    dict2ret = {}
    for tableitem in tabledef:
        itemList = []
        conn = urlopen("http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/"+ tableitem["url"] + ".xml")
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

def dict2sql(dictIn, tdef=None):
    commands = []
    global command_body, tabledef
    if not tdef:
        tdef = tabledef
    for tablename in tdef:
        for element in dictIn[tablename["table"]]:
            elements_fields = "\',\'".join(element)
            commands.append(command_body.format(tablename["table"], elements_fields))
    return commands

def getCommands():
    global tabledef
    return dict2sql(xml2dict(tabledef))

def test():
    tabdef = [
        {"table": "tabela1"}, {"table": "tabela2"}
    ]

    test_dict = {
        "tabela1" : [
            ['elemento1_campo1', 'elemento1_campo2'],
            ['elemento2_campo1', 'elemento2_campo2']
        ],
        "tabela2" : [
            ['elemento1_campo1', 'elemento1_campo2', 'elemento1_campo3'],
            ['elemento2_campo1', 'elemento2_campo2', 'elemento2_campo3']
        ]
    }

    test_commands_result = [
        "INSERT INTO tabela1 VALUES ('elemento1_campo1','elemento1_campo2');",
        "INSERT INTO tabela1 VALUES ('elemento2_campo1','elemento2_campo2');",
        "INSERT INTO tabela2 VALUES ('elemento1_campo1','elemento1_campo2','elemento1_campo3');",
        "INSERT INTO tabela2 VALUES ('elemento2_campo1','elemento2_campo2','elemento2_campo3');"
    ]

    flag = True
    for index, command in enumerate(dict2sql(test_dict, tdef=tabdef)):
        if command != test_commands_result[index]:
            print(command, " is different from ", test_commands_result[index])
            flag = False
    if flag:
        print("dict2sql test passed")