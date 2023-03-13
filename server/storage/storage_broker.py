
from constants import DOCUMENT_DATABASE_NAME
from core.locator import locator


class StorageBroker:
    
    # for concrete doc storage databases like scyllaDB
    @staticmethod
    def _get_document_provider():
        return locator().get_service(DOCUMENT_DATABASE_NAME)
        
    def insert_document(self,data):
        doc_store = self._get_document_provider()
        
        query = self._build_query(data)
        
        res = doc_store.saveData(query)
        return res
        
    def get_document(self,data):
        doc_store = self._get_document_provider()
        
        query = self._build_query(data)
        
        res = doc_store.queryData(query)
        return res

    # for meta search engines like elasticsearch
    def _get_document_seeker():
        pass
    
    def insert_metadata(args):
        pass

    def search_for(search_tokens):
        pass
    
    def _build_query(self,data):
        
        query = data
        # this can get more complicated in translating queries
        # depending on the client's standards
        # for the sake of simplicity, we return it as it is
         
        return query