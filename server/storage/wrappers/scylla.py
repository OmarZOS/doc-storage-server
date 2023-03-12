
from cassandra.cluster import Cluster
from constants import *
from server.storage.storage_service.StorageService import StorageService



# 

class scylla_wrapper(StorageService):
    
        
    def __init__(self): # name...,node/edge
        self.cluster = Cluster(SCYLLA_NODES)

        self.session = self.cluster.connect(SCYLLA_KEYSPACE)


    def _insert(self,index,type,id,body):
        pass
    
    def _get(self,index_name,id):
        pass
    
    def insert_node(self,apiname,tag,node):
        pass
    
    def insert_edge(self,apiname,tag,edge):
        pass

    def search(self,api,query):
        pass
    
    def get(args):
        pass

    def test_connection(self):
        pass

    # just avoid this
    def queryData(self):
        pass
    
    # avoid this too..
    def saveData(self):
        pass    

