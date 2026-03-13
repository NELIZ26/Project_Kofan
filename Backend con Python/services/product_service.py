from db.client import db
from bson import ObjectId
from datetime import datetime, timezone
from schemas.product_schema import product_schema, products_schema

collection = db.products

# CREATE
def create_product(data: dict, user_email: str):
    now = datetime.now(timezone.utc)

    data["created_by"] = user_email
    data["updated_by"] = user_email
    data["created_at"] = now
    data["updated_at"] = now

    result = collection.insert_one(data)

    return product_schema(collection.find_one({"_id": result.inserted_id}))

# CREATE WITH IMAGES
def create_product_with_images(data: dict, images: list[str], user_email: str):
    data["images"] = images

    if images:
        data["main_image"] = images[0]

    return create_product(data, user_email)

# GET ONE
def get_product(product_id: str):
    product = collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise ValueError("Producto no encontrado")
    return product_schema(product)

# LIST WITH ADVANCED FILTER
def get_products(page: int, limit: int, filters: dict):
    skip = (page - 1) * limit
    query = {}

    if filters.get("name"):
        query["name"] = {"$regex": filters["name"], "$options": "i"}

    if filters.get("active") is not None:
        query["active"] = filters["active"]

    if filters.get("min_price") is not None:
        query.setdefault("price", {})["$gte"] = filters["min_price"]

    if filters.get("max_price") is not None:
        query.setdefault("price", {})["$lte"] = filters["max_price"]

    if filters.get("stock_gt") is not None:
        query["stock"] = {"$gt": filters["stock_gt"]}

    cursor = collection.find(query).skip(skip).limit(limit)
    total = collection.count_documents(query)

    return {
        "data": products_schema(cursor),
        "total": total,
        "page": page,
        "limit": limit,
    }

# UPDATE
def update_product(product_id: str, data: dict, user_email: str):
    data["updated_by"] = user_email
    data["updated_at"] = datetime.now(timezone.utc)

    collection.update_one({"_id": ObjectId(product_id)}, {"$set": data})
    
    return get_product(product_id)

# REMOVE IMAGE FROM PRODUCT
def remove_product_image(product_id: str, url: str, user_email: str):
    product = get_product(product_id)

    images = product.get("images", [])
    if url in images:
        images.remove(url)

    update = {"images": images}
    if product.get("main_image") == url:
        update["main_image"] = images[0] if images else None

    return update_product(product_id, update, user_email)

# DELETE
def delete_product(product_id: str):
    result = collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise ValueError("Error al eliminar el producto: no encontrado.")
    return {"message": "Producto eliminado."}