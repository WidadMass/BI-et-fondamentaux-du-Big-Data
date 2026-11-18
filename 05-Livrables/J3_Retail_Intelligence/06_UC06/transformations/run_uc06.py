from pyspark.sql import SparkSession, functions as F, types as T

spark = SparkSession.builder.appName("UC06-Promotion-Silver-Gold").master("local[2]").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

source = "/opt/project/input/promotion/promotion.dat"
silver_path = "/opt/project/output/data/silver/promotion"
gold_path = "/opt/project/output/data/gold/promotion_summary"
quality_path = "/opt/project/output/quality/promotion_quality"
columns = [f"field_{i:02d}" for i in range(19)]
schema = T.StructType([T.StructField(c, T.StringType(), True) for c in columns])

raw = spark.read.option("sep", "|").option("header", "false").schema(schema).csv(source)
silver = (raw.filter(F.col("field_00").isNotNull()).dropDuplicates()
    .withColumn("field_00", F.col("field_00").cast("int"))
    .withColumn("field_02", F.col("field_02").cast("int"))
    .withColumn("field_03", F.col("field_03").cast("int"))
    .withColumn("field_04", F.col("field_04").cast("int"))
    .withColumn("field_05", F.col("field_05").cast("decimal(12,2)")))
gold = silver.groupBy("field_07").agg(F.count("*").alias("promotion_count"), F.round(F.avg("field_05"), 2).alias("average_cost"))
silver.write.mode("overwrite").parquet(silver_path)
gold.write.mode("overwrite").parquet(gold_path)

# Relecture obligatoire des sorties Parquet.
silver_reloaded = spark.read.parquet(silver_path)
gold_reloaded = spark.read.parquet(gold_path)
source_rows = raw.count()
silver_rows = silver.count()
gold_rows = gold.count()
silver_parquet_rows = silver_reloaded.count()
gold_parquet_rows = gold_reloaded.count()
candidate_key_duplicates = silver_rows - silver.select("field_00").distinct().count()

assert silver_parquet_rows == silver_rows, "Volume Silver incoherent apres relecture Parquet"
assert gold_parquet_rows == gold_rows, "Volume Gold incoherent apres relecture Parquet"
assert silver_reloaded.schema == silver.schema, "Schema Silver modifie apres relecture Parquet"

quality = spark.createDataFrame([
    ("source_rows", source_rows),
    ("silver_rows", silver_rows),
    ("gold_rows", gold_rows),
    ("silver_null_ids", silver.filter(F.col("field_00").isNull()).count()),
    ("silver_duplicate_rows", silver_rows - silver.dropDuplicates().count()),
    ("candidate_key_duplicates", candidate_key_duplicates),
    ("silver_parquet_rows", silver_parquet_rows),
    ("gold_parquet_rows", gold_parquet_rows),
    ("silver_schema_fields", len(silver_reloaded.schema.fields)),
], ["metric", "value"])
quality.write.mode("overwrite").json(quality_path)
print(f"Silver: {silver_rows} lignes")
print(f"Gold: {gold_rows} lignes")
print(f"Relecture Parquet Silver: {silver_parquet_rows} lignes, {len(silver_reloaded.schema.fields)} champs")
print(f"Relecture Parquet Gold: {gold_parquet_rows} lignes")
silver_reloaded.printSchema()
quality.show(truncate=False)
spark.stop()
