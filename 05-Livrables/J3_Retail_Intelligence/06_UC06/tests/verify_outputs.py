from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UC06-Verification").master("local[2]").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

silver = spark.read.parquet("/opt/project/output/data/silver/promotion")
gold = spark.read.parquet("/opt/project/output/data/gold/promotion_summary")

assert silver.count() == 300, "Le volume Silver attendu est 300"
assert gold.count() == 9, "Le volume Gold attendu est 9"
assert len(silver.schema.fields) == 19, "Le schema Silver doit contenir 19 champs"
assert silver.filter("field_00 IS NULL").count() == 0, "Identifiants Silver nuls"
assert silver.select("field_00").distinct().count() == silver.count(), "Identifiant candidat non unique"

print("Verification Parquet OK")
print(f"Silver: {silver.count()} lignes, {len(silver.schema.fields)} champs")
print(f"Gold: {gold.count()} lignes")
silver.printSchema()
spark.stop()
