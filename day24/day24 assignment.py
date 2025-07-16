# Databricks notebook source
dbutils.widgets.text("date","")
input_date=dbutils.widgets.get("date")


# COMMAND ----------

df=spark.read.csv(f"/Volumes/workspace/scd/day23/customers/customers_{input_date}.csv", header=True, inferSchema=True)
df.write.format("delta").mode("append").saveAsTable("scd.customer_table_filtered25")

# COMMAND ----------

df2=spark.read.csv(f"/Volumes/workspace/scd/day23/customers/customers_{input_date}.csv", header=True, inferSchema=True)
df2.write.format("delta").mode("append").saveAsTable("scd.customer_table_filtered26")

# COMMAND ----------

historical_df=spark.table("scd.customer_table_filtered25")
display(historical_df)

# COMMAND ----------

current_df=spark.table("scd.customer_table_filtered26")
display(current_df)

# COMMAND ----------

from delta.tables import DeltaTable
from pyspark.sql.functions import lit, current_date

delta_table = DeltaTable.forName(spark, "scd.customer_table_filtered25")

df = delta_table.toDF()

historical_new = historical_df.withColumn("startDate", lit("2000-01-01")) \
                              .withColumn("endDate", lit("2099-12-31")) \
                              .withColumn("currentFlag", lit("Y"))

current_new = current_df.withColumn("startDate", current_date()) \
                        .withColumn("endDate", lit("2200-01-01")) \
                        .withColumn("currentFlag", lit("Y"))







# COMMAND ----------

repeated_ids = historical_df.select("customer_id").intersect(current_df.select("customer_id"))


# COMMAND ----------

from pyspark.sql.functions import col


updated_historical = historical_new.join(repeated_ids, on="customer_id", how="left_semi") \
    .withColumn("endDate", current_date()) \
    .withColumn("currentFlag", lit("N"))

unchanged_historical = historical_new.join(repeated_ids, on="customer_id", how="left_anti")

# COMMAND ----------

final_df = unchanged_historical.unionByName(updated_historical).unionByName(current_new)
display(final_df)