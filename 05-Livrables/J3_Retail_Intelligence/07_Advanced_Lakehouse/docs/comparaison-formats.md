# Comparaison Parquet, Delta Lake, Iceberg et Hudi

| Critère | Parquet seul | Delta Lake | Apache Iceberg | Apache Hudi |
|---|---|---|---|---|
| Nature | Format de fichier colonne | Format de table Lakehouse | Format de table ouvert | Format de table Lakehouse |
| Transactions ACID | Non | Oui | Oui | Oui |
| Historique et time travel | Non natif | Oui | Oui | Oui |
| Évolution de schéma | À gérer hors format | Oui | Oui | Oui |
| Upsert / merge | Non natif | Oui | Oui selon moteur | Point fort |
| Cas d’usage dominant | Stockage analytique simple | Pipelines Spark et Lakehouse | Tables multi-moteurs | Ingestion incrémentale rapide |

Parquet reste le format physique des fichiers dans plusieurs solutions Lakehouse. Seul, il ne fournit cependant ni journal de transactions, ni version cohérente de la table, ni mécanisme standard de concurrence. Delta Lake ajoute un journal `_delta_log` qui décrit les versions et les opérations atomiques appliquées aux fichiers Parquet.

Delta est retenu ici parce que la démonstration utilise Spark et que ses fonctions d’historique, d’évolution de schéma et de time travel sont directement vérifiables dans le même environnement.

