from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, BooleanType, DoubleType


def spark_session():
    """
    In this function the spark session is defined.
    Return: The function returned spark session.
    """

    spark = SparkSession.builder.appName('Read IOT Data') \
        .config("spark.mongodb.input.uri", "mongodb://mongodb:27017/telemetry.sensor") \
        .config("spark.mongodb.output.uri", "mongodb://mongodb:27017/telemetry.sensor") \
        .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:10.1.1') \
        .getOrCreate()
    

    return spark


def iot_schema():
    """
    This function define the telemetry data schema.
    Return: The schema

    """
    schema_ = (StructType() 
            .add("ts", DoubleType()) 
            .add("device", StringType()) 
            .add("co", DoubleType()) 
            .add("humidity", DoubleType()) 
            .add("light", BooleanType()) 
            .add("lpg", DoubleType()) 
            .add("motion", BooleanType()) 
            .add("smoke", DoubleType()) 
            .add("temp", DoubleType())  
    )

    return schema_ 


def read_iot_data():
    """
    This function load the csv file into spark read stream.
    Return: It return csv files as the source of stream for sparks
    """ 
    read_csv = spark_session().readStream \
        .option("header", True) \
        .schema(iot_schema()) \
        .option("maxFilesPerTrigger", 1)\
        .csv('data/file')
    return read_csv
    


def write_stream(source):
    """
    This function write the stream output to the console.
    Return: 
    """
    out_sink = source.writeStream \
        .format("console")\
        .trigger(processingTime="10 second")\
        .option("truncate", False)\
        .outputMode("update").start()
    out_sink.awaitTermination()
    return out_sink




