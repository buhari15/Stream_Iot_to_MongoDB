# Streaming IoT data to MongoDB

The data source can be found on the following link.<br> 
[Raw data](https://www.kaggle.com/code/garystafford/iot-telemetry-demo-notebook)

There are  5 python scripts in this project.
1. Ping connection. <br>
![Ping connection](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/ping_connection.py)
This python script is use to ping to the MongoDB server to test connection.

2. Spark stream defintion. <br>
![Spark stream](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/spark_stream.py)
This python script, defined the spark session, schema, data source, and output sink.

3. Read raw csv to console using the spark stream. <br>
![Spark read csv](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/spark_read_csv.py)
This python script, output the raw csv data to the console without ingesting the data to MongoDB. It was use to test spark stream.

4. Write IoT data through spark structured stream to MongoDB. <br>
![Spark write to MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/write_to_mongodb.py)
This python script, use the spark structured stream to write IoT data to MongoDB as the sink.

5. Read inserted data from MongoDB. <br>
![Read data from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/code/read_db_data.py)
This python script, output the inserted data into MongoDB to the console.

# How to use it.
1. Clone the repository using **git clone https://github.com/buhari15/Stream_Iot_to_MongoDB.git**
2. Navigate to the folder and run **docker-compose up --build** to build and start the services.
    * Once built, spark stream session will start.
    * MongoDB service will also start.
    * All the services will start.
    * Spark Structured stream will stream the IoT data to MongoDB as the sink.
    
3. To read the inserted data from MongoDB run **docker-compose run readmongodb** from another terminal.
    * The output of IoT data from MongoDB after running **docker-compose run readmongodb**  
      ![First output from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/Screen_shoots/Reading_first_data.png)
      The Total data in the collection is 114 after running the first command.
    * The output of IoT data from MongoDB after running **docker-compose run readmongodb** for the second times.
      ![First output from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/Screen_shoots/Read_second.png)
       Now the Total data in the collection is 228.
    *  The DataFrame only output the first 100 elements from the collection. It can be modified in the script **read_db_data.py.**

## Author

**Buhari Abubakar**

+ [github/buhari15](https://github.com/buhari15)

## License

Copyright © 2023 Buhari Abubakar
Released under the MIT license.

***
