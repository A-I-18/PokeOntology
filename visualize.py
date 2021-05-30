def printModel(onto):
    print("\n>>> ONTOLOGY CLASSES:\n")
    for c in (onto.classes()):
        print("# Class: {}".format(c))
        altLabel = c.label
        comment = c.comment
        if altLabel:
            print("\taltLabel = {}".format(altLabel))
        if comment:
            print("\tcomment = {}".format(comment))
        eqt = c.equivalent_to
        if eqt:
            print("\tequivalent_to = {}".format(eqt))
        isa = c.is_a
        if isa:
            print("\tis_a = {}".format(isa))
        subcs = c.subclasses()
        print("\tSubclasses:")
        for subc in subcs:
            print("\t\t- {}".format(subc))
        ins = c.instances()
        print("\tIndividuals:")
        for i in ins:
            print("\t\t- {}".format(i))
            seeAlso = i.seeAlso
            if seeAlso:
                print("\t\t\tseeAlso = {}".format(seeAlso))    

    print("\n>>> ONTOLOGY DISJOINTNESS:\n")
    for disc in onto.disjoint_classes():
        print("# Disjoint classes: {}".format(disc))
    for disp in onto.disjoint_properties():
        print("# Disjoint properties: {}".format(disp))
    for diffi in onto.different_individuals():
        print("# Different individuals: {}".format(diffi))

    print("\n>>> ONTOLOGY OBJECT PROPERTIES:\n")
    for op in (onto.object_properties()):
        print("# Object Property: {}".format(op))
        print("\tDomain: {}".format(op.domain))
        print("\tRange: {}".format(op.range))
        print("\tInstances:")
        ins = op.get_relations()
        for i in ins:
            print("\t\t- {}".format(i))

    print("\n>>> ONTOLOGY DATA PROPERTIES:\n")
    for dp in (onto.data_properties()):
        print("# Data Property: {}".format(dp))
        print("\tDomain: {}".format(dp.domain))
        print("\tRange: {}".format(dp.range))
        print("\tInstances:")
        ins = dp.get_relations()
        for i in ins:
            print("\t\t- {}".format(i))