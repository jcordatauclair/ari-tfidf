#! usr/bin/env python3.6
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import json

inpathname = "../Collection/NoCommonWords/"
outpathname = "../Collection/Vocabulary/"


# fonction qui génère un fichier JSON contenant la représentation tf.idf de la
# collection de documents
# ex. de résultat : {"novemb": [2, 0.301029995, {"4": 0.1428, "5": 0.212}], ...}
#   - "novem" est un terme du vocabulaire
#   - 2 est le nombre de documents dans lequel il apparaît, ie df
#   - 0.301029995 est l'idf
#   - 4 et 5 sont les identifiants des 2 documents dans lesquels il apparaît
#   - 0.1428 est le tf.idf pour le document concerné
def BuildVocabulary(inpath, outpath):

    # nombre de documents disponibles dans la librairie
    nDocs = 3204

    # on définit un dictionnaire qui correspondra à notre vocabulaire
    # clé : mot
    # valeur : df (nombre de documents dans lequel le mot apparaît)
    v = {}

    # on traite successivement tous les fichiers de la collection
    for i in range(1, nDocs + 1):
        file = "CACM-" + str(i)
        infile = inpath + file + ".sttr"
        outfile = outpath + "vocabulaire.json"

        # on ouvre le fichier filtré CACM-i
        with open(infile, "r") as NoCwFile:
            print("processing file " + file)

            nword = 0 # nombre de mots dans le document courant
            d = {} # le dictionnaire qui permet de savoir combien de fois et dans
                   # quel(s) document(s) se trouve le terme en question

            # pour chaque mot du document traité
            for line in NoCwFile:
                for word in line.split():
                    nword += 1
                for word in line.split():

                    # on fixe notre variable à 0 pour le nouveau document que
                    # l'on va traiter, elle indique le nombre de fois où word a
                    # été rencontré dans le document courant
                    encountered = 0.0

                    # si le mot n'est pas dans le vocabulaire, alors :
                    # - on l'ajoute en initialisant son df
                    # - on indique qu'il apparaît une fois dans le doc i
                    if word not in v:
                        v[word] = [1]
                        d[i] = 1.0 / nword

                    # sinon, si le mot est déjà dans le vocabulaire, alors :
                    # - si le mot n'a pas été rencontré dans ce doc :
                    #    ~ on icrémente son df
                    #    ~ on indique qu'il apparaît une fois dans le doc i
                    #    ~ on fixe la variable encountered à 1
                    # - sinon, si le mot a déjà été rencontré dans ce doc :
                    #    ~ on incrémente son nombre d'apparition dans le doc i
                    #    ~ on indique qu'il apparaît une fois de plus dans le
                    #      doc i
                    elif word in v:
                          if (encountered == 0):
                              v[word][0] += 1
                              d[i] = 1.0 / nword
                              encountered = 1.0
                          elif (encountered != 0):
                              encountered += 1.0
                              d[i] = encountered / nword

                    # on ajoute enfin le dictionnaire d au dictionnaire v
                    v[word].append(d)

    # on fusionne les dictionnaires d pour chaque terme rencontré et on rajoute
    # l'idf défini par log(N/df)
    for key, value in v.items():
        newd = {}
        idf = np.log10(nDocs / float(value[0]))
        for d in value[1:]:
            d[d.keys()[0]] = d.values()[0] * idf # d.values()[0] est tf ici
            newd.update(d)
        del value[1:]

        value.append(idf)
        value.append(newd)




    # on écrit les résultats dans un nouveau fichier
    with open(outfile, "w+") as VocabFile:
        json.dump(v, VocabFile)
    print("the results can be accessed in '../Collection/Vocabulary/vocabulaire.json'")

BuildVocabulary(inpathname, outpathname)
