# these are fixed models, that are not likely
# destined for future changes


from datetime import date
from pydantic import BaseModel

class API_Document(BaseModel):
    Doc_ID: int
    idDocument_type: int
    document_type_label_fr: str
    document_type_label_ar: str
    idContainer: int
    type_container: str
    idStore: int
    Storetype: str
    store_label_fr: str
    store_label_ar: str
    store_acronym_fr: str
    store_acronym_ar: str
    Document_data: bytes
    idDomain_Organisation: int
    Domain_Organisation_label_fr: str
    Domain_Organisation_label_ar: str
    Domain_Organisation_acronym_fr: str
    Domain_Organisation_acronym_ar: str
    belonging_code: str
    reference_id: int
    reference_year: int
    reference_ar: str
    reference_fr: str
    Doc_Label: str
    idContainer_position: int
    idShelf: int
    idCob: int
    idBay: int
    idCabinet: int

class API_Organisation(BaseModel):
    id_Organisation: int
    idRegion: int
    region_label_fr: str
    region_label_ar: str
    region_acronym_fr: str
    region_acronym_ar: str
    idSector: int
    label_sector_fr: str
    label_sector_ar: str
    acronym_sector_fr: str
    acronym_sector_ar: str
    Organisation_name_ar: str
    Organisation_name_fr: str
    organisation_acronym_ar: str
    organisation_acronym_fr: str

class API_Elimination(BaseModel):
    idElimination: int
    idTranscript: int
    reference_transcript: str
    max_eliminated_date: date
    min_eliminated_date: date

class API_Person(BaseModel):
    idprofile_rank: int
    profile_rank_label_fr: str
    profile_rank_label_ar: str
    profile_rank_acronym_fr: str
    profile_rank_acronym_ar: str
    idProfile: int
    Profile_serial: str
    idDomain_Organisation: int
    Domain_Organisation_label_fr: str
    Domain_Organisation_label_ar: str
    Domain_Organisation_acronym_fr: str
    Domain_Organisation_acronym_ar: str
    PERSON_ID: int
    Person_name: str
    Person_lastname: str
    idtrainee: int
    idsession: int
    session_start_date: date
    session_end_date: date

class API_User(BaseModel):
    USER_ID: int
    USER_NAME: str
    USER_PASSWORD: str
    admin_privilege: bool
