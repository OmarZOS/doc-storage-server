# This component is responsible for choosing the right place
# to insert data in the most appropriate
# store, it can hold multiple
# storage engines, the insertion logic is in here

from constants import DB_URI, DOCUMENT_TABLE_NAME,SQL_SCHEMA
import wrappers.sql_wrapper as doc_store
from core.models import Document, DocumentChunk

def insert_document(chunk:DocumentChunk):
    engine = doc_store.get_engine(DB_URI)
    res = doc_store.add_record(engine,chunk)
    return res

def get_document(conditions):
    engine = doc_store.get_engine(DB_URI)
    res = doc_store.get_records(engine,Document,conditions)
    return res

def get(table_name,fields,conditions):
    engine = doc_store.get_engine(DB_URI)
    res = doc_store.get_records(engine,SQL_SCHEMA,DOCUMENT_TABLE_NAME,conditions)
    return res

# for meta search engines like elasticsearch
def insert_metadata(args):
    pass

def search_for(search_tokens):
    pass
