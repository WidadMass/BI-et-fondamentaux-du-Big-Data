# Inventaire technique

La source exploitee pour la demonstration UC06 est `retail_project/data/promotion/promotion.dat`.

- format : texte delimite par `|` ;
- en-tete : absent ;
- volume du fichier : 46 396 octets ;
- volume traite : 300 lignes ;
- schema technique : 19 champs nommes `field_00` a `field_18` ;
- traitements : typage des champs numeriques, suppression des lignes sans identifiant et des doublons.

Les autres tables du jeu de donnees sont conservees dans `retail_project/data` et pourront etre traitees avec le meme patron de transformation.

La granularite retenue est une ligne par promotion technique. `field_00` est utilise comme identifiant candidat : il ne contient ni valeur nulle ni doublon sur l extrait traite.
