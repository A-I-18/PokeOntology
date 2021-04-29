from owlready2 import *

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/pokeOntology.owl")

import model
model.createModel(onto)

onto.save(file="pokeOntology.owl", format="ntriples")

import individuals
individuals.addInstances(onto)

# https://owlready2.readthedocs.io/en/latest/disjoint.html?highlight=close_world
# close_world(onto)

print("\n")

# Running HermiT Reasoner
# Create new empty ontology specifing its IRI
inferred = get_ontology("http://myonto.com/pokeOntologyInferred.owl")
with inferred:
    sync_reasoner(infer_property_values = True)

onto.save(file="pokeOntology.owl", format="ntriples")
inferred.save(file="pokeOntologyInferred.owl", format="ntriples")

print("\n")

# Debugging
print("Inconsistent classes: ")
print(list(default_world.inconsistent_classes()))
