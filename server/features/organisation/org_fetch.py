
# from core.models import Document
# from storage_broker import get_document
from server.core.models import DomainOrganisation, Organisation
import server.storage.storage_broker as storage_broker

def fetch_orgs():
    return storage_broker.get(Organisation,None)

def fetch_organisation_by_id(org_id):
    return storage_broker.get(Organisation,{Organisation.id_Organisation:org_id})

def fetch_domains():
    return storage_broker.get(DomainOrganisation)
