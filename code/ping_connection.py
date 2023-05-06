from pymongo import MongoClient


def ping_connection():
    """
    This function test the connection to MongoDB server
    Return: None
    """
    client = MongoClient("mongodb://mongodb:27017")
    try:
        client.admin.command('ping')
        print("You successfully connected to MongoDB!")
    
    except Exception as e:
        print(f'There is error to connecting MongoDB Server: {e}')