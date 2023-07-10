
# from core.models import Document
# from storage_broker import get_document
from server.core.models import DomainOrganisation, Organisation, Region, Sector
import server.storage.storage_broker as storage_broker

def fetch_orgs():
    return storage_broker.get(Organisation,None,[Sector,Region])

def fetch_domains():
    return storage_broker.get(DomainOrganisation)
