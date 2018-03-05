import pymongo

__author__ = 'Tadeu Faustino'

class Database(object):
    URI = "mongodb://127.0.0.1:27107"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['restaurante']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)


    # para mais de uma instância
    # def __init__(self):
      #   self.uri = ""
      #   self.database = None
