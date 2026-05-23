from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlmodel import Session

from app.db.database import get_session

from app.services.csv_service import process_csv_upload
from app.utils.file_helpers import save_uploaded_file

router = APIRouter()

@router.post("/upload-products-csv")
async def upload_products_csv(
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):

    # SAVE CSV TO DISK
    file_path = save_uploaded_file(
        file,
        "app/uploads/csv"
    )

    # PROCESS SAVED FILE
    return process_csv_upload(
        file_path,
        session
    )