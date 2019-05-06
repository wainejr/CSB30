from SPARQLWrapper import SPARQLWrapper, JSON

query = """PREFIX dbres: <http://dbpedia.org/resource/>

DESCRIBE dbres:United_States"""


def get_country_description():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()

print(get_country_description())