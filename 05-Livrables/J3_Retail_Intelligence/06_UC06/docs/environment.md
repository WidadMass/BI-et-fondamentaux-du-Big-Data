# Environnement

Le traitement est execute dans le conteneur `retail-uc06-spark` defini par `docker-compose.tp3.yml`.

| Composant | Version ou configuration |
|---|---|
| Image de base | `apache/spark:4.3.0-python3` |
| Image projet | `retail-uc06-spark-jupyter:4.3.0` |
| Spark | 4.3.0 |
| Java | 21.0.13 LTS dans le conteneur |
| JupyterLab | 4.6.6, port local 8888 |
| Execution | `local[2]` |
| Entree | `/opt/project/input/promotion/promotion.dat` |
| Sortie | `/opt/project/output/` |
