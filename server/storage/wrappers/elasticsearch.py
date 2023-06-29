
from constants import *
from storage.storage_service.StorageService import *

from elasticsearch import Elasticsearch



class elastic_wrapper(StorageService):
    
    def __init__(self): # name...,node/edge

        self.es = Elasticsearch(f"{ELASTIC_SCHEME}://{ELASTIC_HOST}:{ELASTIC_PORT}")

    def _insert(self,index,type,id,body):
        self.es.index(index=index,
            type=type,
            id=id,
            body=body)
    
    def _get(self,index_name,id):
        self.es.get(index=index_name,id=id)
    

    def search(self,api,query):
        return self.es.search(query=query)["hits"]["hits"]
    
    def get(args):
        pass

    def test_connection(self):
        return self.es.ping()

    # just avoid this
    def queryData(self):
        pass
    
    # avoid this too..
    def saveData(self):
        pass    
