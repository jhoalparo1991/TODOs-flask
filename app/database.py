
from pymongo import MongoClient

def get_connection():
    try:
        mongo_client = MongoClient('mongodb://localhost:27017/todo-app')

        if mongo_client :
            print('Connection successfully')
        else:
    
            print('Error in connection')
        return mongo_client
    except ValueError as error:
        print(f'Error in connection -> {error}')