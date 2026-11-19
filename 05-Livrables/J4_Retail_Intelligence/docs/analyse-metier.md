# Analyses métier UC08

## Analyse 1 - catégories de promotion

Question : quelles catégories techniques de `field_07` concentrent le plus de lignes de promotion ?

Méthode : lecture du Gold `promotion_summary`, tri décroissant de `promotion_count`, puis export d'un tableau CSV et d'un graphique en barres.

Interprétation : les catégories sont comparées selon le nombre de promotions observées dans l'extrait. Ce résultat décrit une fréquence dans le jeu synthétique ; il ne permet pas de conclure sur des ventes, une performance magasin ou une causalité commerciale.

## Analyse 2 - distribution de field_05

Question : comment les valeurs numériques de `field_05` sont-elles distribuées dans le Silver ?

Méthode : calcul Spark du minimum, maximum, moyenne et médiane, puis transfert du petit résultat dans Pandas pour produire un histogramme.

Interprétation : l'histogramme montre la dispersion des valeurs présentes. La source ne fournit pas de définition métier fiable de `field_05`, donc l'unité et la signification commerciale restent à confirmer.

## Limites

- l'extrait est synthétique et ne contient pas d'en-tête métier ;
- les champs `field_00` à `field_18` sont des noms techniques ;
- aucune analyse temporelle ou par magasin n'est affirmée car les colonnes nécessaires ne sont pas qualifiées dans le schéma disponible ;
- les résultats sont descriptifs et ne prouvent pas une relation causale.
