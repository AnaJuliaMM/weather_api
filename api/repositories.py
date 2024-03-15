from django.conf import settings 
import pymongo

# ORM
class WeatherRepository:

    def __init__(self, name) -> None:
        self.collection = name
    
    def __get_connection(self):
        MONGO_CONNECTION_STRING = getattr(settings, "MONGO_CONNECTION_STRING")
        MONGO_DATABASE_NAME = getattr(settings, "MONGO_DATABASE_NAME")

        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        connection = client[MONGO_DATABASE_NAME]
        
        return connection
    
    def __get_collection(self):
        conn = self.__get_connection()
        collection = conn[self.collection]
        return collection
    
    def list(self):
        document = self.__get_collection().find({})
        return document
    
    def create(self, document):
        self.__get_collection().insert_one(document)