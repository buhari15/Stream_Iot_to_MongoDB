from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, BooleanType, DoubleType

from spark_stream import spark_session, read_iot_data, iot_schema,  write_stream

# To read the csv file directly without ingesting the data in MongoDB.
# The script output the result on the console.

if __name__ == "__main__": 
    spark = spark_session() 
    print("\n") 
    print("Session start")
    print("==============================================================================================================================")
    print(spark)

    read_file = read_iot_data()
    print("Data loaded")
    write_to_console = write_stream(read_file)
    print(read_file)
    print(write_to_console)