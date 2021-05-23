<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="/PokeOntology-Logo.jpeg" alt="Project logo"></a>
</p>

<h1 align="center">PokeOntology</h1>

---

<p align="center">
  Working with Knowledge Representation with owlready2 python framework
  <br /> 
</p>

# 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Project Structure](#structure)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgement)

# About <a name = "about"></a>

Homework project as part of the [Knowledge Representation and Semantic Technologies](http://www.diag.uniroma1.it//rosati/krst/) course of the master degree in "Engineering in Computer Science" of "Sapienza, Università di Roma", A.Y.2020/21.

The aim of the project is to realize a practical exercise of Knowledge Representation.

The project consists in a Python application, exploiting the Owlready2 framework, which manages from skratch an OWL ontology. The Pokemon fictional universe is used as context.

# Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.

## Built Using

- [Python3](https://www.python.org/) - Programming Language
- [Owlready2](https://pypi.org/project/Owlready2/) - A package for ontology-oriented programming in Python: load OWL 2.0 ontologies as Python objects, modify them, save them, and perform reasoning via HermiT. Includes an optimized RDF quadstore. [Documentation](https://owlready2.readthedocs.io/en/latest/index.html) | [Project Repository](https://bitbucket.org/jibalamy/owlready2/src/master/)

## Prerequisites

What things you need to install the software and how to install them.

For running the application, essentially, only [python3](https://www.python.org/downloads/) and Owlready2 framework are needed

```
pip install Owlready2
```

## Run

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

## 1. Ontology Creation

The OWL 2 ontology identified by the fictional IRI http://myonto.com/pokeOntology.owl is created and saved in the file [pokeOntology.owl](/pokeOntology.py), adopting NTriples format.

### Ontology Classes
[TODO]
### Ontology Disjointness
[TODO]
### Ontology Object Properties
[TODO]
### Ontology Data Properties
[TODO]
### Ontology Inconsistencies
Optionally, inconsistencies might be added to the ontolgy in creation with the aim of checking the modeled semantics.
[TODO]

## 2. Reasoning

A separate world is instantiated for isolating ontology before reasoning, then [HermiT](http://www.hermit-reasoner.com/) reasoner is executed, obtaining the following results
[TODO]

The inferred ontology is saved in file [pokeOntologyInferred.owl](/pokeOntologyInferred.owl)

## 3. Querying Ontology

The following [SPARQL queries](/SPARQL_queries.rq) are executed on the two worlds: ontology after reasoning, ontology before reasoning
[TODO]

# Author <a name = "author"></a>

[Antonio Ionta](https://www.linkedin.com/in/antonio-ionta-a349b515a/) - Idea & Implementation

# Acknowledgements <a name = "acknowledgement"></a>

Inspiration and references [here](/links.txt)
