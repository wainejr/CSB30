# Python
import requests
 
data = requests.get('http://dbpedia.org/data/The_Strokes.json').json()
band = data['http://dbpedia.org/resource/The_Strokes']
 
for key in sorted(band): print(key)