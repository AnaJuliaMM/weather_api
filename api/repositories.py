from django.conf import settings 
import pymongo
from bson import ObjectId


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
    
    #CRUD

    def list(self):
        document = self.__get_collection().find({})
        return document
    
    def getById(self, document_id):
        document = self.__get_collection().find({"_id": ObjectId(document_id)})
        return document

        
		
    def getAll(self):
        document = self.getCollection().find({})
        
    def getByAttribute(self, attribute, value):
        pass
        
    def insert(self, document) -> None:
        self.getCollection().insert_one(document)
        
    def delete(self, document) -> None:
        pass
        
    def deleteAll(self) -> None:
        pass