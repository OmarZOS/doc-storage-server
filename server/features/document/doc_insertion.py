# here, we make schema translations

from server.core.api_models import API_Document
from server.core.models import *
from server.features.insertion import insert_or_complete_or_raise


def insert_reference(doc: API_Document):
    DocReference(reference_id=doc.reference_id,reference_year=doc.reference_year,reference_ar=doc.reference_ar,reference_fr=doc.reference_fr)
    code,doc_ref,msg = insert_or_complete_or_raise(doc_ref)
    if (code == 1): return msg
    return doc_ref

def insert_doc_type(doc: API_Document):
    document_type = DocumentType(idDocument_type=doc.idDocument_type, document_type_label_fr=doc.document_type_label_fr, document_type_label_ar=doc.document_type_label_ar)
    code,document_type,msg = insert_or_complete_or_raise(document_type)
    if (code == 1): return msg
    return document_type

def insert_belonging_type_domain(doc: API_Document,document_type:DocumentType):
    domain_organisation = DomainOrganisation(idDomain_Organisation=doc.idDomain_Organisation, Domain_Organisation_label_fr=doc.Domain_Organisation_label_fr, Domain_Organisation_label_ar=doc.Domain_Organisation_label_ar, Domain_Organisation_acronym_fr=doc.Domain_Organisation_acronym_fr, Domain_Organisation_acronym_ar=doc.Domain_Organisation_acronym_ar)
    code,domain_organisation,msg = insert_or_complete_or_raise(domain_organisation)
    if (code == 1): return msg
    
    document_type_belongings = DocumentTypeBelonging(belonging_code=doc.belonging_code)
    document_type_belongings.belonging_type_id_ref = document_type.idDocument_type
    document_type_belongings.belonging_domain_id_ref = domain_organisation.idDomain_Organisation
    
    code,document_type_belongings,msg = insert_or_complete_or_raise(document_type_belongings)
    if (code == 1): return msg
    return document_type_belongings

def insert_container(doc: API_Document):
    container = Container(idContainer=doc.idContainer, type_container=doc.type_container)
        
    code,container,msg = insert_or_complete_or_raise(container)
    if (code == 1): return msg
    
    return container
    
def insert_position(doc: API_Document):
    
    containerposition = ContainerPosition()
    if(doc.idStore):
        store = Store(idStore=doc.idStore, Storetype=doc.Storetype, store_label_fr=doc.store_label_fr, store_label_ar=doc.store_label_ar, store_acronym_fr=doc.store_acronym_fr, store_acronym_ar=doc.store_acronym_ar)
        code,store,msg = insert_or_complete_or_raise(store)
        if (code == 1): return msg  
        if(doc.idBay):
            bay = Bay(idBay=doc.idBay,Store_ref=store.idStore)
            
            code,bay,msg = insert_or_complete_or_raise(bay)
            if (code == 1): return msg
           
            if(doc.idCob):
                cob = Cob(idCob=doc.idCob,bay_id_ref=bay.idBay)               
                code,cob,msg = insert_or_complete_or_raise(cob)
                if (code == 1): return msg
                if(doc.idShelf):                    
                    shelf = Shelf(idShelf=doc.idShelf,Cob_id_ref=cob.idCob)
                    code,shelf,msg = insert_or_complete_or_raise(shelf)
                    if (code == 1): return msg
                    containerposition.Container_position_shelf_ref_id = shelf.idShelf
                                        
                    code,containerposition,msg = insert_or_complete_or_raise(containerposition)
                    if (code == 1): return msg

    if(doc.idCabinet):
        cabinet = Cabinet(idCabinet=doc.idCabinet,Cabinet_store_ref_id=store.idStore)        
        code,cabinet,msg = insert_or_complete_or_raise(cabinet)
        if (code == 1): return msg
        containerposition.Container_position_cabinet_ref_id = cabinet.idCabinet
        
        code,containerposition,msg = insert_or_complete_or_raise(containerposition)
        if (code == 1): return msg

    return containerposition
    



def insert_doc(doc: API_Document):
    
    doc_ref = insert_reference(doc)
    if(type(doc_ref) != DocReference): return doc_ref
    
    document_type = insert_doc_type(doc)
    if(type(document_type) != DocumentType): return document_type
    
    document_type_belongings = insert_belonging_type_domain(doc)
    if(type(document_type_belongings) != DocumentTypeBelonging): return document_type_belongings
    
    container = insert_container(doc)
    if(type(container) != Container): return container

    containerposition = insert_position(doc)
    if(type(containerposition) != ContainerPosition): return containerposition
   
    document = Document(Doc_Label = doc.Doc_Label,reference_id = doc_ref.reference_id,container_ref_id = container.idContainer)
    code,document,msg = insert_or_complete_or_raise(document)
    if (code == 1): return msg

    # TODO: just one chunk for now, loop later
    chunk = DocumentChunk(Document_chunk_data = doc.Document_data,Document_Doc_ID=document.Doc_ID)    
    code,chunk,msg = insert_or_complete_or_raise(chunk)
    if (code == 1): return msg
        
    containedtype = ContainedType(container_type_ref_id = container.idContainer,types_contained_ref_id=document_type.idDocument_type,Container_position_ref_id=containerposition.idContainer_position)
    code,containedtype,msg = insert_or_complete_or_raise(containedtype)
    if (code == 1): return msg
    
    return "Insertion successfull."

