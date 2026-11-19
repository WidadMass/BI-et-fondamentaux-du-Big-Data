# Partie avancée — Lakehouse et Delta Lake

Cette partie facultative prolonge l’UC06 avec une démonstration technique de Delta Lake, sans modifier le traitement PySpark obligatoire déjà validé.

## Environnement

- Image officielle : `deltaio/delta-docker:4.3.1`
- Delta Lake : 4.3.1
- Apache Spark : 4.1.1
- Java : 21
- Conteneur : `retail-advanced-delta`
- JupyterLab : <http://localhost:8889/lab?token=delta-retail>

## Exécution

Depuis la racine du dépôt :

```powershell
docker compose -f .\docker-compose.tp3-advanced.yml up -d
docker exec retail-advanced-delta bash -lc '/opt/spark/bin/spark-submit --packages io.delta:delta-spark_4.1_2.13:4.3.1 --conf spark.driver.extraJavaOptions="-Divy.cache.dir=/tmp -Divy.home=/tmp" --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog /opt/project/output/transformations/delta_demo.py'
```

## Résultats attendus

- version 0 : 300 lignes issues de Silver ;
- version 1 : 301 lignes après ajout incrémental ;
- ajout de la colonne `source_system` avec `mergeSchema` ;
- historique contenant les opérations `WRITE` ;
- lecture de la version 0 par time travel ;
- présence du journal transactionnel `_delta_log`.

Les explications conceptuelles sont dans le dossier `docs/` et les données Delta dans `data/delta/`.

## Preuves à capturer

1. `docker compose -f .\docker-compose.tp3-advanced.yml ps` montrant le conteneur actif.
2. La fin de l’exécution affichant les versions 0 et 1, les comptes 300 et 301 et `RESULTAT : demonstration Delta validee`.
3. Le contenu du dossier `data/delta/promotion/_delta_log`.
4. JupyterLab ouvert sur le port 8889, si une preuve visuelle de l’environnement est souhaitée.

