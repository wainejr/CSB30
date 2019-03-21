import ReadXMLFile as rxml
import xml.etree.ElementTree as ET  
import csv

PATH_FOLDER = './dadosMarvel/'
FILENAME_IN = './marvel_simplificado.xml'
FILENAME_HR = PATH_FOLDER + 'herois.csv'       # heroes
FILENAME_GHR = PATH_FOLDER + 'herois_good.csv' # good heroes
FILENAME_BHR = PATH_FOLDER + 'herois_bad.csv'  # bad heroes


def heroes_xml2csv(heroes, filename_csv):
	with open(filename_csv, 'w') as csv_file:
		spamwriter = csv.writer(csv_file, delimiter=',')	
		for i in range(0, len(heroes)):
			spamwriter.writerow(list(heroes[i].values()))
	return

def findAvgWeight(heroes):
	avgw = 0
	for hero in heroes:
		avgw += float(hero["weight_kg"])
	avgw /= len(heroes)
	return avgw

def findIMC(heroes, hero_name):
	for hero in heroes:
		if hero['name'] == hero_name:
			hero2save = hero
			break
	imc = float(hero2save["weight_kg"]) / (float(hero2save["height_m"]) ** 2)
	return imc

tree = ET.parse(FILENAME_IN)  
universe = tree.getroot()

heroes = []
for hero in universe:
    heroes.append(dict())
    heroes[-1]['id'] = hero.attrib['id'] # add id
    for elem in hero:
        heroes[-1][str(elem.tag)] = elem.text # add elements

good_heroes = [heroes[i] for i in range(0, len(heroes)) if heroes[i]['alignment'] == 'Good']
bad_heroes = [heroes[i] for i in range(0, len(heroes)) if heroes[i]['alignment'] == 'Bad']

total_h = len(heroes)
print("{}% good heroes / {}% bad heroes"
	.format(round(len(good_heroes)*100/total_h, 2), round(len(bad_heroes)*100/total_h, 2)))
print("Average weight:{}".format(round(findAvgWeight(heroes), 2)))
print("Hulk IMC:{}".format(findIMC(heroes, 'Hulk')))

heroes_xml2csv(heroes, FILENAME_HR)
heroes_xml2csv(good_heroes, FILENAME_GHR)
heroes_xml2csv(bad_heroes, FILENAME_BHR)

