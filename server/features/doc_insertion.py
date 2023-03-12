

from server.storage.storage_broker import StorageBroker
import server.core.messages as messages

broker = StorageBroker()


def insert_doc_by_id(doc_id: str):
    pass

def insert_doc(doc):
    attribs = [attr for attr in dir(doc) if not attr.startswith('__') and not callable(getattr(doc, attr))]
    vals = []
    for attr in attribs:
        vals.add(doc[attr]) 
    
    res = broker.insert_document(attribs, vals)
    
    # TODO: update query response message here..
    
    return res
    
    
    













