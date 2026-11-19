# TP4 – UC08 Analyse décisionnelle et UC07 Azure

## Parcours réalisé

Le parcours Azure a été réalisé avec l’offre **Azure for Students**. Les ressources
ont été créées depuis Azure CLI exécutée dans Docker.

## Ressources déployées

| Ressource | Valeur |
|---|---|
| Abonnement | Azure for Students |
| Groupe de ressources | `rg-retail-intelligence` |
| Région | `francecentral` |
| Compte ADLS Gen2 | `retailtp4widad2026` |
| Système de fichiers | `retail-intelligence` |
| HNS | Activé |
| TLS minimal | TLS 1.2 |
| Réplication | Standard_LRS |

## Organisation ADLS

```text
retail-intelligence/
├── bronze/tpcxbb/
├── silver/promotion/
├── gold/promotion_summary/
├── quality/
└── documentation/
```

Les preuves et commandes sont décrites dans `docs/azure-implementation.md`.
La matrice des droits est présentée dans `docs/securite.md`.
L’inventaire des données est présenté dans `docs/inventaire-donnees.md`.
Le dictionnaire des KPI calculables est présenté dans `docs/dictionnaire-kpi.md`.
Les analyses métier, limites et recommandations sont présentées dans
`docs/analyse-metier.md`.
La comparaison des services et le schéma sont disponibles dans
`docs/comparaison-services.md` et `docs/architecture.md`.

## Données utilisées

Les jeux Silver et Gold produits dans l’UC06 sont documentés dans
`docs/inventaire-donnees.md`. Le fichier source `promotion.dat` a été déposé dans
Bronze et les fichiers Parquet Silver/Gold ont été déposés dans leurs zones.

## Limites

Azure Data Factory, Synapse Analytics et Power BI ne sont pas déployés dans cette
étape. Ils sont étudiés comme composants cibles de l’architecture. Les analyses
locales Spark/Jupyter et les visualisations Matplotlib restent reproductibles dans
Docker.

## UC08 – Analyse et reproduction

Le notebook `notebooks/TP4_Retail_Intelligence.ipynb` a été exécuté dans le
conteneur `retail-uc06-spark`. Les sorties sont conservées dans :

- `analytics/outputs/statistiques.csv` ;
- `analytics/outputs/kpi_par_categorie.csv` ;
- `analytics/outputs/distribution_field_05.csv` ;
- `analytics/visualizations/promotions_par_categorie.png` ;
- `analytics/visualizations/distribution_field_05.png`.

Le dossier de synthèse PDF est disponible dans
`output/pdf/TP4_Retail_Intelligence.pdf`. Il regroupe les résultats, les analyses,
les droits d'accès et les captures de preuve Azure et Spark.

Reproduction du script :

```powershell
docker compose -f .\docker-compose.tp3.yml up -d spark-uc06
docker exec retail-uc06-spark /opt/spark/bin/spark-submit --master local[2] /opt/project/tp4/scripts/tp4_uc08.py
```

La sortie attendue est de 300 lignes Silver, 9 lignes Gold, 9 catégories et une
moyenne `field_05` de 521,23.

## Preuves à conserver

1. création du groupe de ressources Azure ;
2. compte ADLS Gen2 avec `isHnsEnabled: true` et `minimumTlsVersion: TLS1_2` ;
3. arborescence Bronze/Silver/Gold ;
4. fichiers Parquet et `promotion.dat` déposés ;
5. rôle RBAC `Storage Blob Data Contributor` ;
6. ACL Bronze, Silver et Gold ;
7. sortie du script et notebook exécuté ;
8. les deux visualisations.
