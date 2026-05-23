from sqlmodel import Session

from app.models.job import Job

def create_job(
    session: Session,
    job_type: str
):

    job = Job(
        type=job_type,
        status="PENDING",
        progress=0
    )

    session.add(job)
    session.commit()
    session.refresh(job)

    return job

def update_job_status(
    session: Session,
    job: Job,
    status: str,
    progress: int
):

    job.status = status
    job.progress = progress

    session.add(job)
    session.commit()