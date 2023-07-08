# from core.models import Document
# from storage_broker import get_document
from server.core.models import ContainedType, Container, ContainerPosition, DocReference, Document, DocumentChunk, DocumentType
import server.storage.storage_broker as storage_broker

def fetch_doc_by_id(doc_id: str):
    return storage_broker.get(Document,{Document.Doc_ID:doc_id},[DocumentChunk,DocReference,Container])
    # return get_document(Document.Doc_ID == doc_id)



    
    
    
    
    