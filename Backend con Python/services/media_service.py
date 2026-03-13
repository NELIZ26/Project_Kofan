import os
import uuid
import shutil
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "static/images"
ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp"]

def save_image(file: UploadFile) -> str:
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return f"/static/images/{filename}"

def save_multiple(files: list[UploadFile]) -> list[str]:
    urls = []

    for file in files:
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="Tipo de archivo no permitido")

        filename = f"{uuid.uuid4()}_{file.filename}"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        urls.append(f"/static/images/{filename}")

    return urls

def delete_image(url: str):
    path = url.replace("/static/", "static/")
    if os.path.exists(path):
        os.remove(path)
        return {"message": "Imagen eliminada."}

    return {"message": "La imagen no existe."}