# UC07 - Architecture Azure / ADLS Gen2

## Proposition cible

Les fichiers sources arrivent dans un compte ADLS Gen2 organisé en zones Bronze, Silver et Gold. Azure Data Factory orchestre les déplacements et déclenchements. Un environnement Spark (Synapse Spark ou équivalent) transforme les données. Synapse SQL ou un export contrôlé expose les résultats à la restitution.

```text
Sources TPCx-BB -> ADF -> ADLS Gen2 Bronze -> Spark/Synapse -> ADLS Gen2 Silver -> Spark/Synapse -> Gold -> Power BI/exports
```

## Organisation et HNS

- `bronze/` : données brutes conservées ;
- `silver/` : données nettoyées et harmonisées ;
- `gold/` : agrégats et jeux prêts pour l'analyse ;
- HNS : active une arborescence de répertoires et facilite les ACL sur les chemins.

## Sécurité

RBAC contrôle l'accès à la ressource ou au compte ; les ACL affinent les droits sur les répertoires et fichiers. Le principe du moindre privilège s'applique aux identités, aux zones et aux comptes de service. Les secrets ne doivent jamais être déposés dans Git.

## Réalisé et simulé

Réalisé : traitement local Docker/Spark, sorties Silver/Gold Parquet et analyses UC08. Simulé/documenté : compte ADLS Gen2, HNS, ADF, Synapse et Power BI ; aucun déploiement Azure n'a été effectué dans ce TP.
