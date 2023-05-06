
from pymongo import MongoClient
import datetime
import pandas as pd
import json
from spark_stream import spark_session, iot_schema, read_iot_data


def write_to_mongodb(source):
    """
    This function write the stream output to the MongoDB.
    Return: 
    """
    mongodb_sink = source.writeStream \
        .format("mongodb") \
        .option("checkpointLocation", "/tmp/pyspark7/")\
        .option("forceDeleteTempCheckpointLocation", "true")\
        .option('spark.mongodb.connection.uri', "mongodb://mongodb:27017/telemetry.sensor")\
        .option('spark.mongodb.database', 'telemetry')\
        .option('spark.mongodb.collection', 'sensor')\
        .trigger(processingTime="10 second")\
        .option("truncate", False)\
        .outputMode("append").start()
    mongodb_sink.awaitTermination()
    return mongodb_sink


if __name__ == "__main__":

    spark = spark_session()
    input_source = read_iot_data()
    print("Writing to MongoDB")
    output_sink = write_to_mongodb(input_source)
    
   
    
   








