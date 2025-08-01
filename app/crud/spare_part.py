from sqlalchemy.orm import Session
from app.models.spare_part import SparePart
from app.schemas.spare_part import SparePartCreate, SparePartUpdate


def create_spare_part(db: Session, part: SparePartCreate):
    db_part = SparePart(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part


def get_spare_parts(db: Session):
    return db.query(SparePart).all()


def get_spare_part(db: Session, part_id: int):
    return db.query(SparePart).filter(SparePart.id == part_id).first()


def update_quantity(db: Session, part_id: int, quantity: int):
    part = get_spare_part(db, part_id)
    if part:
        part.quantity += quantity
        db.commit()
        db.refresh(part)
        return part
    return None


def delete_spare_part(db: Session, part_id: int):
    part = get_spare_part(db, part_id)
    if part:
        db.delete(part)
        db.commit()
        return True
    return False
