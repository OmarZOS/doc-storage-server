from fastapi import FastAPI
from constants import *
from server.core.models import document_model
from server.features.doc_fetch import fetch_doc_by_id
from server.features.doc_insertion import insert_doc

# ----------- App initialisation -------------------------------------

app = FastAPI()

# ------------- Routes -----------------------------------------------

@app.get("/documents/{document_id}")
def get_doc_by_id(document_id: str):
    doc = fetch_doc_by_id( doc_id=document_id)
    return doc

@app.post("/documents/insertion")
def insert_document(document: document_model):
    res = insert_doc(document)
    return res



@app.post("/document_search/")
def search_doc(search_args: str):
    doc = fetch_doc_by_id( search_args)
    return doc

