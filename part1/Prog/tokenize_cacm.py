#! usr/bin/env python3.6
# -*- coding: utf-8 -*-

import re
import nltk

nltk.download('punkt')
from nltk import word_tokenize

inpathname = "../Collection/Init/"
outpathname = "../Collection/Token/"

def FiltreTokenizer(inpath, outpath):

    # nombre de documents disponibles dans la librairie
    nDocs = 3204;

    for i in range(1, nDocs + 1):
        file = "CACM-" + str(i)
        infile = inpath + file
        outfile = outpath + file + ".flt"

        # on ouvre le fichier initial CACM-i
        with open(infile, "r") as InitFile:
            print("processing file " + file)

            # on créé le fichier filtré CACM-i
            with open(outfile, "w+") as TokenFile:
                for line in InitFile:
                    tokens = nltk.word_tokenize(line)
                    for j in range(0, len(tokens)):
                        regex = re.compile(r"([A-Z]|[a-z])\w+")
                        if regex.match(tokens[j]):
                            TokenFile.write(tokens[j].lower() + "\n")

FiltreTokenizer(inpathname, outpathname)
