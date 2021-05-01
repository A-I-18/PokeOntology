from owlready2 import *

def addInstances(onto):
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
    pb2 = onto.NormalPokeBall()
    pb3 = onto.GreatPokeBall()
    pb4 = onto.GreatPokeBall()

    battle = onto.PokemonBattle("Ash_vs_Gary")
    f1 = onto.PokemonFight("wartortle_vs_evee")
    f2 = onto.PokemonFight("pikachu_vs_zapdos")

    '''
    PROPERTY ASSERTIONS
    '''

    pikachu.weakness = [bulbasaur]
    charmeleon.evolves = charizard

    pb1.contain.append(pikachu)
    pb2.contain.append(wartortle)
    pb3.contain.append(evee)
    pb4.contain.append(zapdos)

    ash.possess = [pb1, pb2]
    gary.possess = [pb3, pb4, p1]

    ash.participateInBattle.append(battle)
    gary.participateInBattle.append(battle)

    wartortle.participateInFight.append(f1)
    evee.participateInFight.append(f1)
    pikachu.participateInFight.append(f2)
    zapdos.participateInFight.append(f2)

    battle.involves = [f1, f2]