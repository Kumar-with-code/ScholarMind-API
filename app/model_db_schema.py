from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, DateTime
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_name = Column(String, index=True, nullable=False)
    student_class = Column(String, nullable=False)
    student_section = Column(String, nullable=False)
    student_dob = Column(Date, nullable=False)

    # Add timestamp columns
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)