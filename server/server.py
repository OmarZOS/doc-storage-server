from typing import Optional
from fastapi import FastAPI
from server.constants import *
from server.core.api_models import API_Document, API_Person
from server.features.document.doc_fetch import fetch_all_type_origins, fetch_container_position, fetch_doc_by_id, fetch_type_origins
from server.features.document.doc_insertion import insert_doc
from server.features.organisation.org_fetch import fetch_domains, fetch_organisation_by_id, fetch_orgs
from server.features.person.person_fetch import fetch_personnel, fetch_sessions
from server.features.person.person_insertion import insert_person, insert_trainee

# ----------- App initialisation -------------------------------------

DOCUMENT_DATABASE_NAME = "MYSQL_SERVICE"
app = FastAPI()

# ------------- Document related Routes -----------------------------------------------

@app.get("/")
def home():
    return {'data': 'Hello world'}

@app.get("/document/{document_id}")
def get_doc_by_id(document_id: str):
    doc = fetch_doc_by_id(document_id)
    return doc

@app.get("/container/{container_id}")
def get_container_by_id(container_id: str):
    position = fetch_container_position(container_id)
    return position

@app.post("/document/insertion")
def insert_document(document: API_Document):
    res = insert_doc(document)
    return res

# origins keep specific properties (age, confidentiality) for types in certain domains
@app.get("/origin/{belonging_id}")
def get_type_origins(belonging_id: Optional[str] = None):
    return fetch_type_origins(belonging_id)

@app.get("/origins/all")
def get_all_type_origins():
    return fetch_all_type_origins()


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

@app.get("/organisations/all")
def get_orgs():
    res = fetch_orgs()
    return res

@app.get("/organisation/{org_id}")
def get_org_by_id(org_id:str):
    res = fetch_organisation_by_id(org_id)
    return res

@app.get("/domains/all")
def get_domains():
    res = fetch_domains()
    return res

