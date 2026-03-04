from fastapi import APIRouter, Depends, Query, HTTPException, UploadFile, File, Form
from typing import Optional, List
import os
import uuid
import shutil

from models.product_models import ProductCreate, ProductUpdate
from dependencies.auth import require_admin
from services.product_service import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product,
    create_product_with_images,
    remove_product_image
)
from services.media_service import save_multiple, delete_image

router = APIRouter(prefix="/products", tags=["Products"])

UPLOAD_DIR = "static/images"
ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp"]
os.makedirs(UPLOAD_DIR, exist_ok=True)

# CREATE PRODUCT
@router.post("/")
def create(data: ProductCreate, user=Depends(require_admin)):
    return create_product(data.dict(), user.email)

# LIST PRODUCTS
@router.get("/")
def list_products(
    page: int = 1,
    limit: int = 10,
    name: Optional[str] = Query(None),
    active: Optional[bool] = Query(None),
):
    filters = {"name": name, "active": active}
    return get_products(page, limit, filters)

# GET PRODUCT
@router.get("/{product_id}")
def get(product_id: str):
    product = get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# UPDATE PRODUCT
@router.put("/{product_id}")
def update(product_id: str, data: ProductUpdate, user=Depends(require_admin)):
    updated = update_product(
        product_id,
        data.dict(exclude_unset=True, exclude={"id"}),
        user.email,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return updated

# DELETE PRODUCT
@router.delete("/{product_id}")
def delete(product_id: str, user=Depends(require_admin)):
    delete_product(product_id)
    return {"message": "Producto eliminado"}

# UPLOAD SINGLE IMAGE
@router.post("/upload-image")
def upload_image(file: UploadFile = File(...), user=Depends(require_admin)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido")

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    url = f"/static/images/{filename}"
    return {"url": url}

# UPLOAD MULTIPLE IMAGES
@router.post("/create-with-images")
async def create_product_with_images_router(
    name: str = Form(...),
    description: Optional[str] = Form(None),
    price: float = Form(...),
    images: List[UploadFile] = File(...),
    user=Depends(require_admin)
):
    filenames = []

    for image in images:
        extension = image.filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{extension}"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as buffer:
            buffer.write(await image.read())

        filenames.append(filename)

    # DATA BASE
    data = {
        "name": name,
        "description": description,
        "price": price,
    }

    # SERVICE CALL
    return create_product_with_images(data, filenames, user.email)

# ADD IMAGE TO PRODUCT
@router.post("/{product_id}/add-image")
def add_image_to_product(product_id: str, url: str, user=Depends(require_admin)):
    product = get_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    images = product.get("images", [])
    images.append(url)

    return update_product(product_id, {"images": images}, user.email)

# SET MAIN IMAGE
@router.post("/{product_id}/set-main-image")
def set_main_image(product_id: str, url: str, user=Depends(require_admin)):
    product = get_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if url not in product.get("images", []):
        raise HTTPException(status_code=400, detail="La imagen no pertenece al producto")

    return update_product(product_id, {"main_image": url}, user.email)

# DELETE IMAGE
@router.delete("/{product_id}/delete-image")
def delete_product_image(product_id: str, url: str, user=Depends(require_admin)):
    remove_product_image(product_id, url, user.email)
    delete_image(url)

    return {"message": "Imagen eliminada"}