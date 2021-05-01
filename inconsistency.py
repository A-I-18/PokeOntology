from owlready2 import *

def weakness(onto):
    onto.pikachu1.weakness = [onto.charmeleon1]

def evolves(onto):
    onto.charmeleon1.evolves = onto.pikachu1