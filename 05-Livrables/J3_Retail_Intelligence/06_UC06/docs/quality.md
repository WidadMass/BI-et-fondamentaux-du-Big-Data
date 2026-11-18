# Controle qualite

Le rapport JSON `quality/promotion_quality` contient les indicateurs suivants :

- `source_rows` ;
- `silver_rows` ;
- `gold_rows` ;
- `silver_null_ids` ;
- `silver_duplicate_rows`.
- `candidate_key_duplicates` ;
- `silver_parquet_rows` et `gold_parquet_rows` apres relecture ;
- `silver_schema_fields` apres relecture.

Le dernier traitement observe donne 300 lignes source, 300 lignes Silver, 9 lignes Gold, 0 identifiant nul et 0 doublon. Les sorties Parquet sont relues et leur volume est compare aux DataFrames avant ecriture. Le schema Silver relu doit etre strictement identique au schema ecrit.

Limite : les controles sont techniques et reposent sur un schema generique, car aucun en-tete metier n accompagne l extrait. Ils ne remplacent pas des regles fonctionnelles validees par le metier.
