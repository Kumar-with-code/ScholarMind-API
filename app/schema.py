from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    student_name: str
    student_class: str
    student_section: str
    student_dob: date


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    student_class: Optional[str] = None
    student_section: Optional[str] = None
    student_dob: Optional[date] = None


class StudentResponse(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # Pydantic v2 Config
    model_config = ConfigDict(from_attributes=True)