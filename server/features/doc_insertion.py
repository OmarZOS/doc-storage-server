# here, we make schema translations

from server.core.api_models import API_Document
from server.core.models import *
import server.storage.storage_broker as storage_broker

def insert_doc(doc: API_Document):
    
    # TODO: just one chunk for now, loop later
    doc_ref = DocReference(reference_id=doc.reference_id,reference_year=doc.reference_year,reference_ar=doc.reference_ar,reference_fr=doc.reference_fr)
    
    code,doc_ref,msg = insert_or_complete_or_raise(doc_ref)
    if (code == 1): return msg

    print(doc_ref.reference_id)
    document = Document(Doc_Label = doc.Doc_Label)
    
    document_type = DocumentType(idDocument_type=doc.idDocument_type, document_type_label_fr=doc.document_type_label_fr, document_type_label_ar=doc.document_type_label_ar)
    
    code,document_type,msg = insert_or_complete_or_raise(document_type)
    if (code == 1): return msg

    
    
    if (doc.belonging_code or doc.idDomain_Organisation or doc.Domain_Organisation_acronym_fr):
        domain_organisation = DomainOrganisation(idDomain_Organisation=doc.idDomain_Organisation, Domain_Organisation_label_fr=doc.Domain_Organisation_label_fr, Domain_Organisation_label_ar=doc.Domain_Organisation_label_ar, Domain_Organisation_acronym_fr=doc.Domain_Organisation_acronym_fr, Domain_Organisation_acronym_ar=doc.Domain_Organisation_acronym_ar)
        
        code,domain_organisation,msg = insert_or_complete_or_raise(domain_organisation)
        if (code == 1): return msg

        
        document_type_belongings = DocumentTypeBelonging(belonging_code=doc.belonging_code)
        document_type_belongings.belonging_type_id_ref = document_type.idDocument_type
        document_type_belongings.belonging_domain_id_ref = domain_organisation.idDomain_Organisation
        
    
    if (doc.idContainer or doc.type_container):
        container = Container(idContainer=doc.idContainer, type_container=doc.type_container)
        
        code,container,msg = insert_or_complete_or_raise(container)
        if (code == 1): return msg

        
        containedtype = ContainedType()
        containerposition = ContainerPosition()
        containedtype.types_contained_ref_id = document_type.idDocument_type
        
        
        code,document_type_belongings,msg = insert_or_complete_or_raise(document_type_belongings)
        if (code == 1): return msg

        
        containedtype.container_type_ref_id = container.idContainer
        
        
        code,containedtype,msg = insert_or_complete_or_raise(containedtype)
        if (code == 1): return msg

        
        document.container_ref_id = container.idContainer
        
    
    
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

                    
                    containedtype.Container_position_ref_id = containerposition.idContainer_position
                    
                    
                    code,containedtype,msg = insert_or_complete_or_raise(containedtype)
                    if (code == 1): return msg

    if(doc.idCabinet):
        cabinet = Cabinet(idCabinet=doc.idCabinet,Cabinet_store_ref_id=store.idStore)
        
        
        code,cabinet,msg = insert_or_complete_or_raise(cabinet)
        if (code == 1): return msg

        
        containerposition.Container_position_cabinet_ref_id = cabinet.idCabinet
        
        code,containerposition,msg = insert_or_complete_or_raise(containerposition)
        if (code == 1): return msg

        containedtype.Container_position_ref_id = containerposition.idContainer_position
        
        
        code,containedtype,msg = insert_or_complete_or_raise(containedtype)
        if (code == 1): return msg

        
    document.reference_id = doc_ref.reference_id
    
    
    code,document,msg = insert_or_complete_or_raise(document)
    if (code == 1): return msg

    chunk = DocumentChunk(Document_chunk_data = doc.Document_data,Document_Doc_ID=document.Doc_ID)
    
    code,chunk,msg = insert_or_complete_or_raise(chunk)
    if (code == 1): return msg
    
    return "Insertion successfull."

def insert_or_complete_or_raise(obj):
    try:
        obj = storage_broker.insert_record(obj)
    except Exception as e:
        return (1,None,f"An exception occurred with {type(obj)}"+str(e))
    # Object found, fetched and returned
    return (0,obj,"")
