<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
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

-----Write about 1-2 paragraphs describing the purpose of your project.

Homework project as part of the "Knowledge Representation and Semantic Technologies" course of the master degree in "Engineering in Computer Science" of "Sapienza, Università di Roma".

The aim of the project is to realize a practical exercise of Knowledge Representation.

The project consists in a Python application, exploiting the Owlready2 framework, which manages from skratch an OWL ontology. The Pokemon fictional universe is used as context.

# Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Built Using

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## Prerequisites

What things you need to install the software and how to install them.

For running the application, essentially, only python3 and Owlready2 framework are needed

```
pip install Owlready2
```

## Run

In the root of the project:

```
python pokeOntology.py
```
# Project Structure <a name="structure"></a>
[TODO]

# Usage <a name="usage"></a>

The execution of the program follows these steps

## 1. Ontology Creation

The OWL 2 ontology identified by the fictional IRI http://myonto.com/pokeOntology.owl is created and saved in the file pokeOntology.owl, adopting NTriples format.

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

A separate world is instantiated for isolating ontology before reasoning, then HermiT reasoner is executed, obtaining the following results
[TODO]

The inferred ontology is saved in file pokeOntologyInferred.owl

## 3. Querying Ontology

The following SPARQL queries are executed on the two worlds: ontology after reasoning, ontology before reasoning
[TODO]

# Author <a name = "author"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

# Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
