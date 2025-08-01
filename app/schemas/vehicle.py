from pydantic import BaseModel
from datetime import datetime


class VehicleBase(BaseModel):
    name: str
    type: str


class VehicleCreate(VehicleBase):
    pass


class VehicleOut(VehicleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
