from pydantic import BaseModel
from datetime import datetime


class IssueBase(BaseModel):
    vehicle_id: int
    spare_part_id: int
    quantity: int


class IssueCreate(IssueBase):
    pass


class IssueOut(IssueBase):
    id: int
    issued_at: datetime

    class Config:
        orm_mode = True
