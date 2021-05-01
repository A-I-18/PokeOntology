from owlready2 import *

def createModel(onto):
    '''
    BASIC CLASSES DEFINITION
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
    class Zapdos(ElectricPokemon, FlyingPokemon):
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
    AllDisjoint([Bulbasaur, Ivysaur, Charmeleon, Charizard, Pikachu, Zapdos, Evee, Vaporeon, Jolteon, Moltres, Squirtle, Wartortle])
    FirePokemon.equivalent_to.append(Charmeleon | Charizard | Moltres)
    WaterPokemon.equivalent_to.append(Vaporeon | Squirtle | Wartortle)
    GrassPokemon.equivalent_to.append(Bulbasaur | Ivysaur)
    PoisonPokemon.equivalent_to.append(Ivysaur)
    FlyingPokemon.equivalent_to.append(Charizard | Zapdos | Moltres)
    ElectricPokemon.equivalent_to.append(Pikachu | Zapdos | Jolteon)
    NormalPokemon.equivalent_to.append(Evee)

    '''
    BASIC PROPERTIES DEFINITION
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

    # Data-type properties
    with onto:
        # demographic: height, weight, age (numerical), region (string)
        class demographic(DataProperty):
            pass
        class height(demographic, FunctionalProperty):
            range = [float]
        class weight(demographic, FunctionalProperty):
            range = [float]
        class age(demographic, FunctionalProperty):
            range = [int]
        # The region attribute is restricted to take values only from the following array ["kanto", "johto"]
        class region(demographic, FunctionalProperty):
            range = [OneOf(["kanto", "johto"])]
        
        # characteristic: power, heart, wingSpan (numerical), feature (string)
        class characteristic(DataProperty):
            pass
        class power(characteristic, FunctionalProperty):
            range = [float]
        class heart(characteristic, FunctionalProperty):
            range = [float]
        class wingSpan(characteristic, FunctionalProperty):
            domain = [FlyingPokemon]
            range = [float]
        # The feature attribute is restricted to take values only from the following array ["seed", "flower", "mammal", "reptile", "bird", "rodent"]
        class feature(characteristic, FunctionalProperty):
            range = [OneOf(["seed", "flower", "mammal", "reptile", "bird", "rodent"])]
        
        # name, description
        class fullName(DataProperty, FunctionalProperty):
            range = [str]
        class description(DataProperty):
            range = [str]

        # A Pokemon has the attributes height, weight, power, heart, feature, region
        Pokemon.is_a.append(height.exactly(1) & weight.exactly(1) & power.exactly(1) & heart.exactly(1) & feature.exactly(1) & region.exactly(1))
        # A FlyingPokemon has an additional attribute: wingSpan
        FlyingPokemon.is_a.append(wingSpan.exactly(1))
        # Moltres and Zapdos have a property restriction on wingSpan to be > 500
        Moltres.is_a.append(wingSpan.only(ConstrainedDatatype(float, min_exclusive = 500)))
        Zapdos.is_a.append(wingSpan.only(ConstrainedDatatype(float, min_exclusive = 500)))
        # Bulbasaur and Squirtle have a restriction on height < 50 and weight < 50
        Bulbasaur.is_a.append(height.only(ConstrainedDatatype(float, max_exclusive = 50)) & weight.only(ConstrainedDatatype(float, max_exclusive = 50)))
        Squirtle.is_a.append(height.only(ConstrainedDatatype(float, max_exclusive = 50)) & weight.only(ConstrainedDatatype(float, max_exclusive = 50)))
        # Eevee has a property restriction on height < 100
        Evee.is_a.append(height.only(ConstrainedDatatype(float, max_exclusive = 100)))

        # A PokemonTrainer has the following attributes: height, weight, age
        PokemonTrainer.is_a.append(height.exactly(1) & weight.exactly(1) & age.exactly(1))

        # All Human have name
        Human.equivalent_to.append(fullName.some(str))

    '''
    MORE MODEL DEFINITION
    '''

    # A StarterPokemon is a Pokemon with height < 100 and weight < 100
    class StarterPokemon(Pokemon):
        equivalent_to = [Pokemon & height.only(ConstrainedDatatype(float, max_exclusive = 100)) & weight.only(ConstrainedDatatype(float, max_exclusive = 100))]
    # A LegendaryPokemon is a FlyingPokemon with wingSpan > 300
    class LegendaryPokemon(FlyingPokemon):
        equivalent_to = [FlyingPokemon & wingSpan.only(ConstrainedDatatype(float, min_exclusive = 300))]

    class Skill(Thing):
        namespace = onto
    electricShock = Skill("ElectricShock")
    electricField = Skill("ElectricField")
    shield = Skill("Shield")
    whip = Skill("Whip")
    harden = Skill("Harden")
    sporeRelease = Skill("SporeRelease")
    fireBall = Skill("FireBall")
    waterGun = Skill("WaterGun")
    Skill.equivalent_to.append(OneOf([electricShock, electricField, shield, whip, harden, sporeRelease, fireBall, waterGun]))
    with onto:
        class hasSkill(ObjectProperty):
            domain = [Pokemon]
            range = [Skill]
        ElectricPokemon.is_a.append(hasSkill.value(electricShock) & hasSkill.value(electricField))
        PoisonPokemon.is_a.append(hasSkill.value(sporeRelease))
        FirePokemon.is_a.append(hasSkill.value(fireBall))
        WaterPokemon.is_a.append(hasSkill.value(waterGun) & hasSkill.value(harden))
        FlyingPokemon.is_a.append(hasSkill.value(shield))
        GrassPokemon.is_a.append(hasSkill.value(whip))
        NormalPokemon.is_a.append(hasSkill.value(shield))
        
    # There exist different PokemonItem: Potion and PokeBall
    class PokemonItem(Thing):
        namespace = onto
    class Potion(PokemonItem):
        pass
    class PokeBall(PokemonItem):
        pass
    AllDisjoint([Potion, PokeBall])
    PokemonItem.equivalent_to.append(Potion | PokeBall)
    # Potion can either be NormalPotion or SuperPotion
    class NormalPotion(Potion):
        pass
    class SuperPotion(Potion):
        pass
    AllDisjoint([NormalPotion, SuperPotion])
    Potion.equivalent_to.append(NormalPotion | SuperPotion)
    # PokeBall can either be NormalPokeBall or GreatPokeBall
    class NormalPokeBall(PokeBall):
        pass
    class GreatPokeBall(PokeBall):
        pass
    AllDisjoint([NormalPokeBall, GreatPokeBall])
    PokeBall.equivalent_to.append(NormalPokeBall | GreatPokeBall)

    with onto:
        # A PokemonTrainer may possess some PokemonItem
        class possess(ObjectProperty):
            domain = [PokemonTrainer]
            range = [PokemonItem]
        # A PokeBall can contain at maximum 1 Pokemon only
        class contain(ObjectProperty):
            domain = [PokeBall]
            range = [Pokemon]
        PokeBall.is_a.append(contain.max(1))

    # A PokemonBattle has the following attributes: description, region
    class PokemonBattle(Thing):
        namespace = onto
    PokemonBattle.is_a.append(description.exactly(1) & region.exactly(1))

    with onto:
        # A PokemonTrainer can participate in a PokemonBattle
        class participateInBattle(ObjectProperty):
            domain = [PokemonTrainer]
            range = [PokemonBattle]

    # A PokemonBattle involves some PokemonFight
    class PokemonFight(Thing):
        namespace = onto
    with onto:
        class involves(ObjectProperty):
            domain = [PokemonBattle]
            range = [PokemonFight]
        PokemonBattle.is_a.append(involves.some(PokemonFight))

    with onto:
        # A Pokemon can participate in some PokemonFight
        class participateInFight(ObjectProperty):
            domain = [Pokemon]
            range = [PokemonFight]
