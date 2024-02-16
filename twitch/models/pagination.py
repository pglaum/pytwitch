from pydantic import BaseModel


class Pagination(BaseModel):
    cursor: str
