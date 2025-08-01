from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.spare_part import SparePartCreate, SparePartOut
from app.crud import spare_part as crud
from app.db.deps import get_db
from typing import List

router = APIRouter(prefix="/parts", tags=["Spare Parts"])


@router.post("/", response_model=SparePartOut)
def create_part(part: SparePartCreate, db: Session = Depends(get_db)):
    return crud.create_spare_part(db, part)


@router.get("/", response_model=List[SparePartOut])
def list_parts(db: Session = Depends(get_db)):
    return crud.get_spare_parts(db)


@router.delete("/{part_id}")
def delete_part(part_id: int, db: Session = Depends(get_db)):
    success = crud.delete_spare_part(db, part_id)
    return {"deleted": success}
