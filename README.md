# BI et fondamentaux du Big Data - Retail Intelligence

Travail realise par **Widad MASGHAR** dans le cadre du TP fil rouge Retail Intelligence.

## Organisation du depot

- `01-Cours/` : support de cours utilise pour le travail.
- `02-TP/` : enonce du TP et liste des livrables du Jour 1.
- `03-DataSet_Source-de-donnees/` : informations sur le jeu de donnees Retail.
- `04-Annexes/` : documents de reference et schema des tables principales.
- `05-Livrables/` : rendus des UC-01 a UC-06, avec les preuves demandees.

## Contenu du rendu

Le dossier `05-Livrables/J1_Retail_Intelligence/` contient :

- UC-01 : cadrage metier, questions decisionnelles, dictionnaire des KPI, inventaire des sources, qualification des donnees, limites et hypotheses, preuves ;
- UC-02 : comparaison des architectures, architecture cible, schema des flux, positionnement des composants, gouvernance, passage du local vers Azure, preuves.

Le dossier `05-Livrables/J2_Retail_Intelligence/` contient :

- UC-03 : environnement Hadoop/HDFS, inventaire des sources, arborescence du Data Lake, depot et controles de stockage ;
- UC-04 : flux NiFi `GetFile -> PutHDFS`, configuration, execution, provenance, erreurs et corrections ;
- partie complementaire : approfondissements sur les blocs HDFS, la convention de nommage, l'integrite, la supervision et la reprise ;
- partie avancee AV-04 : controles avant ingestion avec routage des fichiers valides vers HDFS et des fichiers invalides vers le dossier error ;
- questions de recul, ecart de version NiFi et gestion des erreurs integres directement dans les livrables UC-03 et UC-04 ;
- fichiers PDF finaux et captures de preuves.

Les livrables UC-03 et UC-04 integrent les reponses aux questions de recul et documentent l'ecart entre la version NiFi demandee (2.12.0) et la version observee dans les captures (1.28.1). Les preuves finales montrent aussi la relation `failure` geree et l'evenement de provenance `SEND` montrant le transit vers HDFS.

Le dossier `05-Livrables/J3_Retail_Intelligence/05_UC05/` contient :

- UC-05 facultative : comparaison des familles NoSQL, notions HBase, modele `products`, Row Key `item_id`, comparaison avec HDFS et Parquet, avantages, limites et question de recul ;
- HBase n'etant pas disponible dans l'environnement utilise, aucune demonstration operationnelle n'est revendiquee.

Le dossier `05-Livrables/J3_Retail_Intelligence/06_UC06/` contient :

- le traitement PySpark execute dans Docker ;
- une sortie Silver en Parquet (`data/silver/promotion`) ;
- une sortie Gold agregee en Parquet (`data/gold/promotion_summary`) ;
- les controles de qualite (`quality/promotion_quality`).

Le dossier `05-Livrables/J3_Retail_Intelligence/07_Advanced_Lakehouse/` contient :

- une comparaison de Parquet, Delta Lake, Iceberg et Hudi ;
- une architecture Lakehouse et une strategie incrementale ;
- une demonstration Delta Lake 4.3.1 avec Spark 4.1.1 ;
- une evolution de schema controlee avec `mergeSchema` ;
- deux versions de table, un time travel vers la version 0 et le journal `_delta_log`.

## Demarrage du Jour 3 avec Docker

Depuis la racine du depot :

```powershell
docker compose -f .\docker-compose.tp3.yml up -d
docker compose -f .\docker-compose.tp3.yml ps
docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/scripts/run_uc06.py
docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/tests/verify_outputs.py
```

JupyterLab UC-06 : `http://localhost:8888/lab?token=uc06-retail`.

Le conteneur `retail-uc06-spark` est independant des conteneurs HDFS et NiFi du Jour 2. Il monte les donnees brutes en lecture seule et ecrit les resultats UC-06 dans `05-Livrables/J3_Retail_Intelligence/06_UC06/`.

## Partie avancee Delta Lake

Cette partie utilise un second conteneur afin de conserver intact l'environnement UC-06 obligatoire :

```powershell
docker compose -f .\docker-compose.tp3-advanced.yml up -d
docker exec retail-advanced-delta bash -lc '/opt/spark/bin/spark-submit --packages io.delta:delta-spark_4.1_2.13:4.3.1 --conf spark.driver.extraJavaOptions="-Divy.cache.dir=/tmp -Divy.home=/tmp" --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog /opt/project/output/transformations/delta_demo.py'
```

JupyterLab Delta : `http://localhost:8889/lab?token=delta-retail`.

## Demarrage du Jour 2

Depuis la racine du depot :

```powershell
docker compose -f .\docker-compose.uc03.yml up -d
docker compose -f .\docker-compose.uc03.yml ps
```

Interfaces locales :

- HDFS : `http://localhost:9870` ;
- NiFi : `https://localhost:8443/nifi`.

Chemins principaux :

- entree NiFi : `/data/nifi/input` ;
- destination HDFS UC-03 : `/retail-lake/raw/tpcxbb/initial` ;
- destination HDFS UC-04 : `/retail-lake/raw/nifi`.

Verification UC-04 :

```powershell
docker exec retail-uc03-hdfs hdfs dfs -ls -h /retail-lake/raw/nifi
docker exec retail-uc03-hdfs hdfs dfs -cat /retail-lake/raw/nifi/promotion.dat | Select-Object -First 3
```

## Controle avance AV-04

Le flux NiFi applique deux controles avant le depot :

- extension `.dat` ;
- taille strictement superieure a zero.

Le flux est organise ainsi :

```text
GetFile -> RouteOnAttribute
             |-- matched -> PutHDFS
             |-- unmatched -> PutFile
```

Les fichiers non conformes sont places dans `/data/nifi/error`. Les preuves comprennent la configuration des expressions, un depot valide dans HDFS et le rejet de `test.txt`.

Arret :

```powershell
docker compose -f .\docker-compose.uc03.yml stop
```

## Jeu de donnees

Le projet utilise le jeu de donnees `retail_project`, inspire du benchmark TPCx-BB. Les donnees brutes et leur archive ne sont pas versionnees en raison de leur volume. Les inventaires, controles et echantillons necessaires a la justification du travail sont fournis dans les dossiers de preuves de l'UC-01.

