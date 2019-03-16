import ReadXMLFile as rxml
import xml.etree.ElementTree as ET  
import csv

PATH_FOLDER = './dadosMarvel/'
FILENAME_HR = PATH_FOLDER + 'herois.csv'	   # heroes
FILENAME_GHR = PATH_FOLDER + 'herois_good.csv' # good heroes
FILENAME_BHR = PATH_FOLDER + 'herois_bad.csv'  # bad heroes


def heroes_xml2csv(heroes, filename_csv):
	with open(filename_csv, 'w') as csv_file:
		spamwriter = csv.writer(csv_file, delimiter=',')	
		for hero in heroes:
			spamwriter.writerow(hero)
	return

tree = ET.parse('marvel_simplificado.xml')  
universe = tree.getroot()

heroes = list(list())
for hero in universe:
	heroes.append(list())
	heroes[-1].append(hero.attrib['id']) # add id
	for elem in hero:
		heroes[-1].append(elem.text) # add atribute		

heroes_xml2csv(heroes, FILENAME_HR)
