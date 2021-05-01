from owlready2 import *

'''
CREATE ONTOLOGY
'''

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/pokeOntology.owl")

import model
model.createModel(onto)

import individuals
individuals.addInstances(onto)

# https://owlready2.readthedocs.io/en/latest/disjoint.html?highlight=close_world
# close_world(onto)

print("\n")

'''
INTRODUCE INCONSISTENCIES
'''

import inconsistency
# inconsistency.weakness(onto)
# inconsistency.evolves(onto)
# inconsistency.region(onto)
# inconsistency.feature(onto)
# inconsistency.wingSpan(onto)
# inconsistency.heightAndWeight(onto)
# inconsistency.height(onto)
# inconsistency.name(onto)

'''
REASONING
'''

# Create new empty ontology specifing its IRI
inferred = get_ontology("http://myonto.com/pokeOntologyInferred.owl")
with inferred:
    # Running HermiT Reasoner
    sync_reasoner([onto], infer_property_values = True)
    # sync_reasoner_pellet()

print("Inconsistent classes: ")
print(list(onto.inconsistent_classes()))

'''
SAVE OWL FILES
'''

onto.save(file="pokeOntology.owl", format="ntriples")
inferred.save(file="pokeOntologyInferred.owl", format="ntriples")

print("\n")
