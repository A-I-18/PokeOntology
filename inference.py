from owlready2 import *

def addInstances(onto):
    ai = onto.Organism("AI")
    ai.fullName = "Antonio"

    starter = onto.Pokemon("turtle")
    starter.height = 25
    starter.weight = 49

    legendary = onto.Pokemon("articuno")
    legendary.wingSpan = 527

    trainer = onto.Organism("trainerX")
    trainer.possess.append(onto.SuperPotion())

    pokeball = onto.PokemonItem("pb")
    pokeball.contain.append(onto.pikachu1)
