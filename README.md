# Streaming IoT data to MongoDB

The data source can be found on the following link.
![Raw data](https://www.kaggle.com/code/garystafford/iot-telemetry-demo-notebook)

There are  5 python scripts in this project.
1. Ping connection
![Ping connection](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/ping_connection.py)
This python script is use to ping to the MongoDB server to test connection.

2. Spark stream defintion
![Spark stream](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/spark_stream.py)
This python script, defined the spark session, schema, data source, and output sink.

3. Read raw csv to console using the spark stream
![Spark read csv](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/spark_read_csv.py)
This python script, output the raw csv data to the console without ingesting the data to MongoDB. It was use to test spark stream.

4. Write IoT data through spark structured stream to MongoDB
![Spark write to MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/write_to_mongodb.py)
This python script, use the spark structured stream to write IoT data to MongoDB as the sink.

5. Read inserted data from MongoDB
![Read data from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/read_db_data.py)
This python script, output the inserted data into MongoDB to the console.

# How to use it.
1. Clone the repository
2. Run **docker-compose up** to start the services.
    * Once started spark stream session will start.
    * MongoDB service will also start
    * IoT data will writing to MongoDB using the spark structured stream.
    
3. To read the inserted data from MongoDB run docker-compose run readmongodb from another terminal
    * ![First output from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/Screen_shoots/Reading_first_data.png)
    * ![First output from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/Screen_shoots/Read_second.png)

## Author

**Buhari Abubakar**

+ [github/buhari15](https://github.com/buhari15)

## License

Copyright © 2023 Buhari Abubakar
Released under the MIT license.

***
