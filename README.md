# Streaming IoT data to MongoDB

The data source of this project can be found on the following link.
![Raw data](https://github.com/buhari15/tweets-nigeria-analysis/blob/main/tweets_ng.jsonl)

There are  5 python scripts in this project.
1. Ping connection
![Ping connection](https://github.com/buhari15/tweets-nigeria-analysis/blob/main/tweets_ng.jsonl)
This python script is use to ping to the MongoDB server to test connection.

2. Spark stream defintion
![Spark stream](https://github.com/buhari15/tweets-nigeria-analysis/blob/main/tweets_ng.jsonl)
This python script, defined the spark session, schema, data source, and output sink.

3. Read raw csv to console using the spark stream
![Spark read csv](https://github.com/buhari15/tweets-nigeria-analysis/blob/main/tweets_ng.jsonl)
This python script, output the raw csv data to the console without ingesting the data to MongoDB. It was use to test spark stream.

4. Write IoT data through spark structured stream to MongoDB
![Spark write to MongoDB](https://github.com/buhari15/tweets-nigeria-analysis/blob/main/tweets_ng.jsonl)
This python script, use the spark structured stream to write IoT data to MongoDB as the sink.

5. Read inserted data from MongoDB
![Read data from MongoDB](https://github.com/buhari15/tweets-nigeria-analysis/blob/main/tweets_ng.jsonl)
This python script, output the inserted data into MongoDB to the console.

# How to use it.

## Author

**Buhari Abubakar**

+ [github/buhari15](https://github.com/buhari15)

## License

Copyright © 2023 Buhari Abubakar
Released under the MIT license.

***