from owlready2 import *
import model
import individuals
import inference
import query
import visualize

print(
'''
>>> ONTOLOGY CREATION
'''
)

# Create new empty ontology specifing its IRI
onto = get_ontology("http://myonto.com/pokeOntology.owl")
print("Created empty ontology: {}".format(onto.base_iri))

print("\nCreating ontology model ...")
model.createModel(onto)
print("... Done!")

print("\nCreating ontology instances ...")
individuals.addInstances(onto)
inference.addInstances(onto)
query.addInstances(onto)
print("... Done!")

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
print("\nOntology saved in file pokeOntology.owl")

print("\n", end="")

'''
PRINT MODEL
'''

visualize.printModel(onto)
print("\n", end="")


print(
'''
>>> REASONING
'''
)

# Create new empty ontology specifing its IRI
inferred = get_ontology("http://myonto.com/pokeOntologyInferred.owl")
with inferred:
    # Running HermiT Reasoner
    sync_reasoner([onto], infer_property_values = True)
    # sync_reasoner_pellet()

print("Inconsistent classes: {}".format(list(onto.inconsistent_classes())))

'''
SAVE OWL FILES
'''

inferred.save(file="pokeOntologyInferred.owl", format="ntriples")
print("\nInferred ontology saved in file pokeOntologyInferred.owl\n")

print(
'''
>>> QUERYING ONTOLOGY
'''
)

query.executeQuery(onto)
