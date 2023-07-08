# This component is responsible for choosing the right place
# to insert data in the most appropriate
# store, it can hold multiple
# storage engines, the insertion logic is in here

from server.constants import DB_URI, DOCUMENT_TABLE_NAME,SQL_SCHEMA
import server.storage.wrappers.sql_wrapper as doc_store
from server.core.models import Document, DocumentChunk

def insert_document(objects):
    try:
        engine = doc_store.get_engine(DB_URI)
    except:
        print('An exception occurred while connecting to the database.')
        raise 'An exception occurred while connecting to the database.'
    for item in objects:
        
        res = doc_store.add_record(engine,item)
    return res

def insert_record(obj):
    try:
        engine = doc_store.get_engine(DB_URI)
    except:
        print('An exception occurred while connecting to the database.')
        raise 'An exception occurred while connecting to the database.'
    res = doc_store.add_record(engine,obj)
    return res

def get_document(conditions):
    try:
        engine = doc_store.get_engine(DB_URI)
    except:
        print('An exception occurred while connecting to the database.')
        raise 'An exception occurred while connecting to the database.'
    res = doc_store.get_records(engine,Document,conditions)
    return res

def get(table,conditions=None, join_tables=None):
    try:
        engine = doc_store.get_engine(DB_URI)
    except:
        print('An exception occurred while connecting to the database.')
        raise 'An exception occurred while connecting to the database.'
    res = doc_store.get_records(engine,table,conditions,join_tables)
    return res

# for meta search engines like elasticsearch
def insert_metadata(args):
    pass

def search_for(search_tokens):
    pass
