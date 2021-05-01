from owlready2 import *

def addInstances(onto):
    ai = onto.Organism("AI")
    ai.fullName = "Antonio"

    ash = onto.PokemonTrainer("AshKetchum")
    gary = onto.PokemonTrainer("GaryOak")

    pikachu = onto.Pikachu()
    charmeleon = onto.Charmeleon()
    charizard = onto.Charizard()
    bulbasaur = onto.Bulbasaur()
    wartortle = onto.Wartortle()
    zapdos = onto.Zapdos()
    evee = onto.Evee()

    p1 = onto.NormalPotion()
    pb1 = onto.NormalPokeBall()
    pb2 = onto.GreatPokeBall()

    '''
    OBJECT PROPERTY ASSERTIONS
    '''

    pikachu.weakness = [bulbasaur]

    charmeleon.evolves = charizard

    ash.possess.append(pb1)
    gary.possess.append(p1)
    gary.possess.append(pb2)

    # '''
    # DATA PROPERTY ASSERTIONS
    # '''

    # # pikachu1 power 300
    # pikachu.power = 300