# This component is responsible for choosing the right place
# to insert data in the most appropriate
# store, it can hold multiple
# storage engines, the insertion logic is in here

from constants import DB_URI, DOCUMENT_TABLE_NAME,SQL_SCHEMA
import wrappers.mysql as doc_store
from core.models import Document

def insert_document(document:Document):
    engine = doc_store.get_engine(DB_URI)
    res = doc_store.create_record(engine,SQL_SCHEMA,DOCUMENT_TABLE_NAME,document)
    return res

def get_document(conditions):
    engine = doc_store.get_engine(DB_URI)
    res = doc_store.read_records(engine,SQL_SCHEMA,DOCUMENT_TABLE_NAME,conditions)
    return res

def get(table_names,fields,conditions):
    engine = doc_store.get_engine(DB_URI)
    res = doc_store.read_records(engine,SQL_SCHEMA,DOCUMENT_TABLE_NAME,conditions)
    return res

# for meta search engines like elasticsearch
def insert_metadata(args):
    pass

def search_for(search_tokens):
    pass
