from pymongo import MongoClient
import datetime
import pandas as pd



def mongodb_connect():
    """
    This function setup connection and create a mongodb database.
    Return: This function return the database and collection.
    """
    client = MongoClient('mongodb://mongodb:27017/')
    db = client['telemetry']
    db_collection = db['sensor']

    return db_collection


def check_data():
    """
    This function check and output all the data from MogoDB.
    Return: This function return a pandas DataFrame with the result on the console.
    """
    db_collection = mongodb_connect()
    find_data = db_collection.find()
    data_to_list = list(find_data)
    data_F = pd.DataFrame(data_to_list)  
    return data_F
  

if __name__ == "__main__":  
    print("\n") 
    print("Reading Data from MongoDB to Pandas DataFrame")
    print("==============================================================================================================================")
    
    dd = check_data()
    print("Total collection in the Database", dd.shape[0])
    print("\n")
    print("Read data to console.\n")
    print(dd.head(100))
    
    print("\n") 
    print("Finished reading file from MongoDB")