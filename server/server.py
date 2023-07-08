from fastapi import FastAPI
from server.constants import *
from server.core.api_models import API_Document
from server.features.doc_fetch import fetch_doc_by_id
from server.features.doc_insertion import insert_doc

# ----------- App initialisation -------------------------------------

DOCUMENT_DATABASE_NAME = "MYSQL_SERVICE"
app = FastAPI()

# ------------- Routes -----------------------------------------------

@app.get("/")
def home():
    return {'data': 'Hello world'}

@app.get("/documents/{document_id}")
def get_doc_by_id(document_id: str):
    doc = fetch_doc_by_id(document_id)
    return doc

@app.post("/documents/insertion")
def insert_document(document: API_Document):
    res = insert_doc(document)
    return res

@app.post("/document_search/")
def search_doc(search_args: str):
    doc = fetch_doc_by_id( search_args)
    return doc

