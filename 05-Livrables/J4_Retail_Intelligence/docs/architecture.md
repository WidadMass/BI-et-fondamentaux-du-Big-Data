# Schéma d’architecture TP4

```text
Source promotion.dat
        |
        v
ADLS Gen2 : Bronze/tpcxbb
        |
        v
Spark / PySpark dans Docker ou Synapse Spark (cible)
        |
        +--> ADLS Gen2 : Silver/promotion
        |          |
        |          +--> contrôles qualité
        |
        +--> ADLS Gen2 : Gold/promotion_summary
                   |
                   +--> Jupyter / Matplotlib
                   +--> Power BI (extension étudiée)
```

Les zones Bronze, Silver et Gold sont réellement présentes dans le compte ADLS
`retailtp4widad2026`. Spark et PySpark ont été exécutés dans Docker. Synapse,
Data Factory et Power BI apparaissent dans le schéma comme composants cibles et
ne sont pas présentés comme déployés.
