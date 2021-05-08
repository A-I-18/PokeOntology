from owlready2 import *
import model
import individuals
import inference
import query
import visualize

'''
CREATE ONTOLOGY
'''

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/pokeOntology.owl")

model.createModel(onto)

individuals.addInstances(onto)
inference.addInstances(onto)
query.addInstances(onto)

# https://owlready2.readthedocs.io/en/latest/disjoint.html?highlight=close_world
# close_world(onto)

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
# inconsistency.skill(onto)
# inconsistency.pokeball(onto)

'''
SAVE OWL FILE
'''

onto.save(file="pokeOntology.owl", format="ntriples")

'''
PRINT MODEL
'''

visualize.printModel(onto)
print("\n")


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

inferred.save(file="pokeOntologyInferred.owl", format="ntriples")

print("\n")

'''
QUERYING ONTOLOGY
'''

query.executeQuery(onto)
