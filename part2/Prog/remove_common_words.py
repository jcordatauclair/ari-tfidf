#! usr/bin/env python3.6
# -*- coding: utf-8 -*-

import nltk

nltk.download('punkt')
from nltk import word_tokenize
from nltk.stem.porter import *

inpathname = "../../TP1/Collection/Token/"
outpathname = "../Collection/NoCommonWords/"
commonwordsfile = "../../TP1/Data/common_words"

# ici, stembool est un booléen qui indique si oui ou non on souhaite l'incorporer
# dans le traitement
def RemoveCommonWords(inpath, outpath, stembool):

    if (stembool == True):
        stemmer = PorterStemmer()

    # nombre de documents disponibles dans la librairie
    nDocs = 3204;

    # on définit un dictionnaire auquel on va associer un 'common-word' (mot)
    # et une clé (1)
    stopList = {}

    # on créé notre stop-list depuis notre fichier de common-words
    with open(commonwordsfile) as CwFile:
        for line in CwFile:
            commonWord = nltk.word_tokenize(line)[0]
            stopList[commonWord] = 1

    # on parcourt chacun de nos fichiers filtrés
    for i in range(1, nDocs + 1):
        file = "CACM-" + str(i)
        infile = inpath + file + ".flt"
        outfile = outpath + file + ".sttr"

        # on ouvre le fichier filtré CACM-i
        with open(infile, "r") as TokenFile:
            print("processing file " + file)

            # on créé le fichier sans les common-words CACM-i
            with open(outfile, "w+") as NoCwFile:
                for line in TokenFile:
                    word = nltk.word_tokenize(line)[0]
                    if word not in stopList:
                        if (stembool == True):
                            NoCwFile.write(stemmer.stem(word) + " ")
                        else:
                            NoCwFile.write(word + " ")
                    else:
                        print("  removing " + word)


RemoveCommonWords(inpathname, outpathname, True)
