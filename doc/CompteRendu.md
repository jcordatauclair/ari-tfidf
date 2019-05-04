## **COMPTE-RENDU**

###### Julien Cordat-Auclair, **INFO4**.
*Lien du sujet sur la page **https://hmul8r6b.imag.fr/doku.php***.

--------------------------------------------------------------------------------

### **1ère partie :** *tokenizer* & loi de Zipf

Cette première partie permet de former une collection de documents ordonnée pour pouvoir simplifier les traitements qui seront réalisés plus tard. Elle en met d'ailleurs un premier en place.

#### - ***tokenize_cacm.py***

C'est le script qui permet de rendre la lecture des documents aisée en remplaçant les majuscules par des minuscules et en supprimant les chiffres et les symboles.

**Méthode :** on parcourt chaque document de la collection ainsi que chaque terme (déjà mis en minuscule via la fonction `lower()`) grâce à la librairie *nltk*. À l'aide d'une expression régulière adaptée, on identifie les termes qui nous conviennent et on les écrit dans un nouveau fichier avec l'extension *.flt*.

**Exemple :**
- avant traitement
```
Computer Patent Disclosures
CACM October, 1964
Kates, J. P.
```
- après traitement :
```
computer
patent
disclosures
cacm
october
kates
```

#### - ***zipf.py***

Ce script permet plusieurs choses : calculer les fréquences d'apparitions de tous les termes apparaissant dans la collection, la taille du vocabulaire mais aussi de tracer les courbes représentant la loi de Zipf.

**Méthode :** on utilise un dictionnaire qui aura comme clés les termes rencontrés au cours du parcours de tous les documents, et comme valeur associée à chacune de ces clés leur fréquence d'apparition dans la collection.
```
# si le mot n'est pas dans le dictionnaire, alors on l'ajoute
# si le mot y est déjà, alors on incrémente sa fréquence
if word not in d:
  d[word] = 1
  TotalVocabulaire += 1
else:
  d[word] += 1
TotalOccurrences += 1
```
On écrit les résultats dans un fichier puis grâce à la libraire *matplotlib*, on affiche la courbe représentant la loi de Zipf appliquée à notre collection.

**Exemple :**
```
Les 10 mots apparaissant le plus souvent et leur fréquence :
('the', 10996)
('of', 9026)
('and', 4495)
('to', 3726)
('is', 3722)
('in', 3427)
('cacm', 3204)
('for', 3160)
('are', 1983)
('algorithm', 1542)

Taille du vocabulaire : 12106
Nombre d'occurrences total : 172933
Valeur théorique de lambda : 18394.277571050316
```

Et voici les courbes que l'on obtient :

![](capture1.png)

![](capture2.png)

### **2ème partie :** construction du vocabulaire

Cette seconde partie permet la création d'un vocabulaire détaillé selon le modèle *tf.idf* et de l'index inversé.

#### - ***remove_common_words.py***

Un script qui permet en premier lieu de supprimer les termes polluants l'analyse (déterminants, pronoms ...). J'ai ajouté un argument à la fonction qui permet à l'utilisateur de décider si oui on non il faut utiliser le *stemmer*, un module *nltk* qui analyse un terme et le remplace par sa racine (par exemple, *computer* deviendra *comput*).

**Méthode :** comme d'habitude, on parcourt les documents de la collection précédemment traitée, puis pour chaque terme rencontré, on invoque ou non le *stemmer* pour trouver la racine du mot, mais surtout on vérifie s'il est un *stop-word* ou non. Si c'est le cas, alors on l'élimine, sinon on le garde en le réécrivant dans un nouveau document (qui constituera la nouvelle collection).
```
if word not in stopList:
  if (stembool == True):
    NoCwFile.write(stemmer.stem(word) + " ")
  else:
    NoCwFile.write(word + " ")
else:
  print("  removing " + word)
```

**Exemple :**
- avant traitement :
```
coordinates
on
an
ellipsoid
algorithm
cacm
september
dorrer
```

- après traitement :
```
coordin ellipsoid algorithm cacm septemb dorrer
```

#### - ***build_voc.py***

C'est le script qui va permettre de construire le dictionnaire selon le modèle *tf.idf* et l'index inversé. J'ai largement commenté le code de ce fichier et je vous renvoie donc vers ce dernier pour prendre connaissance de la méthode que j'ai utilisé.

**Exemple :**
```
"osiri": [1, 3.5056925074122, {"2634": 0.09738034742811666}], "interchang": [28, 2.0585344760699806, {"1922": 0.14703817686214146, "1476": 0.018057319965526144, "1349": 0.033202168968870654, "1289": 0.2287260528966645,
```

On lit le dictionnaire de la manière suivante :
- la racine "osiri"
- apparaît dans un seul et unique document
- et son **idf** vaut 3.505692507412
- elle apparaît dans le document dont l'identifiant est 2634
- avec un **tf.idf** égal à 0.09738034742811666 pour ce document
- ...

### **3ème partie :** recherche et évaluation

Je ne suis pas parvenu à résoudre cette partie (mise à part le chargement des documents et dictionnaires). Le fait d'être en binôme m'aurait probablement été utile pour la fin de ce TP ! J'espère que ce n'est pas trop grave et que le travail que j'ai réalisé vous conviendra tout de même.
