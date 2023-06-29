
from constants import *
from storage.storage_service.StorageService import *
from sqlalchemy import create_engine, MetaData, Table, select

# engine = create_engine(DB_URI)
def get_engine(db_uri):
    engine = create_engine(db_uri)
    return engine

def get_table(engine, schema_name, table_name):
    metadata = MetaData(bind=engine, schema=schema_name)
    table = Table(table_name, metadata, autoload=True)
    return table

def create_record(engine, schema_name, table_name, data_dict):
    table = get_table(engine, schema_name, table_name)
    with engine.connect() as conn:
        ins = table.insert().values(**data_dict)
        result = conn.execute(ins)
        return result.lastrowid

def read_records(engine, schema_name, table_name, conditions=None):
    table = get_table(engine, schema_name, table_name)
    with engine.connect() as conn:
        if conditions:
            query = select([table]).where(conditions)
        else:
            query = select([table])
        result = conn.execute(query)
        return [dict(row) for row in result]

def update_record(engine, schema_name, table_name, record_id, data_dict):
    table = get_table(engine, schema_name, table_name)
    with engine.connect() as conn:
        stmt = table.update().where(table.c.id == record_id).values(**data_dict)
        conn.execute(stmt)

def delete_record(engine, schema_name, table_name, record_id):
    table = get_table(engine, schema_name, table_name)
    with engine.connect() as conn:
        stmt = table.delete().where(table.c.id == record_id)
        conn.execute(stmt)

