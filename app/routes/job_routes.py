from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.db.database import get_session
from app.models.job import Job

router = APIRouter()

@router.get("/jobs")
def get_jobs(
    session: Session = Depends(get_session)
):
    jobs = session.exec(select(Job)).all()
    return jobs