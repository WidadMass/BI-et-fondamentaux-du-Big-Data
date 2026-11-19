# Partie complémentaire - Tableau de bord Power BI

## Objectif

Construire un tableau de bord à partir du fichier Gold `kpi_par_categorie.csv`.
Le fichier est exporté par le traitement UC08 et contient une ligne par catégorie
technique `field_07`.

Source locale : `analytics/outputs/kpi_par_categorie.csv`

Source cloud cible : `abfss://retail-intelligence@retailtp4widad2026.dfs.core.windows.net/gold/promotion_summary/`

## Import dans Power BI

1. Ouvrir Power BI Desktop.
2. Choisir **Obtenir les données > Texte/CSV**.
3. Sélectionner `analytics/outputs/kpi_par_categorie.csv`.
4. Vérifier les types : `field_07` en texte, `promotion_count` en entier,
   `average_cost` en nombre décimal.
5. Renommer la table `KPI_Categorie`.

Pour une connexion Azure, utiliser le connecteur **Azure Data Lake Storage Gen2**
avec le chemin du filesystem et le dossier Gold. L'accès doit être réalisé avec
un compte autorisé par RBAC/ACL ; aucune clé ni secret ne doit être enregistré
dans Git.

## Mesures DAX

```DAX
Nombre de promotions = SUM(KPI_Categorie[promotion_count])

Nombre de catégories = DISTINCTCOUNT(KPI_Categorie[field_07])

Moyenne du coût technique = AVERAGE(KPI_Categorie[average_cost])

Catégorie principale =
CONCATENATEX(
    TOPN(1, ALL(KPI_Categorie[field_07]), [Nombre de promotions], DESC),
    KPI_Categorie[field_07],
    ", "
)
```

La mesure `Moyenne du coût technique` doit rester présentée comme un indicateur
technique : l'unité métier de `field_05` n'est pas connue.

## Visuels attendus

- cartes : nombre de promotions, nombre de catégories, moyenne technique ;
- histogramme : `field_07` en axe et `promotion_count` en valeur ;
- histogramme : distribution de `average_cost` par catégorie ;
- segment (slicer) sur `field_07` ;
- titre indiquant « TP4 - Retail Intelligence - Gold promotion_summary ».

## Résultats de référence

- 300 promotions au total ;
- 9 catégories ;
- catégorie la plus fréquente : `able` avec 37 lignes ;
- catégorie la moins fréquente : `ese` avec 27 lignes.

Ces valeurs doivent être visibles dans le rapport après actualisation.
