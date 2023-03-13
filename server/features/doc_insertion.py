

from storage.storage_broker import StorageBroker
import core.messages as messages

broker = StorageBroker()


def insert_doc_by_id(doc_id: str):
    pass

def insert_doc(doc):
    attribs = [attr for attr in dir(doc) if not attr.startswith('__') and not callable(getattr(doc, attr))]
    data = {}
    for attr in attribs:
        data[attr] = doc[attr] 
    
    res = broker.insert_document(data)
    
    # TODO: update query response message here..
    
    return res
    
    
    













