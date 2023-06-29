from server.core.models import Document
from storage_broker import get_document


def fetch_doc_by_id(doc_id: str):
    
    
    return get_document(Document.Doc_ID == doc_id)



    
    
    
    
    