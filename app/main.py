from app.db.database import Base, engine
from app.models import user
from fastapi import FastAPI
from app.routers import auth, vehicle, spare_part, issue
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)


app = FastAPI()

# CORS middleware (allow frontend to access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(vehicle.router)
app.include_router(spare_part.router)
app.include_router(issue.router)
