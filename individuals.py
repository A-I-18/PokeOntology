from owlready2 import *

def addInstances(onto):
    '''
    INSTANCES INVOLVING ASH VS GARY
    '''
    
    ash = onto.PokemonTrainer("AshKetchum")
    gary = onto.PokemonTrainer("GaryOak")

    pikachu = onto.Pikachu("Ashs_Pikachu")
    wartortle = onto.Wartortle("Ashs_Wartortle")
    charizard = onto.Charizard("Ashs_Charizard")
    evee = onto.Evee("Garys_Evee")
    zapdos = onto.Zapdos("Garys_Zapdos")
    charizard2 = onto.Charizard("Garys_Charizard")

    pikachu.power = 105
    wartortle.power = 50
    charizard.power = 101
    evee.power = 65
    zapdos.power = 100
    charizard2.power = 95

    pb1 = onto.NormalPokeBall()
    pb2 = onto.NormalPokeBall()
    pb3 = onto.GreatPokeBall()
    pb4 = onto.GreatPokeBall()
    pb5 = onto.PokeBall()
    pb6 = onto.PokeBall()
    pb1.contain.append(pikachu)
    pb2.contain.append(wartortle)
    pb3.contain.append(charizard)
    pb4.contain.append(evee)
    pb5.contain.append(zapdos)
    pb6.contain.append(charizard2)
    ash.possess = [pb1, pb2, pb3]
    gary.possess = [pb4, pb5, pb6]

    battle = onto.PokemonBattle("Ash_vs_Gary")
    f1 = onto.PokemonFight("wartortle_vs_evee")
    f2 = onto.PokemonFight("pikachu_vs_zapdos")
    f3 = onto.PokemonFight("charizard_vs_charizard")
    ash.participateInBattle.append(battle)
    gary.participateInBattle.append(battle)
    wartortle.participateInFight.append(f1)
    evee.participateInFight.append(f1)
    pikachu.participateInFight.append(f2)
    zapdos.participateInFight.append(f2)
    charizard.participateInFight.append(f3)
    charizard2.participateInFight.append(f3)
    battle.involves = [f1, f2, f3]

    '''
    OTHER INSTANCES
    '''

    sh = onto.SimpleHuman("Ashs_Mother")

    bulbasaur = onto.Bulbasaur()
    ivysaur = onto.Ivysaur()
    charmeleon = onto.Charmeleon()
    charizard3 = onto.Charizard()
    pikachu2 = onto.Pikachu()
    zapdos2 = onto.Zapdos()
    evee2 = onto.Evee()
    evee3 = onto.Evee()
    vaporeon = onto.Vaporeon()
    jolteon = onto.Jolteon()
    moltres = onto.Moltres()
    squirtle = onto.Squirtle()
    wartortle2 = onto.Wartortle()

    bulbasaur.weakness = [charmeleon, moltres, zapdos2]
    ivysaur.weakness = [charmeleon, moltres, zapdos2]
    charmeleon.weakness = [vaporeon, squirtle, wartortle2]
    charizard3.weakness = [vaporeon, squirtle, wartortle2]
    pikachu2.weakness = [bulbasaur, ivysaur]
    zapdos2.weakness = [bulbasaur, ivysaur]
    evee2.weakness = [ivysaur]
    evee3.weakness = [ivysaur]
    vaporeon.weakness = [pikachu2, zapdos2]
    jolteon.weakness = [bulbasaur, ivysaur]
    moltres.weakness = [vaporeon, squirtle, wartortle2]
    squirtle.weakness = [pikachu2, zapdos2]
    wartortle2.weakness = [pikachu2, zapdos2]

    bulbasaur.evolves = ivysaur
    charmeleon.evolves = charizard3
    evee2.evolves = vaporeon
    evee3.evolves = jolteon
    squirtle.evolves = wartortle2
