## **README**

###### Julien Cordat-Auclair, **INFO4**.
*Lien du sujet sur la page **https://hmul8r6b.imag.fr/doku.php***.

--------------------------------------------------------------------------------

Les scripts sont exécutés sous ***python 3.6*** sur ma machine. Si vous n'avez pas cette version, il faudra modifier les entêtes de chacun des scripts (sans garantie que tout fonctionnera correctement).

--------------------------------------------------------------------------------

- ***split_cacm.py*** : permet de traiter la librairie de documents en séparant les fichiers, en les organisant selon une sémantique précise et en les rangeant dans un dossier spécifique avec un nom unique.
Les documents créés suite à l'exécution de ce script se trouvent dans `TP1/Collection/Init`.

- ***tokenize_cacm.py*** : permet de *tokeniser* les documents de la collection, c'est-à-dire d'enlever les chiffres et les symboles, de remplacer les majuscules par des minuscules et d'afficher un mot par ligne.
Les documents créés suite à l'exécution de ce script se trouvent dans `TP1/Collection/Token`.

- ***zipf.py*** : permet d'analyser les documents dans leur ensemble et notamment de relever les 10 termes apparaissant le plus souvent parmi eux ainsi que leur fréquence d'apparition, mais aussi de visualiser la loi de Zipf associée.
Le fichier créé suite à l'exécution de ce script se trouve dans `TP1/Collection/Zipf` et se nomme `results.txt`.
Les courbes s'affichent quant à elles instantanément lorsque l'utilisateur exécute le script (elles ne sont pas sauvegardées).

- ***remove_common_words*** : permet de supprimer les mots communs (*for*, *and*, *to*, *be* ... tous les mots qui risqueraient de polluer l'analyse) des documents.
Les documents créés suite à l'exécution de ce script se trouvent dans `TP2/Collection/NoCommonWords`.

- ***build_voc.py*** : permet de constituer le vocabulaire formé par le contenu de tous les documents de la collection, notamment selon le modèle *tf.idf* et l'index inversé.
Le fichier créé suite à l'exécution de ce script se trouve dans `TP2/Collection/Vocabulary` et se nomme `vocabulary.json`.

--------------------------------------------------------------------------------
