# here, we make schema translations

from server.core.api_models import API_Document
from server.core.models import *
from server.features.insertion import insert_or_complete_or_raise


def insert_reference(doc: API_Document):
    doc_ref = DocReference(reference_id=doc.ReferenceID,reference_year=doc.ReferenceYear,reference_ar=doc.ReferenceAR,reference_fr=doc.ReferenceFR)
    code,doc_ref,msg = insert_or_complete_or_raise(doc_ref)
    if (code == 1): return msg
    return doc_ref

def insert_doc_type(doc: API_Document):
    document_type = DocumentType(idDocument_type=doc.DocTypeID, document_type_label_fr=doc.DocTypeLabelFR, document_type_label_ar=doc.DocTypeLabelAR)
    code,document_type,msg = insert_or_complete_or_raise(document_type)
    if (code == 1): return msg
    return document_type

def insert_belonging_type_domain(doc: API_Document,document_type:DocumentType):
    domain_organisation = DomainOrganisation(idDomain_Organisation=doc.DomainID, Domain_Organisation_label_fr=doc.DomainLabelFR, Domain_Organisation_label_ar=doc.DomainLabelAR, Domain_Organisation_acronym_fr=doc.DomainAcronymFR, Domain_Organisation_acronym_ar=doc.DomainAcronymAR)
    code,domain_organisation,msg = insert_or_complete_or_raise(domain_organisation)
    if (code == 1): return msg
    
    document_type_belongings = DocumentTypeBelonging(belonging_code=doc.BelongingCode)
    document_type_belongings.belonging_type_id_ref = document_type.idDocument_type
    document_type_belongings.belonging_domain_id_ref = domain_organisation.idDomain_Organisation
    
    code,document_type_belongings,msg = insert_or_complete_or_raise(document_type_belongings)
    if (code == 1): return msg
    return document_type_belongings

def insert_container(doc: API_Document):
    container = Container(idContainer=doc.ContainerID, type_container=doc.ContainerType)
        
    code,container,msg = insert_or_complete_or_raise(container)
    if (code == 1): return msg
    
    return container
    
def insert_position(doc: API_Document):
    
    containerposition = ContainerPosition()
    if(doc.StoreID):
        store = Store(idStore=doc.StoreID, Storetype=doc.StoreType, store_label_fr=doc.StoreLabelFR, store_label_ar=doc.StoreLabelAR, store_acronym_fr=doc.StoreAcronymFR, store_acronym_ar=doc.StoreAcronymAR)
        code,store,msg = insert_or_complete_or_raise(store)
        if (code == 1): return msg  
        if(doc.BayID):
            bay = Bay(idBay=doc.BayID,Store_ref_id=store.idStore)
            
            code,bay,msg = insert_or_complete_or_raise(bay)
            if (code == 1): return msg
           
            if(doc.CobID):
                cob = Cob(idCob=doc.CobID,bay_ref_id=bay.idBay,Cob_ref_fr=doc.CobRefFR,Cob_ref_ar=doc.CobRefAR)               
                code,cob,msg = insert_or_complete_or_raise(cob)
                if (code == 1): return msg
                if(doc.ShelfID):                    
                    shelf = Shelf(idShelf=doc.ShelfID,cob_ref_id=cob.idCob,Shelf_ref_fr=doc.ShelfRefFR,Shelf_ref_ar=doc.ShelfRefAR)
                    code,shelf,msg = insert_or_complete_or_raise(shelf)
                    if (code == 1): return msg
                    containerposition.Container_position_shelf_ref_id = shelf.idShelf
                                        
                    code,containerposition,msg = insert_or_complete_or_raise(containerposition)
                    if (code == 1): return msg

    if(doc.CabinetID):
        cabinet = Cabinet(idCabinet=doc.CabinetID,Cabinet_store_ref_id=store.idStore,Cabinet_ref_ar=doc.CabinetRefAR,Cabinet_ref_fr=doc.CabinetRefFR)        
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
    
    document_type_belongings = insert_belonging_type_domain(doc,document_type)
    if(type(document_type_belongings) != DocumentTypeBelonging): return document_type_belongings
    
    container = insert_container(doc)
    if(type(container) != Container): return container

    containerposition = insert_position(doc)
    if(type(containerposition) != ContainerPosition): return containerposition
   
    document = Document(Doc_Label = doc.DocumentLabel,reference_id = doc_ref.reference_id,container_ref_id = container.idContainer)
    code,document,msg = insert_or_complete_or_raise(document)
    if (code == 1): return msg

    # TODO: just one chunk for now, loop later
    chunk = DocumentChunk(Document_chunk_data = doc.DocumentData,Document_Doc_ID=document.Doc_ID)    
    code,chunk,msg = insert_or_complete_or_raise(chunk)
    if (code == 1): return msg
        
    containedtype = ContainedType(container_type_ref_id = container.idContainer,types_contained_ref_id=document_type.idDocument_type,Container_position_ref_id=containerposition.idContainer_position)
    code,containedtype,msg = insert_or_complete_or_raise(containedtype)
    if (code == 1): return msg
    
    return "Insertion successfull."

