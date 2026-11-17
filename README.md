# BI et fondamentaux du Big Data - Retail Intelligence

Travail realise par **Widad MASGHAR** dans le cadre du TP fil rouge Retail Intelligence.

## Organisation du depot

- `01-Cours/` : support de cours utilise pour le travail.
- `02-TP/` : enonce du TP et liste des livrables du Jour 1.
- `03-DataSet_Source-de-donnees/` : informations sur le jeu de donnees Retail.
- `04-Annexes/` : documents de reference et schema des tables principales.
- `05-Livrables/` : rendus des UC-01 a UC-04, avec les preuves demandees.

## Contenu du rendu

Le dossier `05-Livrables/J1_Retail_Intelligence/` contient :

- UC-01 : cadrage metier, questions decisionnelles, dictionnaire des KPI, inventaire des sources, qualification des donnees, limites et hypotheses, preuves ;
- UC-02 : comparaison des architectures, architecture cible, schema des flux, positionnement des composants, gouvernance, passage du local vers Azure, preuves.

Le dossier `05-Livrables/J2_Retail_Intelligence/` contient :

- UC-03 : environnement Hadoop/HDFS, inventaire des sources, arborescence du Data Lake, depot et controles de stockage ;
- UC-04 : flux NiFi `GetFile -> PutHDFS`, configuration, execution, provenance, erreurs et corrections ;
- partie complementaire : approfondissements sur les blocs HDFS, la convention de nommage, l'integrite, la supervision et la reprise ;
- partie avancee AV-04 : controles avant ingestion avec routage des fichiers valides vers HDFS et des fichiers invalides vers le dossier error ;
- fichiers PDF finaux et captures de preuves.

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
