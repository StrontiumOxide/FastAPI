from pydantic import BaseModel
from datetime import datetime

class CreateAnnouncementRequest(BaseModel):
    title: str | None
    description: str | None
    price: int | None
    author: str | None
    

class GetAnnouncementResponse(BaseModel):
    id: int
    title: str
    description: str
    price: int
    author: str
    date_create: datetime


class UpdateAnnouncementRequest(CreateAnnouncementRequest):
    pass


class SearchFieldsAnnouncementRequest(CreateAnnouncementRequest):
    pass
