# Questions de recul

## 1 Pourquoi verifier les schemas avant les transformations

Le schema indique les colonnes, les types et les valeurs nulles possibles. Sans cette verification, une somme peut etre appliquee a une chaine de caracteres, une date peut etre mal interpretee ou une colonne attendue peut manquer. La verification evite des resultats techniquement executes mais faux.

## 2 Difference entre donnees brutes, Silver et Gold

La donnee brute conserve la source sans transformation. La couche Silver contient des donnees nettoyees, typees et controlees. La couche Gold contient des jeux derives et agreges pour un besoin analytique precis.

## 3 Pourquoi connaitre la granularite avant une agregation

La granularite definit ce que represente une ligne. Sans elle, une aggregation peut compter plusieurs fois le meme evenement ou melanger des niveaux differents. Le resultat devient alors impossible a interpreter correctement.

## 4 Risques d une jointure sur une cle supposee

Une cle non verifiee peut contenir des doublons, des valeurs nulles ou des valeurs absentes dans l autre table. La jointure peut multiplier les lignes, perdre des enregistrements ou attribuer une information au mauvais objet.

## 5 Pourquoi ne pas supprimer automatiquement les valeurs atypiques

Une valeur extreme peut etre une erreur, mais aussi un comportement reel et important. Sa suppression sans analyse peut masquer une fraude, une promotion exceptionnelle ou un probleme de qualite. Elle doit d abord etre signalee et confrontee aux regles metier.

## 6 Controles de coherence apres transformation

Il faut comparer les volumes avant et apres, verifier les schemas, compter les valeurs nulles et les doublons, controler les cles candidates, verifier les plages de valeurs et relire les fichiers produits. Les aggregats doivent aussi etre rapproches des donnees sources.

## 7 Pourquoi Parquet convient aux usages analytiques

Parquet stocke les donnees par colonnes, compresse efficacement les valeurs similaires et conserve le schema. Un moteur analytique peut donc lire uniquement les colonnes necessaires et reduire les entrees sorties.

## 8 Pourquoi Parquet seul n est pas une table transactionnelle Lakehouse

Parquet decrit des fichiers, mais ne fournit pas a lui seul de journal de transactions, de gestion coherente des mises a jour, d historique de versions ou de concurrence. Ces garanties necessitent un format de table comme Delta Lake, Iceberg ou Hudi et ses metadonnees.

## 9 Quand NoSQL complete un Data Lake

NoSQL est pertinent lorsqu une application doit retrouver rapidement un enregistrement par cle, ingerer des evenements a forte frequence ou gerer une structure flexible. Le Data Lake reste mieux adapte au stockage historique et aux analyses globales.

## 10 Limites des donnees TPCx BB

TPCx-BB est un jeu de benchmark et non une observation exhaustive d une entreprise reelle. Les valeurs, volumes et relations peuvent etre synthetiques. Les resultats servent a valider une chaine technique, mais ne doivent pas etre generalises en conclusions commerciales sans contexte metier.
