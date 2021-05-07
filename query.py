from owlready2 import *
import json

def addInstances(onto):
    # SuperPokeBall
    supPb1 = onto.PokeBall("supPb1", weight=105)
    supPb2 = onto.GreatPokeBall("supPb2", weight=120)

    # BeginnerPokemonTrainer
    sp = onto.Pokemon("sp", height=5, weight=5)
    pb = onto.NormalPokeBall(contain=[sp])
    bpt1 = onto.Human("bpt1", age=10, possess=[pb])

    # PokemonFight victors
    fight = onto.PokemonFight()
    victorPokemon = onto.Pokemon(power=80, participateInFight=[fight])
    loserPokemon = onto.Pokemon(power=10, participateInFight=[fight])
    victorPb = onto.PokeBall(contain=[victorPokemon])
    # loserPb = onto.PokeBall(contain=[loserPokemon])
    victor = onto.PokemonTrainer("victor", possess=[victorPb])
    # loser = onto.PokemonTrainer("loser", possess=[loserPb])

def executeQuery(onto):
    # Reading file with queries in a single string
    with open("SPARQL_queries.rq", "r") as read_file:
        data = read_file.read()

    # Tokenize string on the basis of regex for extracting queries
    queries = re.split('#.*', data)

    for i in range(1, len(queries)):
        print("----------{}".format(queries[i]), end='')
        result = list(default_world.sparql(queries[i]))
        print("result = {}\n----------".format(result))
