# TP4 - Analyse décisionnelle et architectures Data

## Périmètre réalisé

- UC08 : exploration du Silver et du Gold issus de l'UC06, statistiques descriptives, deux analyses métier et deux visualisations Matplotlib ;
- UC07 : architecture Azure proposée, organisation ADLS Gen2 Bronze/Silver/Gold, HNS, sécurité et distinction entre réalisé et simulé ;
- exécution locale reproductible dans Docker avec Spark, PySpark, Pandas et Matplotlib.

## Reproduction

Depuis la racine du dépôt :

```powershell
docker compose -f .\docker-compose.tp3.yml build spark-uc06
docker compose -f .\docker-compose.tp3.yml up -d spark-uc06
docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/scripts/tp4_uc08.py
```

Le notebook `notebooks/TP4_Retail_Intelligence.ipynb` reprend les mêmes calculs. Les sorties sont produites dans `analytics/outputs` et `analytics/visualizations`.

## Données et limites

Les données sont l'extrait synthétique `promotion.dat`, transformé en Silver (300 lignes, 19 champs) et Gold (9 catégories de `field_07`). Les noms `field_00` à `field_18` sont techniques car la source ne fournit pas d'en-tête métier. Les analyses portent donc sur les champs réellement disponibles et ne prétendent pas mesurer un chiffre d'affaires ou des ventes magasin.

## Preuves attendues

- sortie notebook exécutée : volumes, schéma et contrôles qualité ;
- tableau de statistiques descriptives ;
- graphique des promotions par catégorie technique ;
- histogramme de `field_05` ;
- documentation UC07 : architecture, ADLS/HNS, sécurité et simulation locale.
