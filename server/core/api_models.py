# these are fixed models, that are not likely
# destined for future changes


from datetime import date
from pydantic import BaseModel
from typing import Optional

class API_Document(BaseModel):
    Doc_ID: Optional[int]
    idDocument_type: Optional[int]
    document_type_label_fr: Optional[str]
    document_type_label_ar: Optional[str]
    idContainer: Optional[int]
    type_container: Optional[str]
    idStore: Optional[int]
    Storetype: Optional[str]
    store_label_fr: Optional[str]
    store_label_ar: Optional[str]
    store_acronym_fr: Optional[str]
    store_acronym_ar: Optional[str]
    Document_data: Optional[bytes]
    idDomain_Organisation: Optional[int]
    Domain_Organisation_label_fr: Optional[str]
    Domain_Organisation_label_ar: Optional[str]
    Domain_Organisation_acronym_fr: Optional[str]
    Domain_Organisation_acronym_ar: Optional[str]
    belonging_code: Optional[str]
    reference_id: Optional[int]
    reference_year: Optional[int]
    reference_ar: Optional[str]
    reference_fr: Optional[str]
    Doc_Label: Optional[str]
    idContainer_position: Optional[int]
    idShelf: Optional[int]
    idCob: Optional[int]
    idBay: Optional[int]
    idCabinet: Optional[int]

class API_Organisation(BaseModel):
    id_Organisation: Optional[int]
    idRegion: Optional[int]
    region_label_fr: Optional[str]
    region_label_ar: Optional[str]
    region_acronym_fr: Optional[str]
    region_acronym_ar: Optional[str]
    idSector: Optional[int]
    label_sector_fr: Optional[str]
    label_sector_ar: Optional[str]
    acronym_sector_fr: Optional[str]
    acronym_sector_ar: Optional[str]
    Organisation_name_ar: Optional[str]
    Organisation_name_fr: Optional[str]
    organisation_acronym_ar: Optional[str]
    organisation_acronym_fr: Optional[str]

class API_Elimination(BaseModel):
    idElimination: Optional[int]
    idTranscript: Optional[int]
    reference_transcript: Optional[str]
    max_eliminated_date: Optional[date]
    min_eliminated_date: Optional[date]

class API_Person(BaseModel):
    idprofile_rank: Optional[int]
    profile_rank_label_fr: Optional[str]
    profile_rank_label_ar: Optional[str]
    profile_rank_acronym_fr: Optional[str]
    profile_rank_acronym_ar: Optional[str]
    idProfile: Optional[int]
    Profile_serial: Optional[str]
    idDomain_Organisation: Optional[int]
    Domain_Organisation_label_fr: Optional[str]
    Domain_Organisation_label_ar: Optional[str]
    Domain_Organisation_acronym_fr: Optional[str]
    Domain_Organisation_acronym_ar: Optional[str]
    PERSON_ID: Optional[int]
    Person_name: Optional[str]
    Person_lastname: Optional[str]
    idtrainee: Optional[int]
    idsession: Optional[int]
    session_start_date: Optional[date]
    session_end_date: Optional[date]

class API_User(BaseModel):
    USER_ID: Optional[int]
    USER_NAME: Optional[str]
    USER_PASSWORD: Optional[str]
    admin_privilege: Optional[bool]
