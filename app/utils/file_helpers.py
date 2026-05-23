import os
import uuid

def save_uploaded_file(file, folder_path):

    os.makedirs(folder_path, exist_ok=True)

    filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path