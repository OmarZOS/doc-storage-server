

import os


# # getting a list of scylla node names ["node1","node2"]
# SCYLLA_NODES = os.getenv("SCYLLA_NODES").split(",")
# SCYLLA_KEYSPACE = os.getenv("SCYLLA_DEFAULT_KEYSPACE")







ELASTIC_SCHEME = os.getenv("ELASTIC_SCHEME")
ELASTIC_HOST = os.getenv("ELASTIC_HOST")
ELASTIC_PORT = os.getenv("ELASTIC_PORT")


SQL_SCHEMA = os.getenv("SQL_SCHEMA")
SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DATABASE = os.getenv("SQL_DATABASE")
DB_URI = f"{SQL_SCHEMA}://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DATABASE}"

DOCUMENT_DATABASE_NAME = "MYSQL_SERVICE"

DOCUMENT_TABLE_NAME = "Document"
DOCUMENT_CHUNK_TABLE_NAME = "Document"


