from owlready2 import *

def addInstances(onto):
    # "AshKetchum" and "GaryOak", of type PokemonTrainer
    ash = onto.PokemonTrainer("AshKetchum")
    gary = onto.PokemonTrainer("GaryOak")

    # "pikachu1", "charmeleon1", "charizard1", "bulbasaur1", "wartortle1" of the respective types
    pikachu = onto.Pikachu()
    charmeleon = onto.Charmeleon()
    charizard = onto.Charizard()
    bulbasaur = onto.Bulbasaur()
    wartortle = onto.Wartortle()

    '''
    OBJECT PROPERTY ASSERTIONS
    '''

    pikachu.weakness = [bulbasaur]

    charmeleon.evolves = charizard

    # '''
    # DATA PROPERTY ASSERTIONS
    # '''

    # # pikachu1 power 300
    # pikachu.power = 300