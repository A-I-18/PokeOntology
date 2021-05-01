from owlready2 import *

def addInstances(onto):
    starter = onto.Pokemon("turtle")
    starter.height = 25
    starter.weight = 49

    legendary = onto.Pokemon("articuno")
    legendary.wingSpan = 527
