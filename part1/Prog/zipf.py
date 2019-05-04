#! usr/bin/env python3.6
# -*- coding: utf-8 -*-

import nltk
import numpy as np
import matplotlib.pyplot as plt

nltk.download('punkt')
from nltk import word_tokenize

inpathname = "../Collection/Token/"
outpathname = "../Collection/Zipf/"

def Zipf(inpath, outpath):

    # nombre de documents disponibles dans la librairie
    nDocs = 3204;

    # on définit un dictionnaire auquel on va associer une valeur (mot)
    # et une clé (fréquence d'apparition de ce mot)
    d = {}

    TotalOccurrences = 0 # nombre total de mots
    TotalVocabulaire = 0 # nombre de mots différents

    # tableau dont l'indice correspond au rang du mot, la valeur correspond à
    # sa fréquence d'apparition
    RankFreq = []

    # loi de Zipf : fc(m) = lambda / rang(m)
    fc = []

    for i in range(1, nDocs + 1):
        file = "CACM-" + str(i)
        infile = inpath + file + ".flt"
        outfile = outpath + "results.txt"

        # on ouvre le fichier filtré CACM-i
        with open(infile, "r") as TokenFile:
            print("processing file " + file)

            for line in TokenFile:
                word = nltk.word_tokenize(line)[0]

                # si le mot n'est pas dans le dictionnaire, alors on l'ajoute
                # si le mot y est déjà, alors on incrémente sa fréquence
                if word not in d:
                    d[word] = 1
                    TotalVocabulaire += 1
                else:
                    d[word] += 1
                TotalOccurrences += 1

    with open(outfile, "w+") as ZipfFile:
        dsorted = sorted(d.items(), key=lambda kv: kv[1], reverse = True)
        ZipfFile.write("Les 10 mots apparaissant le plus souvent et leur fréquence :" + "\n")

        for word in range(0, 10):
            ZipfFile.write(str(dsorted[word]) + "\n")

        ZipfFile.write("\n")
        ZipfFile.write("Taille du vocabulaire : " + str(TotalVocabulaire) + "\n")
        ZipfFile.write("Nombre d'occurrences total : " + str(TotalOccurrences) + "\n")

        l = TotalOccurrences/np.log(TotalVocabulaire)
        ZipfFile.write("Valeur théorique de lambda : " + str(l))

        print("the results can be accessed in '../Collection/Zipf/results.txt'")

    for i in range(0, 500): # 500 car la transition est ainsi plus visible
        RankFreq.append(dsorted[i][1])

    for j in range(0, TotalVocabulaire):
        fc.append(l / (j + 1))

    print("displaying the first plot")
    plt.plot(RankFreq, color="blue", linestyle="solid")
    plt.xlabel('Rang')
    plt.ylabel('Occurrences')
    plt.title("Nombre total d'occurrences en fonction du rang des 500 premiers termes")
    plt.show()

    print("displaying the second plot")
    plt.plot(np.log(np.arange(TotalVocabulaire)), np.log(fc), color="blue", linestyle="solid")
    plt.xlabel('ln(rang)')
    plt.ylabel('ln(fc)')
    plt.title("Loi de Zipf pour les 500 premiers termes")
    plt.show()

Zipf(inpathname, outpathname)
