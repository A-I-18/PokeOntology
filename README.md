<p align="center">
  <img width=260px height=260px src="/PokeOntology-Logo.png" alt="Project logo">
</p>

---

<p align="center">
  Working with Knowledge Representation with owlready2 python framework
  <br /> 
</p>

# 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
	- [Built Using](#built)
	- [Prerequisites](#prerequisites)
	- [Run](#run)
- [Project Structure](#structure)
- [Usage](#usage)
	1. [Ontology Creation](#onto_creation)
		- [Ontology Classes](#onto_classes)
		- [Ontology Disjointness](#onto_disjoint)
		- [Ontology Object Properties](#onto_oprops)
		- [Ontology Data Properties](#onto_dprops)
	2. [Ontology Inconsistencies](#onto_incons)
	3. [Reasoning](#reasoning)
	4. [Querying Ontology](#query) 
- [Author](#author)
- [Acknowledgments](#acknowledgement)

# About <a name = "about"></a>

Homework project as part of the [Knowledge Representation and Semantic Technologies](http://www.diag.uniroma1.it//rosati/krst/) course of the master degree in "Engineering in Computer Science" of "Sapienza, Università di Roma", A.Y.2020/21.

The aim of the project is to realize a practical exercise of Knowledge Representation.

The project consists in a Python application, exploiting the Owlready2 framework, which manages from skratch an OWL ontology. The Pokemon fictional universe is used as context.

# Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.

## Built Using <a name = "built"></a>

- [Python3](https://www.python.org/) - Programming Language
- [Owlready2](https://pypi.org/project/Owlready2/) - A package for ontology-oriented programming in Python: load OWL 2.0 ontologies as Python objects, modify them, save them, and perform reasoning via HermiT. Includes an optimized RDF quadstore. [Documentation](https://owlready2.readthedocs.io/en/latest/index.html) | [Project Repository](https://bitbucket.org/jibalamy/owlready2/src/master/)

## Prerequisites <a name = "prerequisites"></a>

What things you need to install the software and how to install them.

For running the application, essentially, only [python3](https://www.python.org/downloads/) and Owlready2 framework are needed

```
pip install Owlready2
```

## Run <a name = "run"></a>

In the root of the project:

```
python pokeOntology.py
```
# Project Structure <a name="structure"></a>

The entry point of the application is the script [pokeOntology.py](/pokeOntology.py), which exploits the following modules:
- [model.py](/model.py), it creates the ontology, defining its classes, its properties and all the axioms of the knowledge-base
- [individuals.py](/individuals.py), it adds basic individuals to the ontology, respecting its semantics
- [inference.py](/inference.py), it adds individuals to the ontolgy following the criterion of defining instances whose knowledge about should be enanched by the reasoner
- [query.py](/query.py), it adds individuals to the ontology following the criterion of defining instances that sholud be retrived by specific queries and it executes SPARQL queries read from the [SPARQL_queries.rq](/SPARQL_queries.rq) file
- [inconsistency.py](/inconsistency.py), it adds individuals to the ontology following the criterion of defining instances that sholud cause the model to become inconsistent
- [visualize.py](/visualize.py), it prints the model having care of showing all the aspects of the modeled knowledge

# Usage <a name="usage"></a>

The execution of the program follows these steps

## 1. Ontology Creation <a name = "onto_creation"></a>

The OWL 2 ontology identified by the fictional IRI http://myonto.com/pokeOntology.owl is created and saved in the file [pokeOntology.owl](/pokeOntology.py), adopting NTriples format.

### Ontology Classes <a name = "onto_classes"></a>
#### Class: pokeOntology.Organism
	equivalent_to = [pokeOntology.Human | pokeOntology.Pokemon]
	is_a = [owl.Thing]
	Subclasses:
		- pokeOntology.Human
		- pokeOntology.Pokemon
	Individuals:
		- pokeOntology.AI
		- pokeOntology.trainerX
		- pokeOntology.bpt1
		- pokeOntology.turtle
		- pokeOntology.articuno
		- pokeOntology.sp
		- pokeOntology.pokemon1
		- pokeOntology.pokemon2
		- pokeOntology.AshKetchum
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/Ash_Ketchum']
		- pokeOntology.GaryOak
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/Gary_Oak']
		- pokeOntology.victor
		- pokeOntology.Ashs_Mother
		- pokeOntology.charmeleon1
		- pokeOntology.Ashs_Charizard
		- pokeOntology.Garys_Charizard
		- pokeOntology.charizard1
		- pokeOntology.moltres1
		- pokeOntology.vaporeon1
		- pokeOntology.squirtle1
		- pokeOntology.Ashs_Wartortle
		- pokeOntology.wartortle1
		- pokeOntology.bulbasaur1
		- pokeOntology.ivysaur1
		- pokeOntology.Garys_Zapdos
		- pokeOntology.zapdos1
		- pokeOntology.Ashs_Pikachu
		- pokeOntology.pikachu1
		- pokeOntology.jolteon1
		- pokeOntology.Garys_Evee
		- pokeOntology.evee1
		- pokeOntology.evee2
#### Class: pokeOntology.Human
	equivalent_to = [pokeOntology.PokemonTrainer | pokeOntology.SimpleHuman, pokeOntology.fullName.some(<class 'str'>)]
	is_a = [pokeOntology.Organism]
	Subclasses:
		- pokeOntology.PokemonTrainer
		- pokeOntology.SimpleHuman
	Individuals:
		- pokeOntology.bpt1
		- pokeOntology.AshKetchum
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/Ash_Ketchum']
		- pokeOntology.GaryOak
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/Gary_Oak']
		- pokeOntology.victor
		- pokeOntology.Ashs_Mother
#### Class: pokeOntology.Pokemon
	altLabel = ['Pocket Monster']
	comment = ['Fantasy creatures in the Pokemon world, drawn as if mutated from real-world creatures']
	equivalent_to = [pokeOntology.FirePokemon | pokeOntology.WaterPokemon | pokeOntology.GrassPokemon | pokeOntology.PoisonPokemon | pokeOntology.FlyingPokemon | pokeOntology.ElectricPokemon | pokeOntology.NormalPokemon]
	is_a = [pokeOntology.Organism, pokeOntology.height.exactly(1, owl.Thing) & pokeOntology.weight.exactly(1, owl.Thing) & pokeOntology.power.exactly(1, owl.Thing) & pokeOntology.heart.exactly(1, owl.Thing) & pokeOntology.feature.exactly(1, owl.Thing) & pokeOntology.region.exactly(1, owl.Thing)]
	Subclasses:
		- pokeOntology.FirePokemon
		- pokeOntology.WaterPokemon
		- pokeOntology.GrassPokemon
		- pokeOntology.PoisonPokemon
		- pokeOntology.FlyingPokemon
		- pokeOntology.ElectricPokemon
		- pokeOntology.NormalPokemon
		- pokeOntology.StarterPokemon
	Individuals:
		- pokeOntology.turtle
		- pokeOntology.articuno
		- pokeOntology.sp
		- pokeOntology.pokemon1
		- pokeOntology.pokemon2
		- pokeOntology.charmeleon1
		- pokeOntology.Ashs_Charizard
		- pokeOntology.Garys_Charizard
		- pokeOntology.charizard1
		- pokeOntology.moltres1
		- pokeOntology.vaporeon1
		- pokeOntology.squirtle1
		- pokeOntology.Ashs_Wartortle
		- pokeOntology.wartortle1
		- pokeOntology.bulbasaur1
		- pokeOntology.ivysaur1
		- pokeOntology.Garys_Zapdos
		- pokeOntology.zapdos1
		- pokeOntology.Ashs_Pikachu
		- pokeOntology.pikachu1
		- pokeOntology.jolteon1
		- pokeOntology.Garys_Evee
		- pokeOntology.evee1
		- pokeOntology.evee2
#### Class: pokeOntology.PokemonTrainer
	altLabel = ['Pokemon Battle player']
	comment = ['Trains Pokemon to fight battles with other Trainers, and capture other Pokemon']
	is_a = [pokeOntology.Human, pokeOntology.height.exactly(1, owl.Thing) & pokeOntology.weight.exactly(1, owl.Thing) & pokeOntology.age.exactly(1, owl.Thing)]
	Subclasses:
	Individuals:
		- pokeOntology.AshKetchum
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/Ash_Ketchum']
		- pokeOntology.GaryOak
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/Gary_Oak']
		- pokeOntology.victor
#### Class: pokeOntology.SimpleHuman
	is_a = [pokeOntology.Human]
	Subclasses:
	Individuals:
		- pokeOntology.Ashs_Mother
#### Class: pokeOntology.FirePokemon
	equivalent_to = [pokeOntology.Charmeleon | pokeOntology.Charizard | pokeOntology.Moltres]
	is_a = [pokeOntology.Pokemon, pokeOntology.weakness.only(pokeOntology.WaterPokemon), pokeOntology.hasSkill.value(pokeOntology.FireBall)]
	Subclasses:
		- pokeOntology.Charmeleon
		- pokeOntology.Charizard
		- pokeOntology.Moltres
	Individuals:
		- pokeOntology.charmeleon1
		- pokeOntology.Ashs_Charizard
		- pokeOntology.Garys_Charizard
		- pokeOntology.charizard1
		- pokeOntology.moltres1
#### Class: pokeOntology.WaterPokemon
	equivalent_to = [pokeOntology.Vaporeon | pokeOntology.Squirtle | pokeOntology.Wartortle]
	is_a = [pokeOntology.Pokemon, pokeOntology.weakness.only(pokeOntology.ElectricPokemon), pokeOntology.hasSkill.value(pokeOntology.WaterGun) & pokeOntology.hasSkill.value(pokeOntology.Harden)]
	Subclasses:
		- pokeOntology.Vaporeon
		- pokeOntology.Squirtle
		- pokeOntology.Wartortle
	Individuals:
		- pokeOntology.vaporeon1
		- pokeOntology.squirtle1
		- pokeOntology.Ashs_Wartortle
		- pokeOntology.wartortle1
#### Class: pokeOntology.GrassPokemon
	equivalent_to = [pokeOntology.Bulbasaur | pokeOntology.Ivysaur]
	is_a = [pokeOntology.Pokemon, pokeOntology.weakness.only(pokeOntology.FirePokemon | pokeOntology.FlyingPokemon), pokeOntology.hasSkill.value(pokeOntology.Whip)]
	Subclasses:
		- pokeOntology.Bulbasaur
		- pokeOntology.Ivysaur
	Individuals:
		- pokeOntology.bulbasaur1
		- pokeOntology.ivysaur1
#### Class: pokeOntology.PoisonPokemon
	equivalent_to = [pokeOntology.Ivysaur]
	is_a = [pokeOntology.Pokemon, pokeOntology.hasSkill.value(pokeOntology.SporeRelease)]
	Subclasses:
		- pokeOntology.Ivysaur
	Individuals:
		- pokeOntology.ivysaur1
#### Class: pokeOntology.FlyingPokemon
	equivalent_to = [pokeOntology.Charizard | pokeOntology.Zapdos | pokeOntology.Moltres]
	is_a = [pokeOntology.Pokemon, pokeOntology.wingSpan.exactly(1, owl.Thing), pokeOntology.hasSkill.value(pokeOntology.Shield)]
	Subclasses:
		- pokeOntology.Charizard
		- pokeOntology.Zapdos
		- pokeOntology.Moltres
		- pokeOntology.LegendaryPokemon
	Individuals:
		- pokeOntology.Ashs_Charizard
		- pokeOntology.Garys_Charizard
		- pokeOntology.charizard1
		- pokeOntology.Garys_Zapdos
		- pokeOntology.zapdos1
		- pokeOntology.moltres1
#### Class: pokeOntology.ElectricPokemon
	equivalent_to = [pokeOntology.Pikachu | pokeOntology.Zapdos | pokeOntology.Jolteon]
	is_a = [pokeOntology.Pokemon, pokeOntology.weakness.only(pokeOntology.GrassPokemon), pokeOntology.hasSkill.value(pokeOntology.ElectricShock) & pokeOntology.hasSkill.value(pokeOntology.ElectricField)]
	Subclasses:
		- pokeOntology.Pikachu
		- pokeOntology.Zapdos
		- pokeOntology.Jolteon
	Individuals:
		- pokeOntology.Ashs_Pikachu
		- pokeOntology.pikachu1
		- pokeOntology.Garys_Zapdos
		- pokeOntology.zapdos1
		- pokeOntology.jolteon1
#### Class: pokeOntology.NormalPokemon
	equivalent_to = [pokeOntology.Evee]
	is_a = [pokeOntology.Pokemon, pokeOntology.weakness.only(pokeOntology.PoisonPokemon), pokeOntology.hasSkill.value(pokeOntology.Shield)]
	Subclasses:
		- pokeOntology.Evee
	Individuals:
		- pokeOntology.Garys_Evee
		- pokeOntology.evee1
		- pokeOntology.evee2
#### Class: pokeOntology.Bulbasaur
	is_a = [pokeOntology.GrassPokemon, pokeOntology.evolves.only(pokeOntology.Ivysaur), pokeOntology.height.only(ConstrainedDatatype(float, max_exclusive = 50)) & pokeOntology.weight.only(ConstrainedDatatype(float, max_exclusive = 50))]
	Subclasses:
	Individuals:
		- pokeOntology.bulbasaur1
#### Class: pokeOntology.Ivysaur
	is_a = [pokeOntology.GrassPokemon, pokeOntology.PoisonPokemon]
	Subclasses:
	Individuals:
		- pokeOntology.ivysaur1
#### Class: pokeOntology.Charmeleon
	is_a = [pokeOntology.FirePokemon, pokeOntology.evolves.only(pokeOntology.Charizard)]
	Subclasses:
	Individuals:
		- pokeOntology.charmeleon1
#### Class: pokeOntology.Charizard
	is_a = [pokeOntology.FirePokemon, pokeOntology.FlyingPokemon]
	Subclasses:
	Individuals:
		- pokeOntology.Ashs_Charizard
		- pokeOntology.Garys_Charizard
		- pokeOntology.charizard1
#### Class: pokeOntology.Pikachu
	is_a = [pokeOntology.ElectricPokemon]
	Subclasses:
	Individuals:
		- pokeOntology.Ashs_Pikachu
		- pokeOntology.pikachu1
#### Class: pokeOntology.Zapdos
	is_a = [pokeOntology.ElectricPokemon, pokeOntology.FlyingPokemon, pokeOntology.wingSpan.only(ConstrainedDatatype(float, min_exclusive = 500))]
	Subclasses:
	Individuals:
		- pokeOntology.Garys_Zapdos
		- pokeOntology.zapdos1
#### Class: pokeOntology.Evee
	is_a = [pokeOntology.NormalPokemon, pokeOntology.evolves.only(pokeOntology.Vaporeon | pokeOntology.Jolteon), pokeOntology.height.only(ConstrainedDatatype(float, max_exclusive = 100))]
	Subclasses:
	Individuals:
		- pokeOntology.Garys_Evee
		- pokeOntology.evee1
		- pokeOntology.evee2
#### Class: pokeOntology.Vaporeon
	is_a = [pokeOntology.WaterPokemon]
	Subclasses:
	Individuals:
		- pokeOntology.vaporeon1
#### Class: pokeOntology.Jolteon
	is_a = [pokeOntology.ElectricPokemon]
	Subclasses:
	Individuals:
		- pokeOntology.jolteon1
#### Class: pokeOntology.Moltres
	is_a = [pokeOntology.FirePokemon, pokeOntology.FlyingPokemon, pokeOntology.wingSpan.only(ConstrainedDatatype(float, min_exclusive = 500))]
	Subclasses:
	Individuals:
		- pokeOntology.moltres1
#### Class: pokeOntology.Squirtle
	is_a = [pokeOntology.WaterPokemon, pokeOntology.evolves.only(pokeOntology.Wartortle), pokeOntology.height.only(ConstrainedDatatype(float, max_exclusive = 50)) & pokeOntology.weight.only(ConstrainedDatatype(float, max_exclusive = 50))]
	Subclasses:
	Individuals:
		- pokeOntology.squirtle1
#### Class: pokeOntology.Wartortle
	is_a = [pokeOntology.WaterPokemon]
	Subclasses:
	Individuals:
		- pokeOntology.Ashs_Wartortle
		- pokeOntology.wartortle1
#### Class: pokeOntology.StarterPokemon
	equivalent_to = [pokeOntology.Pokemon & pokeOntology.height.only(ConstrainedDatatype(float, max_exclusive = 100)) & pokeOntology.weight.only(ConstrainedDatatype(float, max_exclusive = 100))]
	is_a = [pokeOntology.Pokemon]
	Subclasses:
	Individuals:
#### Class: pokeOntology.LegendaryPokemon
	equivalent_to = [pokeOntology.FlyingPokemon & pokeOntology.wingSpan.only(ConstrainedDatatype(float, min_exclusive = 300))]
	is_a = [pokeOntology.FlyingPokemon]
	Subclasses:
	Individuals:
#### Class: pokeOntology.Skill
	equivalent_to = [OneOf([pokeOntology.ElectricShock, pokeOntology.ElectricField, pokeOntology.Shield, pokeOntology.Whip, pokeOntology.Harden, pokeOntology.SporeRelease, pokeOntology.FireBall, pokeOntology.WaterGun])]
	is_a = [owl.Thing]
	Subclasses:
	Individuals:
		- pokeOntology.ElectricShock
		- pokeOntology.ElectricField
		- pokeOntology.Shield
		- pokeOntology.Whip
		- pokeOntology.Harden
		- pokeOntology.SporeRelease
		- pokeOntology.FireBall
		- pokeOntology.WaterGun
#### Class: pokeOntology.PokemonItem
	equivalent_to = [pokeOntology.Potion | pokeOntology.PokeBall]
	is_a = [owl.Thing]
	Subclasses:
		- pokeOntology.Potion
		- pokeOntology.PokeBall
	Individuals:
		- pokeOntology.pb
		- pokeOntology.pokeball1
		- pokeOntology.pokeball2
		- pokeOntology.supPb1
		- pokeOntology.pokeball3
		- pokeOntology.superpotion1
		- pokeOntology.normalpokeball1
		- pokeOntology.normalpokeball2
		- pokeOntology.normalpokeball3
		- pokeOntology.greatpokeball1
		- pokeOntology.greatpokeball2
		- pokeOntology.supPb2
#### Class: pokeOntology.Potion
	equivalent_to = [pokeOntology.NormalPotion | pokeOntology.SuperPotion]
	is_a = [pokeOntology.PokemonItem]
	Subclasses:
		- pokeOntology.NormalPotion
		- pokeOntology.SuperPotion
	Individuals:
		- pokeOntology.superpotion1
#### Class: pokeOntology.PokeBall
	equivalent_to = [pokeOntology.NormalPokeBall | pokeOntology.GreatPokeBall]
	is_a = [pokeOntology.PokemonItem, pokeOntology.contain.max(1, owl.Thing)]
	Subclasses:
		- pokeOntology.NormalPokeBall
		- pokeOntology.GreatPokeBall
	Individuals:
		- pokeOntology.pokeball1
		- pokeOntology.pokeball2
		- pokeOntology.supPb1
		- pokeOntology.pokeball3
		- pokeOntology.normalpokeball1
		- pokeOntology.normalpokeball2
		- pokeOntology.normalpokeball3
		- pokeOntology.greatpokeball1
		- pokeOntology.greatpokeball2
		- pokeOntology.supPb2
#### Class: pokeOntology.NormalPotion
	is_a = [pokeOntology.Potion]
	Subclasses:
	Individuals:
#### Class: pokeOntology.SuperPotion
	is_a = [pokeOntology.Potion]
	Subclasses:
	Individuals:
		- pokeOntology.superpotion1
#### Class: pokeOntology.NormalPokeBall
	is_a = [pokeOntology.PokeBall]
	Subclasses:
	Individuals:
		- pokeOntology.normalpokeball1
		- pokeOntology.normalpokeball2
		- pokeOntology.normalpokeball3
#### Class: pokeOntology.GreatPokeBall
	is_a = [pokeOntology.PokeBall]
	Subclasses:
	Individuals:
		- pokeOntology.greatpokeball1
		- pokeOntology.greatpokeball2
		- pokeOntology.supPb2
#### Class: pokeOntology.PokemonBattle
	is_a = [owl.Thing, pokeOntology.description.exactly(1, owl.Thing) & pokeOntology.region.exactly(1, owl.Thing), pokeOntology.involves.some(pokeOntology.PokemonFight)]
	Subclasses:
	Individuals:
		- pokeOntology.Ash_vs_Gary
			seeAlso = ['http://bulbapedia.bulbagarden.net/wiki/EP269']
#### Class: pokeOntology.PokemonFight
	is_a = [owl.Thing]
	Subclasses:
	Individuals:
		- pokeOntology.wartortle_vs_evee
		- pokeOntology.pikachu_vs_zapdos
		- pokeOntology.charizard_vs_charizard
		- pokeOntology.pokemonfight1

### Ontology Disjointness <a name = "onto_disjoint"></a>
- AllDisjoint([pokeOntology.Bulbasaur, pokeOntology.Ivysaur, pokeOntology.Charmeleon, pokeOntology.Charizard, pokeOntology.Pikachu, pokeOntology.Zapdos, pokeOntology.Evee, pokeOntology.Vaporeon, pokeOntology.Jolteon, pokeOntology.Moltres, pokeOntology.Squirtle, pokeOntology.Wartortle])
- AllDisjoint([pokeOntology.Human, pokeOntology.Pokemon])
- AllDisjoint([pokeOntology.PokemonTrainer, pokeOntology.SimpleHuman])
- AllDisjoint([pokeOntology.Potion, pokeOntology.PokeBall])
- AllDisjoint([pokeOntology.NormalPotion, pokeOntology.SuperPotion])
- AllDisjoint([pokeOntology.NormalPokeBall, pokeOntology.GreatPokeBall])
### Ontology Object Properties <a name = "onto_oprops"></a>
#### Object Property: pokeOntology.weakness
	Domain: [pokeOntology.Pokemon]
	Range: [pokeOntology.Pokemon]
	Instances:
		- (pokeOntology.bulbasaur1, pokeOntology.moltres1)
		- (pokeOntology.bulbasaur1, pokeOntology.zapdos1)
		- (pokeOntology.bulbasaur1, pokeOntology.charmeleon1)
		- (pokeOntology.ivysaur1, pokeOntology.moltres1)
		- (pokeOntology.ivysaur1, pokeOntology.zapdos1)
		- (pokeOntology.ivysaur1, pokeOntology.charmeleon1)
		- (pokeOntology.charmeleon1, pokeOntology.wartortle1)
		- (pokeOntology.charmeleon1, pokeOntology.squirtle1)
		- (pokeOntology.charmeleon1, pokeOntology.vaporeon1)
		- (pokeOntology.charizard1, pokeOntology.wartortle1)
		- (pokeOntology.charizard1, pokeOntology.squirtle1)
		- (pokeOntology.charizard1, pokeOntology.vaporeon1)
		- (pokeOntology.pikachu1, pokeOntology.ivysaur1)
		- (pokeOntology.pikachu1, pokeOntology.bulbasaur1)
		- (pokeOntology.zapdos1, pokeOntology.ivysaur1)
		- (pokeOntology.zapdos1, pokeOntology.bulbasaur1)
		- (pokeOntology.evee1, pokeOntology.ivysaur1)
		- (pokeOntology.evee2, pokeOntology.ivysaur1)
		- (pokeOntology.vaporeon1, pokeOntology.pikachu1)
		- (pokeOntology.vaporeon1, pokeOntology.zapdos1)
		- (pokeOntology.jolteon1, pokeOntology.ivysaur1)
		- (pokeOntology.jolteon1, pokeOntology.bulbasaur1)
		- (pokeOntology.moltres1, pokeOntology.wartortle1)
		- (pokeOntology.moltres1, pokeOntology.squirtle1)
		- (pokeOntology.moltres1, pokeOntology.vaporeon1)
		- (pokeOntology.squirtle1, pokeOntology.pikachu1)
		- (pokeOntology.squirtle1, pokeOntology.zapdos1)
		- (pokeOntology.wartortle1, pokeOntology.pikachu1)
		- (pokeOntology.wartortle1, pokeOntology.zapdos1)
#### Object Property: pokeOntology.evolves
	Domain: [pokeOntology.Pokemon]
	Range: [pokeOntology.Pokemon]
	Instances:
		- (pokeOntology.bulbasaur1, pokeOntology.ivysaur1)
		- (pokeOntology.charmeleon1, pokeOntology.charizard1)
		- (pokeOntology.evee1, pokeOntology.vaporeon1)
		- (pokeOntology.evee2, pokeOntology.jolteon1)
		- (pokeOntology.squirtle1, pokeOntology.wartortle1)
#### Object Property: pokeOntology.hasSkill
	Domain: [pokeOntology.Pokemon]
	Range: [pokeOntology.Skill]
	Instances:
#### Object Property: pokeOntology.possess
	Domain: [pokeOntology.PokemonTrainer]
	Range: [pokeOntology.PokemonItem]
	Instances:
		- (pokeOntology.AshKetchum, pokeOntology.greatpokeball1)
		- (pokeOntology.AshKetchum, pokeOntology.normalpokeball2)
		- (pokeOntology.AshKetchum, pokeOntology.normalpokeball1)
		- (pokeOntology.GaryOak, pokeOntology.greatpokeball2)
		- (pokeOntology.GaryOak, pokeOntology.pokeball2)
		- (pokeOntology.GaryOak, pokeOntology.pokeball1)
		- (pokeOntology.trainerX, pokeOntology.superpotion1)
		- (pokeOntology.bpt1, pokeOntology.normalpokeball3)
		- (pokeOntology.victor, pokeOntology.pokeball3)
#### Object Property: pokeOntology.contain
	Domain: [pokeOntology.PokeBall]
	Range: [pokeOntology.Pokemon]
	Instances:
		- (pokeOntology.normalpokeball1, pokeOntology.Ashs_Pikachu)
		- (pokeOntology.normalpokeball2, pokeOntology.Ashs_Wartortle)
		- (pokeOntology.greatpokeball1, pokeOntology.Ashs_Charizard)
		- (pokeOntology.greatpokeball2, pokeOntology.Garys_Evee)
		- (pokeOntology.pokeball1, pokeOntology.Garys_Zapdos)
		- (pokeOntology.pokeball2, pokeOntology.Garys_Charizard)
		- (pokeOntology.pb, pokeOntology.pikachu1)
		- (pokeOntology.normalpokeball3, pokeOntology.sp)
		- (pokeOntology.pokeball3, pokeOntology.pokemon1)
#### Object Property: pokeOntology.participateInBattle
	Domain: [pokeOntology.PokemonTrainer]
	Range: [pokeOntology.PokemonBattle]
	Instances:
		- (pokeOntology.AshKetchum, pokeOntology.Ash_vs_Gary)
		- (pokeOntology.GaryOak, pokeOntology.Ash_vs_Gary)
#### Object Property: pokeOntology.involves
	Domain: [pokeOntology.PokemonBattle]
	Range: [pokeOntology.PokemonFight]
	Instances:
		- (pokeOntology.Ash_vs_Gary, pokeOntology.wartortle_vs_evee)
		- (pokeOntology.Ash_vs_Gary, pokeOntology.charizard_vs_charizard)
		- (pokeOntology.Ash_vs_Gary, pokeOntology.pikachu_vs_zapdos)
#### Object Property: pokeOntology.participateInFight
	Domain: [pokeOntology.Pokemon]
	Range: [pokeOntology.PokemonFight]
	Instances:
		- (pokeOntology.Ashs_Wartortle, pokeOntology.wartortle_vs_evee)
		- (pokeOntology.Garys_Evee, pokeOntology.wartortle_vs_evee)
		- (pokeOntology.Ashs_Pikachu, pokeOntology.pikachu_vs_zapdos)
		- (pokeOntology.Garys_Zapdos, pokeOntology.pikachu_vs_zapdos)
		- (pokeOntology.Ashs_Charizard, pokeOntology.charizard_vs_charizard)
		- (pokeOntology.Garys_Charizard, pokeOntology.charizard_vs_charizard)
		- (pokeOntology.pokemon1, pokeOntology.pokemonfight1)
		- (pokeOntology.pokemon2, pokeOntology.pokemonfight1)
### Ontology Data Properties <a name = "onto_dprops"></a>
#### Data Property: pokeOntology.demographic
	Domain: []
	Range: []
	Instances:
#### Data Property: pokeOntology.height
	Domain: []
	Range: [<class 'float'>]
	Instances:
		- (pokeOntology.turtle, 25)
		- (pokeOntology.sp, 5)
#### Data Property: pokeOntology.weight
	Domain: []
	Range: [<class 'float'>]
	Instances:
		- (pokeOntology.turtle, 49)
		- (pokeOntology.supPb1, 105)
		- (pokeOntology.supPb2, 120)
		- (pokeOntology.sp, 5)
#### Data Property: pokeOntology.age
	Domain: []
	Range: [<class 'int'>]
	Instances:
		- (pokeOntology.bpt1, 10)
#### Data Property: pokeOntology.region
	Domain: []
	Range: [OneOf(['kanto', 'johto'])]
	Instances:
#### Data Property: pokeOntology.characteristic
	Domain: []
	Range: []
	Instances:
#### Data Property: pokeOntology.power
	Domain: []
	Range: [<class 'float'>]
	Instances:
		- (pokeOntology.Ashs_Pikachu, 105)
		- (pokeOntology.Ashs_Wartortle, 50)
		- (pokeOntology.Ashs_Charizard, 101)
		- (pokeOntology.Garys_Evee, 65)
		- (pokeOntology.Garys_Zapdos, 100)
		- (pokeOntology.Garys_Charizard, 95)
		- (pokeOntology.pokemon1, 80)
		- (pokeOntology.pokemon2, 10)
#### Data Property: pokeOntology.heart
	Domain: []
	Range: [<class 'float'>]
	Instances:
#### Data Property: pokeOntology.wingSpan
	Domain: [pokeOntology.FlyingPokemon]
	Range: [<class 'float'>]
	Instances:
		- (pokeOntology.articuno, 527)
#### Data Property: pokeOntology.feature
	Domain: []
	Range: [OneOf(['seed', 'flower', 'mammal', 'reptile', 'bird', 'rodent'])]
	Instances:
#### Data Property: pokeOntology.fullName
	Domain: []
	Range: [<class 'str'>]
	Instances:
		- (pokeOntology.AI, 'Antonio')
#### Data Property: pokeOntology.description
	Domain: []
	Range: [<class 'str'>]
	Instances:
	
## 2. Ontology Inconsistencies <a name = "onto_incons"></a>
Optionally, inconsistencies might be [added](/inconsistency.py) to the ontolgy in creation with the aim of checking the modeled semantics.

```
onto.pikachu1.weakness = [onto.charmeleon1]
```
violates *ElectricPokemon.is_a.append(weakness.only(GrassPokemon))*

```
onto.charmeleon1.evolves = onto.pikachu1
```
violates *Charmeleon.is_a.append(evolves.only(Charizard))*

```
onto.pikachu1.region = "latina"
```
violates *class region(demographic, FunctionalProperty):
            range = [OneOf(["kanto", "johto"])]*

```
onto.charizard1.feature = "dragon"
```
violates *class feature(characteristic, FunctionalProperty):
            range = [OneOf(["seed", "flower", "mammal", "reptile", "bird", "rodent"])]*

```
onto.zapdos1.wingSpan = 499
```
violates *Zapdos.is_a.append(wingSpan.only(ConstrainedDatatype(float, min_exclusive = 500)))*

```
onto.bulbasaur1.height = 10
onto.bulbasaur1.weight = 55
```
violates *Bulbasaur.is_a.append(height.only(ConstrainedDatatype(float, max_exclusive = 50)) & weight.only(ConstrainedDatatype(float, max_exclusive = 50)))*

```
onto.evee1.height = 202
```
violates *Evee.is_a.append(height.only(ConstrainedDatatype(float, max_exclusive = 100)))*

```
illegalSkill = onto.Skill("action")
AllDifferent([illegalSkill, onto.ElectricShock, onto.ElectricField, onto.Shield, onto.Whip, onto.Harden, onto.SporeRelease, onto.FireBall, onto.WaterGun])
```
violates *Skill.equivalent_to.append(OneOf([electricShock, electricField, shield, whip, harden, sporeRelease, fireBall, waterGun]))*

```
illegalPB = onto.NormalPokeBall()
illegalPB.contain = [onto.bulbasaur1, onto.charizard1]
```
violates *PokeBall.is_a.append(contain.max(1))*

## 3. Reasoning <a name = "reasoning"></a>

A separate world is instantiated for isolating ontology before reasoning, then [HermiT](http://www.hermit-reasoner.com/) reasoner is executed, obtaining the following results:
#### Equivalenting
* Owlready * Equivalenting: pokeOntology.Ivysaur pokeOntology.PoisonPokemon
* Owlready * Equivalenting: pokeOntology.PoisonPokemon pokeOntology.Ivysaur
* Owlready * Equivalenting: pokeOntology.Evee pokeOntology.NormalPokemon
* Owlready * Equivalenting: pokeOntology.NormalPokemon pokeOntology.Evee
#### Reparenting
* Owlready * Reparenting pokeOntology.Zapdos: {pokeOntology.FlyingPokemon, pokeOntology.ElectricPokemon} => {pokeOntology.LegendaryPokemon, pokeOntology.ElectricPokemon}
* Owlready * Reparenting pokeOntology.Bulbasaur: {pokeOntology.GrassPokemon} => {pokeOntology.StarterPokemon, pokeOntology.GrassPokemon}
* Owlready * Reparenting pokeOntology.Squirtle: {pokeOntology.WaterPokemon} => {pokeOntology.StarterPokemon, pokeOntology.WaterPokemon}
* Owlready * Reparenting pokeOntology.Moltres: {pokeOntology.FlyingPokemon, pokeOntology.FirePokemon} => {pokeOntology.FirePokemon, pokeOntology.LegendaryPokemon}
* Owlready * Reparenting pokeOntology.Ivysaur: {pokeOntology.PoisonPokemon, pokeOntology.GrassPokemon} => {pokeOntology.GrassPokemon}
* Owlready * Reparenting pokeOntology.PoisonPokemon (since equivalent): {pokeOntology.PoisonPokemon, pokeOntology.GrassPokemon} => {pokeOntology.GrassPokemon}
* Owlready * Reparenting pokeOntology.sp: {pokeOntology.Pokemon} => {pokeOntology.StarterPokemon}
* Owlready * Reparenting pokeOntology.articuno: {pokeOntology.Pokemon} => {pokeOntology.LegendaryPokemon}
* Owlready * Reparenting pokeOntology.bpt1: {pokeOntology.Human} => {pokeOntology.PokemonTrainer}
* Owlready * Reparenting pokeOntology.ivysaur1: {pokeOntology.Ivysaur} => {pokeOntology.Ivysaur, pokeOntology.PoisonPokemon}
* Owlready * Reparenting pokeOntology.turtle: {pokeOntology.Pokemon} => {pokeOntology.StarterPokemon}
* Owlready * Reparenting pokeOntology.AI: {pokeOntology.Organism} => {pokeOntology.Human}
* Owlready * Reparenting pokeOntology.trainerX: {pokeOntology.Organism} => {pokeOntology.PokemonTrainer}
* Owlready * Reparenting pokeOntology.pb: {pokeOntology.PokemonItem} => {pokeOntology.PokeBall}
#### Adding relation
* Owlready * Adding relation pokeOntology.articuno hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.ivysaur1 hasSkill pokeOntology.Whip
* Owlready * Adding relation pokeOntology.ivysaur1 hasSkill pokeOntology.SporeRelease
* Owlready * Adding relation pokeOntology.vaporeon1 hasSkill pokeOntology.WaterGun
* Owlready * Adding relation pokeOntology.vaporeon1 hasSkill pokeOntology.Harden
* Owlready * Adding relation pokeOntology.evee1 hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.charmeleon1 hasSkill pokeOntology.FireBall
* Owlready * Adding relation pokeOntology.charizard1 hasSkill pokeOntology.FireBall
* Owlready * Adding relation pokeOntology.charizard1 hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.pikachu1 hasSkill pokeOntology.ElectricField
* Owlready * Adding relation pokeOntology.pikachu1 hasSkill pokeOntology.ElectricShock
* Owlready * Adding relation pokeOntology.wartortle1 hasSkill pokeOntology.WaterGun
* Owlready * Adding relation pokeOntology.wartortle1 hasSkill pokeOntology.Harden
* Owlready * Adding relation pokeOntology.Ashs_Charizard hasSkill pokeOntology.FireBall
* Owlready * Adding relation pokeOntology.Ashs_Charizard hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.squirtle1 hasSkill pokeOntology.WaterGun
* Owlready * Adding relation pokeOntology.squirtle1 hasSkill pokeOntology.Harden
* Owlready * Adding relation pokeOntology.Garys_Zapdos hasSkill pokeOntology.ElectricField
* Owlready * Adding relation pokeOntology.Garys_Zapdos hasSkill pokeOntology.ElectricShock
* Owlready * Adding relation pokeOntology.Garys_Zapdos hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.bulbasaur1 hasSkill pokeOntology.Whip
* Owlready * Adding relation pokeOntology.Ashs_Pikachu hasSkill pokeOntology.ElectricField
* Owlready * Adding relation pokeOntology.Ashs_Pikachu hasSkill pokeOntology.ElectricShock
* Owlready * Adding relation pokeOntology.Garys_Charizard hasSkill pokeOntology.FireBall
* Owlready * Adding relation pokeOntology.Garys_Charizard hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.zapdos1 hasSkill pokeOntology.ElectricField
* Owlready * Adding relation pokeOntology.zapdos1 hasSkill pokeOntology.ElectricShock
* Owlready * Adding relation pokeOntology.zapdos1 hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.evee2 hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.moltres1 hasSkill pokeOntology.FireBall
* Owlready * Adding relation pokeOntology.moltres1 hasSkill pokeOntology.Shield
* Owlready * Adding relation pokeOntology.Ashs_Wartortle hasSkill pokeOntology.WaterGun
* Owlready * Adding relation pokeOntology.Ashs_Wartortle hasSkill pokeOntology.Harden
* Owlready * Adding relation pokeOntology.jolteon1 hasSkill pokeOntology.ElectricField
* Owlready * Adding relation pokeOntology.jolteon1 hasSkill pokeOntology.ElectricShock
* Owlready * Adding relation pokeOntology.Garys_Evee hasSkill pokeOntology.Shield

The inferred ontology is saved in file [pokeOntologyInferred.owl](/pokeOntologyInferred.owl)

## 4. Querying Ontology <a name = "query"></a>

The following [SPARQL queries](/SPARQL_queries.rq) are executed on the two worlds: ontology after reasoning, ontology before reasoning

```
# Retrives SuperPokeBall, PokeBall with a weight greater than 100

SELECT DISTINCT ?pokeball 
WHERE {
    ?pokeball rdf:type ?type .
    ?type rdfs:subClassOf* pokeOntology:PokeBall .
    ?pokeball pokeOntology:weight ?w .
    FILTER(?w > "100"^^xsd:float) .
}
```
**Result after reasoning =**\
[[pokeOntology.supPb1], [pokeOntology.supPb2]]

**Result before reasoning =**\
[[pokeOntology.supPb1], [pokeOntology.supPb2]]
```
# Retrives all the Human and, optionally, his Pokemon: a human possessing a pokeball which contains a certain pokemon has that pokemon

SELECT ?human ?pokemon
WHERE {
    ?human rdf:type ?type .
    ?type rdfs:subClassOf* pokeOntology:Human .
    OPTIONAL {
        ?human pokeOntology:possess/pokeOntology:contain ?pokemon .
    }
}
```
**Result after reasoning =**\
[[pokeOntology.bpt1, pokeOntology.sp], [pokeOntology.AI, None], [pokeOntology.AshKetchum, pokeOntology.Ashs_Pikachu], [pokeOntology.AshKetchum, pokeOntology.Ashs_Wartortle], [pokeOntology.AshKetchum, pokeOntology.Ashs_Charizard], [pokeOntology.GaryOak, pokeOntology.Garys_Evee], [pokeOntology.GaryOak, pokeOntology.Garys_Zapdos], [pokeOntology.GaryOak, pokeOntology.Garys_Charizard], [pokeOntology.victor, pokeOntology.pokemon1], [pokeOntology.trainerX, None], [pokeOntology.bpt1, pokeOntology.sp], [pokeOntology.Ashs_Mother, None]]

**Result before reasoning =**\
[[pokeOntology.bpt1, pokeOntology.sp], [pokeOntology.AshKetchum, pokeOntology.Ashs_Pikachu], [pokeOntology.AshKetchum, pokeOntology.Ashs_Wartortle], [pokeOntology.AshKetchum, pokeOntology.Ashs_Charizard], [pokeOntology.GaryOak, pokeOntology.Garys_Evee], [pokeOntology.GaryOak, pokeOntology.Garys_Zapdos], [pokeOntology.GaryOak, pokeOntology.Garys_Charizard], [pokeOntology.victor, pokeOntology.pokemon1], [pokeOntology.Ashs_Mother, None]]
```
# Counts the Pokemon each PokemonTrainer has

SELECT ?trainer (COUNT(DISTINCT ?pokemon) AS ?count)
WHERE {
    ?trainer pokeOntology:possess ?pokeball .
    ?pokeball pokeOntology:contain ?pokemon .
}
GROUP BY ?trainer
ORDER BY DESC(?count)
```
**Result after reasoning =**\
[[pokeOntology.AshKetchum, 3], [pokeOntology.GaryOak, 3], [pokeOntology.bpt1, 1], [pokeOntology.victor, 1]]

**Result before reasoning =**\
[[pokeOntology.AshKetchum, 3], [pokeOntology.GaryOak, 3], [pokeOntology.bpt1, 1], [pokeOntology.victor, 1]]
```
# Retrives BeginnerPokemonTrainer, Human that possesses a PokeBall that contains a StarterPokemon and has an age less than 12

SELECT DISTINCT ?human
WHERE {
    ?human rdf:type ?type .
    ?type rdfs:subClassOf* pokeOntology:Human .
    ?human pokeOntology:possess ?pokeball .
    ?pokeball pokeOntology:contain ?pokemon .
    ?pokemon rdf:type pokeOntology:StarterPokemon .
    ?human pokeOntology:age ?a .
    FILTER(?a < "12"^^xsd:int) .
}
```
**Result after reasoning =**\
[[pokeOntology.bpt1]]

**Result before reasoning =**\
[]
```
# Retrives all the Pokemon which does not have an evolution

SELECT DISTINCT ?pokemon
WHERE {
    ?pokemon rdf:type ?type .
    ?type rdfs:subClassOf* pokeOntology:Pokemon .
    FILTER NOT EXISTS {
        ?pokemon pokeOntology:evolves ?evolution .
    }
}
```
**Result after reasoning =**\
[[pokeOntology.turtle], [pokeOntology.articuno], [pokeOntology.sp], [pokeOntology.pokemon1], [pokeOntology.pokemon2], [pokeOntology.Ashs_Pikachu], [pokeOntology.Ashs_Wartortle], [pokeOntology.Ashs_Charizard], [pokeOntology.Garys_Evee], [pokeOntology.Garys_Zapdos], [pokeOntology.Garys_Charizard], [pokeOntology.ivysaur1], [pokeOntology.charizard1], [pokeOntology.pikachu1], [pokeOntology.zapdos1], [pokeOntology.vaporeon1], [pokeOntology.jolteon1], [pokeOntology.moltres1], [pokeOntology.wartortle1]]

**Result before reasoning =**\
[[pokeOntology.turtle], [pokeOntology.articuno], [pokeOntology.sp], [pokeOntology.pokemon1], [pokeOntology.pokemon2], [pokeOntology.Ashs_Charizard], [pokeOntology.Garys_Charizard], [pokeOntology.charizard1], [pokeOntology.moltres1], [pokeOntology.vaporeon1], [pokeOntology.Ashs_Wartortle], [pokeOntology.wartortle1], [pokeOntology.ivysaur1], [pokeOntology.Garys_Zapdos], [pokeOntology.zapdos1], [pokeOntology.Ashs_Pikachu], [pokeOntology.pikachu1], [pokeOntology.jolteon1], [pokeOntology.Garys_Evee]]
```
# Retrives all the victors of each PokemonFight: a victor is the PokemonTrainer possessing the pokemon with greater power in the fight

SELECT ?fight ?victor
WHERE {
    ?pokemon1 pokeOntology:participateInFight ?fight .
    ?pokemon2 pokeOntology:participateInFight ?fight .
    ?pokemon1 pokeOntology:power ?p1 .
    ?pokemon2 pokeOntology:power ?p2 .
    FILTER(?p1 > ?p2) .
    ?victor pokeOntology:possess ?pokeball .
    ?pokeball pokeOntology:contain ?pokemon1 .
}
```
**Result after reasoning =**\
[[pokeOntology.wartortle_vs_evee, pokeOntology.GaryOak], [pokeOntology.pikachu_vs_zapdos, pokeOntology.AshKetchum], [pokeOntology.charizard_vs_charizard, pokeOntology.AshKetchum], [pokeOntology.pokemonfight1, pokeOntology.victor]]

**Result before reasoning =**\
[[pokeOntology.wartortle_vs_evee, pokeOntology.GaryOak], [pokeOntology.pikachu_vs_zapdos, pokeOntology.AshKetchum], [pokeOntology.charizard_vs_charizard, pokeOntology.AshKetchum], [pokeOntology.pokemonfight1, pokeOntology.victor]]
```
# Retrives the number of victories each PokemonTrainer has obtained in each PokemonBattle

SELECT ?battle ?trainer (COUNT(?pokemon1) AS ?nVictories)
WHERE {
    ?trainer pokeOntology:participateInBattle ?battle .
    ?battle pokeOntology:involves ?fight .
    ?trainer pokeOntology:possess/pokeOntology:contain ?pokemon1 .
    ?pokemon1 pokeOntology:participateInFight ?fight .
    ?pokemon2 pokeOntology:participateInFight ?fight .
    ?pokemon1 pokeOntology:power ?p1 .
    ?pokemon2 pokeOntology:power ?p2 .
    FILTER(?p1 > ?p2) .
}
GROUP BY ?battle ?trainer
```
**Result after reasoning =**\
[[pokeOntology.Ash_vs_Gary, pokeOntology.AshKetchum, 2], [pokeOntology.Ash_vs_Gary, pokeOntology.GaryOak, 1]]

**Result before reasoning =**\
[[pokeOntology.Ash_vs_Gary, pokeOntology.AshKetchum, 2], [pokeOntology.Ash_vs_Gary, pokeOntology.GaryOak, 1]]

# Author <a name = "author"></a>

[Antonio Ionta](https://www.linkedin.com/in/antonio-ionta-a349b515a/) - Idea & Implementation

# Acknowledgements <a name = "acknowledgement"></a>

Inspiration and references [here](/links.txt)
