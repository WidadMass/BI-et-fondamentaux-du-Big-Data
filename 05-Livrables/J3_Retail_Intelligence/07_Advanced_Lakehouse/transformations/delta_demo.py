from pathlib import Path
import shutil

from delta.tables import DeltaTable
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


SILVER_PATH = "/opt/project/input/silver/promotion"
DELTA_PATH = "/opt/project/output/data/delta/promotion"


def build_spark() -> SparkSession:
    return (
        SparkSession.builder.appName("TP3-Advanced-Delta-Lake")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .getOrCreate()
    )


def main() -> None:
    spark = build_spark()
    spark.sparkContext.setLogLevel("WARN")

    delta_directory = Path(DELTA_PATH)
    if delta_directory.exists():
        shutil.rmtree(delta_directory)

    source = spark.read.parquet(SILVER_PATH)
    source_count = source.count()

    baseline = source.withColumn("batch_id", lit("initial"))
    (
        baseline.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(DELTA_PATH)
    )

    version_0_count = (
        spark.read.format("delta").option("versionAsOf", 0).load(DELTA_PATH).count()
    )

    incremental = (
        source.limit(1)
        .withColumn("field_01", lit("DELTA-DEMO-001"))
        .withColumn("batch_id", lit("incremental-001"))
        .withColumn("source_system", lit("schema-evolution-demo"))
    )
    (
        incremental.write.format("delta")
        .mode("append")
        .option("mergeSchema", "true")
        .save(DELTA_PATH)
    )

    current = spark.read.format("delta").load(DELTA_PATH)
    current_count = current.count()
    current_columns = current.columns

    delta_table = DeltaTable.forPath(spark, DELTA_PATH)
    history = delta_table.history()

    print("\n=== DEMONSTRATION DELTA LAKE ===")
    print(f"Source Silver : {source_count} lignes")
    print(f"Version 0     : {version_0_count} lignes")
    print(f"Version courante : {current_count} lignes")
    print(f"Nouvelle colonne presente : {'source_system' in current_columns}")
    print(f"Colonnes courantes : {', '.join(current_columns)}")
    print("\nHistorique Delta :")
    history.select("version", "timestamp", "operation", "operationParameters").show(
        truncate=False
    )
    print("Ligne incrementale :")
    current.filter("field_01 = 'DELTA-DEMO-001'").select(
        "field_01", "batch_id", "source_system"
    ).show(truncate=False)

    log_path = Path("/opt/project/output/data/delta/promotion/_delta_log")
    print(f"Journal de transactions present : {log_path.exists()}")

    assert source_count == 300
    assert version_0_count == 300
    assert current_count == 301
    assert "source_system" in current_columns
    assert log_path.exists()

    print("RESULTAT : demonstration Delta validee")
    spark.stop()


if __name__ == "__main__":
    main()

