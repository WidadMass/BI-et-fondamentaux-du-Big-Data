# UC06 Transformation et Data Lakehouse

## Objectif

Cette UC lit `promotion.dat`, applique des controles de nettoyage, produit une couche Silver, une couche Gold et un rapport de qualite. Le traitement est execute avec PySpark dans Docker.

## Structure

- `docs/` : environnement, inventaire et regles de nettoyage ;
- `notebooks/exploration/` : exploration et premiers controles ;
- `transformations/` : scripts PySpark Silver et Gold ;
- `data/silver/` : donnees nettoyees au format Parquet ;
- `data/gold/` : agregats analytiques au format Parquet ;
- `quality/` : controles de qualite au format JSON ;
- `tests/` : tests de coherence des sorties ;
- `outputs/` : journaux ou exports supplementaires.

Les captures JupyterLab et notebook execute sont conservees dans `outputs/proofs/` et integrees au PDF final.

## Reproduction avec Docker

Depuis la racine du depot :

```powershell
docker compose -f .\docker-compose.tp3.yml up -d
docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/scripts/run_uc06.py
docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/tests/verify_outputs.py
```

JupyterLab est accessible sur `http://localhost:8888/lab?token=uc06-retail`. Le notebook se trouve dans `notebooks/exploration/UC06_exploration.ipynb`.

Execution non interactive du notebook :

```powershell
docker exec retail-uc06-spark jupyter nbconvert --to notebook --execute /opt/project/notebooks/exploration/UC06_exploration.ipynb --inplace --ExecutePreprocessor.timeout=180
```

Verification :

```powershell
Get-ChildItem .\05-Livrables\J3_Retail_Intelligence\06_UC06\data -Recurse
Get-ChildItem .\05-Livrables\J3_Retail_Intelligence\06_UC06\quality -Recurse
```

Resultats observes : 300 lignes en Silver, 9 groupes en Gold, 0 identifiant nul et 0 doublon. Les fichiers Parquet sont relus, leur schema est controle et leurs volumes sont compares aux resultats avant ecriture.
