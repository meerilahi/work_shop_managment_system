from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.vehicle import VehicleCreate, VehicleOut
from app.crud import vehicle as crud
from app.db.deps import get_db
from typing import List

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/", response_model=VehicleOut)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return crud.create_vehicle(db, vehicle)


@router.get("/", response_model=List[VehicleOut])
def list_vehicles(db: Session = Depends(get_db)):
    return crud.get_vehicles(db)


@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    success = crud.delete_vehicle(db, vehicle_id)
    return {"deleted": success}
