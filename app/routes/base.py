from app.routes import (
    get_student,
    create_student,
    update_student,
    delete_student
)

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(get_student.router)
api_router.include_router(create_student.router)
api_router.include_router(update_student.router)
api_router.include_router(delete_student.router)