from server.core.models import  Cabinet, ContainedType, Container, ContainerPosition, DocReference, Document, DocumentChunk, DocumentType, DocumentTypeBelonging, Shelf
import server.storage.storage_broker as storage_broker

def fetch_doc_by_id(doc_id: str):
    return storage_broker.get(Document,{Document.Doc_ID:doc_id},[DocumentChunk,DocReference,Container,ContainedType])

def fetch_container_position(container_id: str):
    # searching in shelves
    res = storage_broker.get(ContainedType,{ContainedType.container_type_ref_id:container_id},[ContainerPosition,Shelf])
    if (res):
        return res
    # searching in cabinets
    return storage_broker.get(ContainedType,{ContainedType.container_type_ref_id:container_id},[ContainerPosition,Cabinet])

def fetch_type_origins(type_id):
    return storage_broker.get(DocumentTypeBelonging,{DocumentTypeBelonging.belonging_type_id_ref:type_id},[DocumentType])

def fetch_all_type_origins():
    return storage_broker.get(DocumentTypeBelonging)


    
    
    
    