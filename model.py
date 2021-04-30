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
    Organism.equivalent_to.append(Human | Pokemon)

    # Humans can either be PokemonTrainer or SimpleHuman
    class PokemonTrainer(Human):
        pass
    class SimpleHuman(Human):
        pass
    AllDisjoint([PokemonTrainer, SimpleHuman])
    Human.equivalent_to.append(PokemonTrainer | SimpleHuman)

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
    Pokemon.equivalent_to.append(FirePokemon | WaterPokemon | GrassPokemon | PoisonPokemon | FlyingPokemon | ElectricPokemon | NormalPokemon)

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
    FirePokemon.equivalent_to.append(Charmeleon | Charizard | Moltres)
    WaterPokemon.equivalent_to.append(Vaporeon | Squirtle | Wartortle)
    GrassPokemon.equivalent_to.append(Bulbasaur | Ivysaur)
    PoisonPokemon.equivalent_to.append(Ivysaur)
    FlyingPokemon.equivalent_to.append(Charizard | Zapados | Moltres)
    ElectricPokemon.equivalent_to.append(Pikachu | Zapados | Jolteon)
    NormalPokemon.equivalent_to.append(Evee)

    '''
    PROPERTIES DEFINITION
    '''
            
    # A Pokemon of one kind may have a weakness to a Pokemon of another kind
    with onto:
        class weakness(ObjectProperty):
            domain    = [Pokemon]
            range     = [Pokemon]
        # WaterPokemon have weakness to ElectricPokemon or GrassPokemon
        WaterPokemon.is_a.append(weakness.only(ElectricPokemon))
        # FirePokemon have weakness to ElectricPokemon or WaterPokemon
        FirePokemon(Pokemon).is_a.append(weakness.only(WaterPokemon))
        # GrassPokemon have weakness to FirePokemon or FlyingPokemon
        GrassPokemon.is_a.append(weakness.only(FirePokemon | FlyingPokemon))
        # ElectricPokemon have weakness to GrassPokemon
        ElectricPokemon.is_a.append(weakness.only(GrassPokemon))
        # NormalPokemon have weakness to PoisonPokemon
        NormalPokemon.is_a.append(weakness.only(PoisonPokemon))

    # A Pokemon may evolve into another Pokemon
    with onto:
        class evolves(ObjectProperty, FunctionalProperty):
            domain    = [Pokemon]
            range     = [Pokemon]
        # Bulbasaur evolves to Ivysaur
        Bulbasaur.is_a.append(evolves.only(Ivysaur))
        # Charmeleon evolves to Charizard
        Charmeleon.is_a.append(evolves.only(Charizard))
        # Eevee can evolve to either Vaporeon or Jolteon
        Evee.is_a.append(evolves.only(Vaporeon | Jolteon))
        # Squirtle evolves to WarTortle
        Squirtle.is_a.append(evolves.only(Wartortle))

