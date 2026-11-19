# Partie avancée - Industrialisation Azure

## Cible

La partie avancée consiste à remplacer l'exécution manuelle Docker par une
chaîne Azure automatisée : Data Factory orchestre le traitement et Synapse
Spark exécute la transformation.

```text
ADLS Bronze -> Data Factory -> Synapse Spark -> ADLS Silver -> Gold -> Power BI
```

## Composants prévus

| Composant | Rôle |
|---|---|
| ADLS Gen2 | stockage Bronze, Silver, Gold |
| Azure Data Factory | déclenchement et orchestration |
| Azure Synapse Workspace | exécution Spark et exploration SQL |
| Power BI | restitution des KPI Gold |
| Azure Monitor | suivi des exécutions et erreurs |

## Pipeline proposé

1. Déclencheur manuel ou planifié.
2. Vérification de la présence de `bronze/tpcxbb/promotion.dat`.
3. Notebook ou job Synapse de nettoyage vers `silver/promotion/`.
4. Agrégation Gold vers `gold/promotion_summary/`.
5. Contrôle des volumes et de la qualité.
6. Actualisation du dataset Power BI.

## Contrôles d'acceptation

- Silver : 300 lignes et 19 colonnes ;
- Gold : 9 catégories et 300 observations agrégées ;
- aucun identifiant nul ;
- aucun doublon sur la clé contrôlée ;
- fichiers Parquet relisibles ;
- échec visible dans le journal Azure Monitor.

## Déploiement prudent

La création d'un workspace Synapse et d'un pipeline Data Factory n'est pas faite
automatiquement dans ce dépôt, car ces services peuvent consommer le crédit
Azure for Students. Le stockage ADLS et les résultats Spark sont déjà réalisés.
Avant tout déploiement, vérifier le crédit restant, la région autorisée et la
suppression des ressources après la démonstration.
