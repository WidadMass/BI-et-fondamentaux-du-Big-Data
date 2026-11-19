from pathlib import Path

from pyspark.sql import SparkSession, functions as F

ROOT = Path("/opt/project/tp4")
SILVER = Path("/opt/project/output/data/silver/promotion")
GOLD = Path("/opt/project/output/data/gold/promotion_summary")
OUT_DATA = ROOT / "analytics" / "outputs"
OUT_VIZ = ROOT / "analytics" / "visualizations"
OUT_DATA.mkdir(parents=True, exist_ok=True)
OUT_VIZ.mkdir(parents=True, exist_ok=True)

spark = (
    SparkSession.builder.master("local[2]")
    .appName("TP4-Retail-Intelligence")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

silver = spark.read.parquet(str(SILVER))
gold = spark.read.parquet(str(GOLD))

silver_rows = silver.count()
gold_rows = gold.count()
category_count = gold.select("field_07").distinct().count()

print("Version Spark :", spark.version)
print("Silver lignes :", silver_rows)
print("Silver colonnes :", len(silver.columns))
print("Gold lignes :", gold_rows)
print("Catégories Gold :", category_count)
silver.printSchema()

stats = silver.select(
    F.count("*").alias("silver_rows"),
    F.min("field_05").alias("field_05_min"),
    F.max("field_05").alias("field_05_max"),
    F.round(F.avg("field_05"), 2).alias("field_05_average"),
    F.expr("percentile_approx(field_05, 0.5)").alias("field_05_median"),
).toPandas()
stats.to_csv(OUT_DATA / "statistiques.csv", index=False)

by_category = gold.orderBy(F.desc("promotion_count")).toPandas()
by_category.to_csv(OUT_DATA / "kpi_par_categorie.csv", index=False)

costs = silver.select("field_05").where(F.col("field_05").isNotNull()).toPandas()
costs.to_csv(OUT_DATA / "distribution_field_05.csv", index=False)

print("Statistiques descriptives :")
print(stats.to_string(index=False))
print("KPI par catégorie :")
print(by_category.to_string(index=False))

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(by_category["field_07"].astype(str), by_category["promotion_count"])
plt.title("Nombre de promotions par catégorie technique")
plt.xlabel("Catégorie technique field_07")
plt.ylabel("Nombre de lignes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT_VIZ / "promotions_par_categorie.png", dpi=150, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10, 5))
plt.hist(costs["field_05"], bins=15)
plt.title("Distribution de field_05 dans le Silver")
plt.xlabel("Valeur de field_05")
plt.ylabel("Nombre de lignes")
plt.tight_layout()
plt.savefig(OUT_VIZ / "distribution_field_05.png", dpi=150, bbox_inches="tight")
plt.close()

print("Résultats écrits dans", OUT_DATA)
print("Graphiques écrits dans", OUT_VIZ)
print("TP4 UC08 terminé")
spark.stop()
