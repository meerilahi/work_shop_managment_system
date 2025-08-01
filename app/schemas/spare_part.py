from pydantic import BaseModel
from datetime import datetime


class SparePartBase(BaseModel):
    name: str
    price: float
    quantity: int


class SparePartCreate(SparePartBase):
    pass


class SparePartUpdate(BaseModel):
    quantity: int


class SparePartOut(SparePartBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
