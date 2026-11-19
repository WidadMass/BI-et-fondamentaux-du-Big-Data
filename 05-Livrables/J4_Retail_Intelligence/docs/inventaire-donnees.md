# Inventaire des données du TP4

## Source Bronze

| Élément | Valeur |
|---|---|
| Nom | `promotion.dat` |
| Provenance | Extrait synthétique TPCx-BB du dépôt |
| Chemin local | `retail_project/data/promotion/promotion.dat` |
| Chemin ADLS | `bronze/tpcxbb/promotion.dat` |
| Format | Texte séparé par `|`, sans en-tête |
| Volume | 46 396 octets, 300 lignes |
| Granularité | Une observation par ligne source |

La source contient 19 colonnes techniques nommées `field_00` à `field_18`.
Elle ne fournit pas de dictionnaire métier associé.

## Jeu Silver

| Élément | Valeur |
|---|---|
| Nom | `silver/promotion` |
| Provenance | Transformation PySpark de l’UC06 |
| Format | Parquet Snappy |
| Volume | 300 lignes, 19 colonnes |
| Granularité | Une ligne nettoyée par observation conservée |
| Utilisation | Statistiques et distribution de `field_05` |
| Chemin ADLS | `silver/promotion/` |

Contrôles appliqués : lecture avec le séparateur `|`, suppression des doublons
exacts, contrôle de `field_00`, conversions de types, comparaison des volumes et
relecture du schéma Parquet.

## Jeu Gold

| Élément | Valeur |
|---|---|
| Nom | `gold/promotion_summary` |
| Provenance | Agrégation PySpark du Silver dans l’UC06 |
| Format | Parquet Snappy |
| Volume | 9 lignes |
| Granularité | Une ligne par valeur de `field_07` |
| Mesure | `promotion_count` |
| Chemin ADLS | `gold/promotion_summary/` |

Le Gold est adapté à une analyse de répartition par catégorie technique. Il ne
permet pas de conclure sur le chiffre d’affaires ou la performance commerciale,
car `field_07` n’est pas qualifié métier.

## Qualité et limites

Le contrôle qualité disponible indique :

- 300 lignes source ;
- 300 lignes Silver ;
- 9 lignes Gold ;
- 0 identifiant nul ;
- 0 doublon détecté ;
- schéma Parquet relu après écriture.

Ces contrôles sont techniques. Une validation métier des noms de colonnes, unités,
clés et indicateurs reste nécessaire.
