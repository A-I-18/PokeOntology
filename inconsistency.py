from owlready2 import *

def weakness(onto):
    onto.pikachu1.weakness = [onto.charmeleon1]

def evolves(onto):
    onto.charmeleon1.evolves = onto.pikachu1

def region(onto):
    onto.pikachu1.region = "latina"

def feature(onto):
    onto.charizard1.feature = "dragon"

def wingSpan(onto):
    onto.zapdos1.wingSpan = 499

def heightAndWeight(onto):
    onto.bulbasaur1.height = 10
    onto.bulbasaur1.weight = 55

def height(onto):
    onto.evee1.height = 202

def name(onto):
    #TODO
    pass