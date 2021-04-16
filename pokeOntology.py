from owlready2 import *

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/pokeOntology.owl")

# Create classes
class Organism(Thing):
    namespace = onto

print (Organism.iri)