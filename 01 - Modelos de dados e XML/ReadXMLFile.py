#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("marvel_simplificado.xml")

universe = DOMTree.documentElement

# Get all the heroes in the universe
heroes = universe.getElementsByTagName("hero")

# Print universe and detail of each hero.
if (__name__ == "__main__"):
	if universe.hasAttribute("name"):
	   print ("Root element : %s" % universe.getAttribute("name"))
	for hero in heroes:
	   print ("*****Hero*****") 
	   if hero.hasAttribute("id"):
	      print ("Id: %s" % hero.getAttribute("id"))

	   name = hero.getElementsByTagName('name')[0]
	   print ("Name: %s" % name.childNodes[0].data)
	 
