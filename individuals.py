from owlready2 import *

def addInstances(onto):
    ash = onto.PokemonTrainer("AshKetchum")
    gary = onto.PokemonTrainer("GaryOak")

    pikachu = onto.Pikachu()
    charmeleon = onto.Charmeleon()
    charizard = onto.Charizard()
    charizard2 = onto.Charizard()
    bulbasaur = onto.Bulbasaur()
    wartortle = onto.Wartortle()
    zapdos = onto.Zapdos()
    evee = onto.Evee()

    p1 = onto.NormalPotion()

    pb1 = onto.NormalPokeBall()
    pb2 = onto.NormalPokeBall()
    pb3 = onto.GreatPokeBall()
    pb4 = onto.GreatPokeBall()
    pb5 = onto.PokeBall()
    pb6 = onto.PokeBall()

    battle = onto.PokemonBattle("Ash_vs_Gary")
    f1 = onto.PokemonFight("wartortle_vs_evee")
    f2 = onto.PokemonFight("pikachu_vs_zapdos")
    f3 = onto.PokemonFight("charizard_vs_charizard")

    '''
    PROPERTY ASSERTIONS
    '''

    pikachu.weakness = [bulbasaur]
    charmeleon.evolves = charizard

    pb1.contain.append(pikachu)
    pb2.contain.append(wartortle)
    pb3.contain.append(charizard)
    pb4.contain.append(evee)
    pb5.contain.append(zapdos)
    pb6.contain.append(charizard2)

    ash.possess = [pb1, pb2, pb3]
    gary.possess = [pb4, pb5, pb6]

    ash.participateInBattle.append(battle)
    gary.participateInBattle.append(battle)

    wartortle.participateInFight.append(f1)
    evee.participateInFight.append(f1)
    pikachu.participateInFight.append(f2)
    zapdos.participateInFight.append(f2)
    charizard.participateInFight.append(f3)
    charizard2.participateInFight.append(f3)

    wartortle.power = 50
    evee.power = 65
    pikachu.power = 105
    zapdos.power = 100
    charizard.power = 101
    charizard2.power = 95

    battle.involves = [f1, f2, f3]