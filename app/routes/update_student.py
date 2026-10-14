from app.database import get_db
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model_db_schema import Student
from app.schema import StudentUpdate, StudentResponse

router = APIRouter(prefix="/students", tags=["Update Student"])

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id : int, student : StudentUpdate, db : Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student is not found",
        )
    
    update_data = student.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
    
    db.commit()
    db.refresh(db_student)
    return db_student