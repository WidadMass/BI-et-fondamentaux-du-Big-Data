# Architecture Lakehouse proposée

```text
Sources métier
     |
     v
NiFi / ingestion contrôlée
     |
     v
Bronze : données brutes et traçables
     |
     v
PySpark : nettoyage, typage, dédoublonnage
     |
     v
Silver : données harmonisées en Parquet
     |
     v
Delta Lake : journal ACID, versions, évolution de schéma
     |
     +-----------------------+
     |                       |
     v                       v
Gold analytique          Contrôles qualité
     |                       |
     v                       v
BI / reporting           Alertes et audit
```

Le stockage objet ou HDFS conserve les fichiers physiques. Le format de table Delta fournit la couche transactionnelle et les métadonnées. Spark exécute les transformations et les lectures analytiques.

