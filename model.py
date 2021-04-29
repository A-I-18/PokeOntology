from owlready2 import *

def createModel(onto):
    '''
    CLASSES DEFINITION
    '''

    # There are two main kinds of Organism: Human and Pokemon
    class Organism(Thing):
        namespace = onto
    class Human(Organism):
        pass
    class Pokemon(Organism):
        pass
    AllDisjoint([Human, Pokemon])

    # Humans can either be PokemonTrainer or SimpleHuman
    class PokemonTrainer(Human):
        pass
    class SimpleHuman(Human):
        pass
    AllDisjoint([PokemonTrainer, SimpleHuman])

    # There are different kinds of Pokemon, based on their type:
    # FirePokemon, WaterPokemon, GrassPokemon, PoisonPokemon, FlyingPokemon, ElectricPokemon and NormalPokemon
    class FirePokemon(Pokemon):
        pass
    class WaterPokemon(Pokemon):
        pass
    class GrassPokemon(Pokemon):
        pass
    class PoisonPokemon(Pokemon):
        pass
    class FlyingPokemon(Pokemon):
        pass
    class ElectricPokemon(Pokemon):
        pass
    class NormalPokemon(Pokemon):
        pass

    # Pokemon species are under one or a combination of Pokemon types
    class Bulbasaur(GrassPokemon):
        pass
    class Ivysaur(GrassPokemon, PoisonPokemon):
        pass
    class Charmeleon(FirePokemon):
        pass
    class Charizard(FirePokemon, FlyingPokemon):
        pass
    class Pikachu(ElectricPokemon):
        pass
    class Zapados(ElectricPokemon, FlyingPokemon):
        pass
    class Evee(NormalPokemon):
        pass
    class Vaporeon(WaterPokemon):
        pass
    class Jolteon(ElectricPokemon):
        pass
    class Moltres(FirePokemon, FlyingPokemon):
        pass
    class Squirtle(WaterPokemon):
        pass
    class Wartortle(WaterPokemon):
        pass
    AllDisjoint([Bulbasaur, Ivysaur, Charmeleon, Charizard, Pikachu, Zapados, Evee, Vaporeon, Jolteon, Moltres, Squirtle, Wartortle])

