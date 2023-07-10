# these are fixed models, that are not likely
# destined for future changes


from datetime import date
from pydantic import BaseModel, Field
from typing import Optional

class API_Document(BaseModel):
    DocumentID: Optional[int] = Field(default=None)
    DocTypeID: Optional[int] = Field(default=None)
    ContainerID: Optional[int] = Field(default=None)
    StoreID: Optional[int] = Field(default=None)
    DomainID: Optional[int] = Field(default=None)
    ReferenceID: Optional[int] = Field(default=None)
    ContainerPositionID: Optional[int] = Field(default=None)
    ShelfID: Optional[int] = Field(default=None)
    CobID: Optional[int] = Field(default=None)
    BayID: Optional[int] = Field(default=None)
    CabinetID: Optional[int] = Field(default=None)
    DocTypeLabelFR: Optional[str] = Field(default=None)
    DocTypeLabelAR: Optional[str] = Field(default=None)
    ContainerType: Optional[str] = Field(default=None)
    StoreType: Optional[str] = Field(default=None)
    StoreLabelFR: Optional[str] = Field(default=None)
    StoreLabelAR: Optional[str] = Field(default=None)
    StoreAcronymFR: Optional[str] = Field(default=None)
    StoreAcronymAR: Optional[str] = Field(default=None)
    DocumentData: Optional[bytes] = Field(default=None)
    DomainLabelFR: Optional[str] = Field(default=None)
    DomainLabelAR: Optional[str] = Field(default=None)
    DomainAcronymFR: Optional[str] = Field(default=None)
    DomainAcronymAR: Optional[str] = Field(default=None)
    BelongingCode: Optional[str] = Field(default=None)
    ReferenceYear: Optional[int] = Field(default=None)
    ReferenceAR: Optional[str] = Field(default=None)
    ReferenceFR: Optional[str] = Field(default=None)
    DocumentLabel: Optional[str] = Field(default=None)

class API_Organisation(BaseModel):
    OrgID: Optional[int] = Field(default=None)
    RegionID: Optional[int] = Field(default=None)
    SectorID: Optional[int] = Field(default=None)
    RegionLabelFR: Optional[str] = Field(default=None)
    RegionLabelAR: Optional[str] = Field(default=None)
    RegionAcronymFR: Optional[str] = Field(default=None)
    RegionAcronymAR: Optional[str] = Field(default=None)
    SectorLabelFR: Optional[str] = Field(default=None)
    SectorLabelAR: Optional[str] = Field(default=None)
    SectorAcronymFR: Optional[str] = Field(default=None)
    SectorAcronymAR: Optional[str] = Field(default=None)
    OrgNameAR: Optional[str] = Field(default=None)
    OrgNameFR: Optional[str] = Field(default=None)
    OrgAcronymAR: Optional[str] = Field(default=None)
    OrgAcronymFR: Optional[str] = Field(default=None)

class API_Elimination(BaseModel):
    EliminationIu: Optional[int] = Field(default=None)
    TranscriptIu: Optional[int] = Field(default=None)
    TranscriptReference: Optional[str] = Field(default=None)
    MaxEliminationDate: Optional[date] = Field(default=None)
    MinEliminationDate: Optional[date] = Field(default=None)


class API_User(BaseModel):
    UserID: Optional[int]= Field(default=None)
    UserName: Optional[str]= Field(default=None)
    UserPassword: Optional[str]= Field(default=None)
    AdminPrivilege: Optional[bool]= Field(default=None)
    
    
class API_Person(BaseModel):
    RankID: Optional[int] = Field(default=None)
    PersonDomainID: Optional[int] = Field(default=None)
    ProfileID: Optional[int] = Field(default=None)
    PersonID: Optional[int] = Field(default=None)
    TraineeID: Optional[int] = Field(default=None)
    SessionID: Optional[int] = Field(default=None)
    CurrentOrgID: Optional[int] = Field(default=None)
    CurrentOrgDomainID: Optional[int] = Field(default=None)
    CurrentSectorID: Optional[int] = Field(default=None)
    ProfileSerial: Optional[str] = Field(default=None)
    DomainLabelFR: Optional[str] = Field(default=None)
    DomainLabelAR: Optional[str] = Field(default=None)
    DomainAcronymFR: Optional[str] = Field(default=None)
    DomainAcronymAR: Optional[str] = Field(default=None)
    PersonName: Optional[str] = Field(default=None)
    PersonLastname: Optional[str] = Field(default=None)
    SessionStartDate: Optional[date] = Field(default=None)
    SessionEndDate: Optional[date] = Field(default=None)
    OrgLabelAR: Optional[str] = Field(default=None)
    OrgLabelFR: Optional[str] = Field(default=None)
    OrgAcronymAR: Optional[str] = Field(default=None)
    OrgAcronymFR: Optional[str] = Field(default=None)
        
        
