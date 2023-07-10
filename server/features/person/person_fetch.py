
from server.core.models import DomainOrganisation, Organisation, Person, Profile, ProfileRank, Region, Sector, Session
import server.storage.storage_broker as storage_broker


def fetch_personnel():
    return storage_broker.get(Person,None,[Profile,ProfileRank,Organisation,Sector,Region])

def fetch_region_personnel(RegionID:int):
    return storage_broker.get(Person,{Region.idRegion:RegionID},[Profile,ProfileRank,Organisation,Sector,Region])

def fetch_sector_personnel(SectorID:int):
    return storage_broker.get(Person,{Sector.idSector:SectorID},[Profile,ProfileRank,Organisation,Sector])

def fetch_domain_personnel(DomainID:int):
    return storage_broker.get(Person,{DomainOrganisation.idDomain_Organisation:DomainID},[Profile,ProfileRank,DomainOrganisation])

def fetch_person(PersonID:int):
    return storage_broker.get(Person,{Person.PERSON_ID:PersonID},[Profile,ProfileRank,Organisation,Sector])

def fetch_personnel_by_rank(RankID:int):
    return storage_broker.get(Person,{ProfileRank.idprofile_rank:RankID},[Profile,ProfileRank,Organisation,Sector])





def fetch_sessions():
    return storage_broker.get(Session,None,None)














