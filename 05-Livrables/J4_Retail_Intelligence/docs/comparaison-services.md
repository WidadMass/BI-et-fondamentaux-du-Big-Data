# Comparaison Azure / local open source

| Fonction | Azure | Parcours local retenu | État dans le TP4 | Limite de l’équivalence |
|---|---|---|---|---|
| Stockage Data Lake | ADLS Gen2 | Répertoires Docker et Parquet | ADLS déployé, local utilisé pour les traitements | ADLS fournit une gouvernance cloud intégrée |
| Organisation hiérarchique | HNS ADLS Gen2 | Arborescence locale | HNS activé et vérifié | Les ACL locales ne reproduisent pas totalement Azure |
| Ingestion/orchestration | Azure Data Factory | Scripts Docker et Docker Compose | ADF étudié, scripts réalisés | Pas de pipeline graphique ni de supervision ADF |
| Traitement distribué | Synapse Spark Pools | Apache Spark / PySpark | Spark exécuté dans Docker | Pas de cluster managé ni d’élasticité cloud |
| Requêtes analytiques | Synapse SQL | Spark SQL / DataFrame | Spark utilisé | Pas de service SQL serverless déployé |
| Format de stockage | Parquet/Delta sur ADLS | Parquet | Parquet utilisé | Iceberg et Delta ne sont pas nécessaires au socle TP4 |
| Catalogue de tables | Purview ou catalogue Synapse | Arborescence et documentation Git | Documentation utilisée | Pas de catalogue de données Azure déployé |
| Restitution | Power BI | Jupyter et Matplotlib | Matplotlib utilisé | Pas de tableau de bord Power BI dans ce livrable |

## Responsabilités des composants

- ADLS Gen2 stocke les zones Bronze, Silver et Gold ;
- Data Factory déplacerait les données et orchestrerait les traitements ;
- Synapse fournirait l’environnement analytique et les capacités SQL/Spark ;
- Spark exécute les transformations PySpark ;
- Parquet matérialise les jeux de données analytiques ;
- Power BI pourrait consommer les jeux Gold pour un tableau de bord.

Le TP4 a donc une réalisation Azure réelle pour le stockage, HNS, les données et
la sécurité. Les services ADF, Synapse et Power BI sont documentés comme extensions
possibles, sans prétendre avoir été déployés.
