from fastapi import FastAPI
from app.database import engine, Base
from app.routes.base import api_router


# automatically creates databse tables if not exists
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ScholarMind API",
    description="Student Management REST API built with FastAPI, SQLAlchemy, and Pydantic v2", 
    version="1.0.0"
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {"Message": "Hey helo from EWB courses"}