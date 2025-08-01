from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def get_vehicles(db: Session):
    return db.query(Vehicle).all()


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()


def delete_vehicle(db: Session, vehicle_id: int):
    vehicle = get_vehicle(db, vehicle_id)
    if vehicle:
        db.delete(vehicle)
        db.commit()
        return True
    return False
