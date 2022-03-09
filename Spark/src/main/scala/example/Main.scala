package example

import org.apache.spark.SparkConf
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.types.IntegerType
import org.apache.spark.sql.{SaveMode, SparkSession, functions}

object Main {
  def main(args: Array[String]) : Unit = {
    // config app name
    val spark_conf = new SparkConf().setAppName("Spark-Job").setMaster("local[4]")
    val spark_session = SparkSession.builder().config(spark_conf).getOrCreate()
    // path read and write hdfs
    val path_hdfs_read =  "hdfs://172.16.0.20:9000/user/root/data/result_data/*"
    val path_hdfs_wirte = "hdfs://172.16.0.20:9000/user/root/data_parquet/"
    // read file csv
    val df = spark_session.read.option("delimiter",",").option("header", "true").csv(path_hdfs_read)
    // filter row === female
    val df2 = df.filter(df("Gender") === "Female")
    // add column name
    val df3 = df2.withColumn("LastName",functions.split(col("Name")," ").getItem(2).cast(IntegerType))
    // mod 3
    val df4 =  df3.withColumn("Mod3",col("LastName" ) % 3)
    // Group by, Count
    val df5 = df4.groupBy("Mod3").count()
    df5.show()
    // wirte dataFrame to parquet
    df5.write.mode(SaveMode.Overwrite).parquet(path_hdfs_wirte)
    // read file Parquet
    val df6 = spark_session.read.parquet(path_hdfs_wirte);
    df6.show()
  }
}
