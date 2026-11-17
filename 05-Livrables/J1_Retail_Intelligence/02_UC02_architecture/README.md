# UC-02 Architecture Data

Ce dossier contient la conception de l'architecture Retail Intelligence à partir des résultats vérifiés de UC-01.

## Choix retenu

- Data Lake local organisé en zones Bronze, Silver et Gold.
- Traitements batch avec ingestion NiFi ou repli Python documenté.
- Parquet en Silver et Gold.
- Data marts et modèle dimensionnel en Gold pour les KPI.
- Lakehouse comme évolution facultative.
- Transposition logique vers ADLS Gen2, sans revendiquer un déploiement Azure.

## Livrables

- UC02_comparaison_architectures.pdf
- UC02_architecture_cible.pdf
- UC02_schema_flux.pdf
- UC02_positionnement_composants.pdf
- UC02_gouvernance.pdf
- UC02_local_vers_azure.pdf
- UC02_preuves/
