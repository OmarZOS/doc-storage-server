# here, we make schema translations

from server.core.api_models import API_Person
from server.core.models import *
from server.features.insertion import insert_or_complete_or_raise

def insert_person(api_person: API_Person):
    
    organisation = Organisation(id_Organisation=api_person.id_Organisation,Organisation_name_ar=api_person.Organisation_name_ar,Organisation_name_fr=api_person.Organisation_name_fr,ACRONYM_AR=api_person.ACRONYM_AR,ACRONYM_FR=api_person.ACRONYM_FR,Organisation_domain_id_ref=api_person.Organisation_domain_id_ref,sector_ref_id=api_person.sector_ref_id)
    code,organisation,msg = insert_or_complete_or_raise(organisation)
    if (code == 1): return msg
    
    profile = Profile(idProfile=api_person.idProfile,Profile_serial=api_person.Profile_serial,Profile_rank_id_ref = api_person.idprofile_rank,Profile_position_org=organisation.id_Organisation,Profile_domain_id_ref=api_person.idDomain_Organisation)
    code,profile,msg = insert_or_complete_or_raise(profile)
    if (code == 1): return msg
    
    person = Person(PERSON_ID = api_person.PERSON_ID,Person_name = api_person.Person_name,Person_lastname = api_person.Person_lastname,Person_profile_id_ref = profile.idProfile)
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