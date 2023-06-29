# these are fixed models, that are not likely
# destined for future changes

from sqlalchemy import Column, Date, Integer, LargeBinary, SmallInteger, String
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class API_Document(Base):
    __tablename__ = 'Document'
    Doc_ID = Column(Integer, nullable=False)
    idDocument_type = Column(Integer)
    document_type_label_fr = Column(String(45))
    document_type_label_ar = Column(String(45))
    
    idContainer = Column(Integer)
    type_container = Column(String(45))
    
    idStore = Column(Integer)
    Storetype = Column(String(45))
    store_label_fr = Column(String(45))
    store_label_ar = Column(String(45))
    store_acronym_fr = Column(String(45))
    store_acronym_ar = Column(String(45))
    Document_data = Column(LargeBinary)
    
    idDomain_Organisation = Column(Integer)
    Domain_Organisation_label_fr = Column(String(45))
    Domain_Organisation_label_ar = Column(String(45))
    Domain_Organisation_acronym_fr = Column(String(45))
    Domain_Organisation_acronym_ar = Column(String(45))
    belonging_code = Column(String(45))
    
    reference_id = Column(Integer)
    reference_year = Column(Integer)
    reference_ar = Column(String(45))
    reference_fr = Column(String(45))
    
    Doc_Label = Column(String(255))
    
    idContainer_position = Column(Integer)
    idShelf = Column(Integer)
    idCob = Column(Integer)
    idBay = Column(Integer)
    idCabinet = Column(Integer)

class API_Organisation(Base):
    __tablename__ = 'Source'
    id_Organisation = Column(Integer)
    
    idRegion = Column(Integer)
    region_label_fr = Column(String(45))
    region_label_ar = Column(String(45))
    region_acronym_fr = Column(String(45))
    region_acronym_ar = Column(String(45))
    
    idSector = Column(Integer)
    label_sector_fr = Column(String(45))
    label_sector_ar = Column(String(45))
    acronym_sector_fr = Column(String(45))
    acronym_sector_ar = Column(String(45))
    
    Organisation_name_ar = Column(String(255))
    Organisation_name_fr = Column(String(255))
    organisation_acronym_ar = Column(String(45))
    organisation_acronym_fr = Column(String(45))

class API_Elimination(Base):
    __tablename__ = 'Elimination'
    idElimination = Column(Integer, nullable=False)
    idTranscript = Column(Integer)
    reference_transcript = Column(String(45))
    max_eliminated_date = Column(Date)
    min_eliminated_date = Column(Date)

class API_Person(Base):
    __tablename__ = 'Person'
    
    idprofile_rank = Column(Integer)
    profile_rank_label_fr = Column(String(45))
    profile_rank_label_ar = Column(String(45))
    profile_rank_acronym_fr = Column(String(45))
    profile_rank_acronym_ar = Column(String(45))
    
    idProfile = Column(Integer)
    Profile_serial = Column(String(45))
    
    idDomain_Organisation = Column(Integer)
    Domain_Organisation_label_fr = Column(String(45))
    Domain_Organisation_label_ar = Column(String(45))
    Domain_Organisation_acronym_fr = Column(String(45))
    Domain_Organisation_acronym_ar = Column(String(45))
    
    PERSON_ID = Column(Integer)
    Person_name = Column(String(45))
    Person_lastname = Column(String(45))
    
    idtrainee = Column(Integer)
    idsession = Column(Integer)
    session_start_date = Column(Date)
    session_end_date = Column(Date)

class API_User(Base):
    __tablename__ = 'User'
    USER_ID = Column(Integer)
    USER_NAME = Column(String(45))
    USER_PASSWORD = Column(String(255))
    admin_privilege = Column(TINYINT)
