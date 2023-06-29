# here, we make schema translations


from server.core.api_models import API_Document
import storage_broker





def insert_doc_by_id(doc_id: str):
    pass

def insert_doc(doc: API_Document):
    
    
    res = storage_broker.insert_document(data)
    return res
    
    
    















