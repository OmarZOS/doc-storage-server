from fastapi import FastAPI
from server.constants import *
from server.core.api_models import API_Document, API_Person
from server.features.document.doc_fetch import fetch_doc_by_id
from server.features.document.doc_insertion import insert_doc
from server.features.organisation.org_fetch import fetch_domains, fetch_orgs
from server.features.person.person_fetch import fetch_personnel, fetch_sessions
from server.features.person.person_insertion import insert_person, insert_trainee

# ----------- App initialisation -------------------------------------

DOCUMENT_DATABASE_NAME = "MYSQL_SERVICE"
app = FastAPI()

# ------------- Document related Routes -----------------------------------------------

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

# ------------- Personnel related Routes -----------------------------------------------

@app.post("/person/insertion")
def insertPerson(person: API_Person):
    res = insert_person(person)
    return res

@app.post("/trainee/insertion")
def insertTrainee(person: API_Person):
    res = insert_trainee(person)
    return res

@app.get("/session/all")
def get_sessions():
    res = fetch_sessions()
    return res

@app.get("/person/all")
def get_sessions():
    res = fetch_personnel()
    return res

# ------------- Administration related Routes -----------------------------------------------

@app.get("/organisation/all")
def get_orgs():
    res = fetch_orgs()
    return res

@app.get("/domain/all")
def get_domains():
    res = fetch_domains()
    return res

