# here, we make schema translations

from server.core.api_models import API_Person
from server.core.models import *
from server.features.insertion import insert_or_complete_or_raise

def insert_person(api_person: API_Person):
    
    organisation = Organisation(id_Organisation=api_person.CurrentOrgID,Organisation_name_ar=api_person.OrgLabelAR,Organisation_name_fr=api_person.OrgLabelFR,ACRONYM_AR=api_person.OrgAcronymAR,ACRONYM_FR=api_person.OrgAcronymFR,Organisation_domain_id_ref=api_person.CurrentOrgDomainID,sector_ref_id=api_person.CurrentSectorID)
    code,organisation,msg = insert_or_complete_or_raise(organisation)
    if (code == 1): return msg
    
    profile = Profile(idProfile=api_person.ProfileID,Profile_serial=api_person.ProfileSerial,Profile_rank_id_ref = api_person.RankID,Profile_position_org=organisation.id_Organisation,Profile_domain_id_ref=api_person.PersonDomainID)
    code,profile,msg = insert_or_complete_or_raise(profile)
    if (code == 1): return msg
    
    person = Person(PERSON_ID = api_person.PersonID,Person_name = api_person.PersonName,Person_lastname = api_person.PersonLastname,Person_profile_id_ref = profile.idProfile)
    code,person,msg = insert_or_complete_or_raise(person)
    if (code == 1): return msg
    
    return person
    
def insert_trainee(api_trainee: API_Person):
    
    person = insert_person(api_trainee)
    if(type(person) != Person): return person
    
    session = Session(idsession=api_trainee.idsession,session_start_date=api_trainee.session_start_date,session_end_date=api_trainee.session_end_date)
    code,session,msg = insert_or_complete_or_raise(session)
    if (code == 1): return msg
    
    trainee = Trainee(idtrainee = api_trainee.idtrainee,profile_ref_id=person.Person_profile_id_ref,session_ref_id=session.idsession,trainee_mark=api_trainee.trainee_mark,trainee_evaluation=api_trainee.trainee_evaluation)
    code,trainee,msg = insert_or_complete_or_raise(trainee)
    if (code == 1): return msg
    
    return trainee

