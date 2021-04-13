from pymongo import MongoClient

class MongoSetup():

    def connect(self):
        client = MongoClient('mongodb://root:example@localhost:27017/')
        return client
    def show_databases(self):
        client = self.connect()
        #client.start_session()
        dbnames= client.list_database_names()
        client.close()
        return dbnames