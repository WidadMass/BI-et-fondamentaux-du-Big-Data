# BI et fondamentaux du Big Data

## TP J1 — Retail Intelligence

**Étudiante : Widad MASGHAR**  
**Formation : Mastère Développement, Data & IA**  
**Travail individuel**  
**Périmètre : UC-01 et UC-02**

## Présentation

Ce dépôt contient le travail réalisé pour le TP du Jour 1 autour du projet
Retail Intelligence. L’objectif est de partir d’un besoin métier retail,
d’examiner les sources réellement disponibles, puis de proposer une première
architecture Data cohérente.

Le travail s’appuie sur le kit de données TPCx-BB fourni dans le projet
`retail_project`, ainsi que sur la documentation TPCx-BB v1.7.0 et le support
du TP.

## Travail réalisé

### UC-01 — Besoin métier et exploration des sources

- identification des utilisateurs et de leurs décisions ;
- formulation des questions décisionnelles ;
- définition initiale des KPI ;
- inventaire des fichiers, volumes, formats et colonnes ;
- vérification de relations entre tables ;
- qualification des données, limites et hypothèses ;
- conservation de preuves sous forme de captures et de fichiers de contrôle.

### UC-02 — Choix et justification d’une architecture Data

- comparaison Data Warehouse, Data Lake et Data Lakehouse ;
- proposition d’une architecture logique cible ;
- description des zones Bronze, Silver et Gold ;
- représentation des flux batch et des traitements d’erreur ;
- positionnement de Python, NiFi, HDFS, PySpark, Parquet et Azure ;
- premières règles de gouvernance, qualité, sécurité et accès ;
- comparaison entre l’architecture locale et une cible Azure logique.

## Architecture retenue

Le choix retenu est un Data Lake local organisé en trois zones :

```text
Sources DAT
    ↓
Ingestion et contrôles
    ↓
Bronze : fichiers originaux et provenance
    ↓
Silver : données typées, contrôlées et harmonisées
    ↓
Gold : faits, dimensions, agrégats et KPI
    ↓
BI et analyses
```

Le traitement est prévu en batch. La cible Azure est décrite de manière
logique avec ADLS Gen2 ; aucun déploiement Azure réel n’est revendiqué dans ce
travail.

## Organisation du dépôt

```text
J1_Retail_Intelligence/
├── README.md
├── 01_UC01_besoin_exploration/
│   ├── UC01_cadrage_metier.pdf
│   ├── UC01_questions_decisionnelles.pdf
│   ├── UC01_dictionnaire_KPI.xlsx
│   ├── UC01_inventaire_sources.xlsx
│   ├── UC01_qualification_donnees.pdf
│   ├── UC01_limites_et_hypotheses.pdf
│   └── UC01_preuves/
└── 02_UC02_architecture/
    ├── UC02_comparaison_architectures.pdf
    ├── UC02_architecture_cible.pdf
    ├── UC02_schema_flux.pdf
    ├── UC02_positionnement_composants.pdf
    ├── UC02_gouvernance.pdf
    ├── UC02_local_vers_azure.pdf
    └── UC02_preuves/
```

## Limites du travail

- l’architecture est une conception logique du Jour 1 ;
- les composants HDFS, NiFi, Spark et Azure ne sont pas présentés comme
  déployés ;
- certains KPI nécessitent encore une validation métier ;
- les identifiants de ligne doivent être complétés pour les faits de ventes et
  de retours lorsque les clés métier ne sont pas uniques ;
- la version exacte du kit de données reste à confirmer séparément de la
  version de la documentation TPCx-BB.

## Auteur

Widad MASGHAR — travail individuel réalisé dans le cadre du TP J1.
    
