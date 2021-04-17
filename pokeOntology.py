from owlready2 import *

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/pokeOntology.owl")

import model
model.createModel(onto)

onto.save(file="pokeOntology.owl", format="ntriples")