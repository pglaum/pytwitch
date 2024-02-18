from pydantic import BaseModel
from typing import Optional


class Pagination(BaseModel):
    cursor: Optional[str]
