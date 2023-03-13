from fastapi import FastAPI
from constants import *
from core.locator import locator
from core.models import document_model
from features.doc_fetch import fetch_doc_by_id
from features.doc_insertion import insert_doc
from storage.wrappers.mysql import mysql_wrapper

# ----------- App initialisation -------------------------------------

DOCUMENT_DATABASE_NAME = "MYSQL_SERVICE"
locator().subscribe_service(DOCUMENT_DATABASE_NAME,mysql_wrapper)
# print("Starting my run..")
app = FastAPI()

# ------------- Routes -----------------------------------------------

@app.get("/")
def home():
    return {'data': 'Hello world'}

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

