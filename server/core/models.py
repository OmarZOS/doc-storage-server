
import enum
from pydantic import BaseModel


# this enum is used to respond to queries
class QUERY_RESULTS(enum.Enum):
   SUCCESS = 1
   FAILED = 2
   TIMEDOUT = 3
   UNKNOWN = 4

# requesting from the server using this query model
class document_model(BaseModel):
    id: str
    content: str
    description: str | None = None
    length: int | None = None

# building third party queries is made using this model
class Query:
    table_name : str
    fields : str
    conditions : str | None = None