
from constants import *
from storage.storage_service.StorageService import *
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker


# engine = create_engine(DB_URI)
def get_engine(db_uri):
    engine = create_engine(db_uri)
    return engine

def get_session(engine):
    # Create the database engine and session
    Session = sessionmaker(bind=engine)
    return Session()

# Function to add an record to a table
def add_record(engine,obj):
    session = get_session(engine)
    session.add(obj)
    session.commit()
    return obj

# Function to get all records from a table
def get_all_records(engine,model_class):
    session = get_session(engine)
    return session.query(model_class).all()

# Function to get an record by ID from a table
def get_record_by_id(engine,model_class, id):
    session = get_session(engine)
    return session.query(model_class).get(id)

# Function to get objects from a table based on conditions
def get_records(engine,model_class, conditions = None):
    session = get_session(engine)
    query = session.query(model_class)
    if conditions:
        for attr, value in conditions.items():
            query = query.filter(getattr(model_class, attr) == value)
    return query.all()

# Function to update an record in a table
def update_record(engine,obj):
    session = get_session(engine)
    session.commit()
    return obj

# Function to delete an record from a table
def delete_record(engine,obj):
    session = get_session(engine)
    session.delete(obj)
    session.commit()