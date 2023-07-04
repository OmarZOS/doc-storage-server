# here, we make schema translations


from server.core.api_models import API_Document
from server.core.models import *
import storage_broker





def insert_doc_by_id(doc_id: str):
    pass

def insert_doc(doc: API_Document):
    
    # Build the hierarchy
    # TODO: just one chunk for now, loop later
    chunk = DocumentChunk(Document_chunk_data = doc.Document_data)
    doc_ref = DocReference(reference_id=doc.reference_id,reference_year=doc.reference_year,reference_ar=doc.reference_ar,reference_fr=doc.reference_fr)
    document = Document(Doc_Label = doc.Doc_Label)
    document_type = DocumentType(idDocument_type=doc.idDocument_type, document_type_label_fr=doc.document_type_label_fr, document_type_label_ar=doc.document_type_label_ar)
    
    if (doc.belonging_code or doc.idDomain_Organisation or doc.Domain_Organisation_acronym_fr):
        document_type_belongings.document_type = document_type
        domain_organisation = DomainOrganisation(idDomain_Organisation=doc.idDomain_Organisation, Domain_Organisation_label_fr=doc.Domain_Organisation_label_fr, Domain_Organisation_label_ar=doc.Domain_Organisation_label_ar, Domain_Organisation_acronym_fr=doc.Domain_Organisation_acronym_fr, Domain_Organisation_acronym_ar=doc.Domain_Organisation_acronym_ar)
        document_type_belongings = DocumentTypeBelonging(belonging_code=doc.belonging_code)
        document_type_belongings.domain_organisation = domain_organisation
    
    if (doc.idContainer or doc.type_container):
        container = Container(idContainer=doc.idContainer, type_container=doc.type_container)
        containedtype = ContainedType()
        containerposition = ContainerPosition()
        containedtype.Document_type = document_type
        containedtype.Container = container
        document.Container = container
    
    
    if(doc.idStore):
        store = Store(idStore=doc.idStore, Storetype=doc.Storetype, store_label_fr=doc.store_label_fr, store_label_ar=doc.store_label_ar, store_acronym_fr=doc.store_acronym_fr, store_acronym_ar=doc.store_acronym_ar)
        if(doc.idBay):
            bay = Bay(idBay=doc.idBay)
            bay.Store = store
            if(doc.idCob):
                cob = Cob(idCob=doc.idCob)
                cob.Bay = bay
                if(doc.idShelf):
                    shelf = Shelf(idShelf=doc.idShelf)
                    shelf.Cob = cob
                    containerposition.Shelf = shelf
                    containedtype.Container_position = containerposition
    if(doc.idCabinet):
        cabinet = Cabinet(idCabinet=doc.idCabinet)
        containerposition.Cabinet = cabinet
        containedtype.Container_position = containerposition
    
    document.doc_reference = doc_ref
    chunk.Document = document
    
    res = storage_broker.insert_document(chunk)
    return res
    
    
    















