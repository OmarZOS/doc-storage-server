
import enum
from pydantic import BaseModel



class QUERY_RESULTS(enum.Enum):
   SUCCESS = 1
   FAILED = 2
   TIMEDOUT = 3
   UNKNOWN = 4


class document_model(BaseModel):
    id: str
    content: bin
    description: str | None = None
    length: int | None = None