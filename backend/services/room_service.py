from bson import ObjectId
from datetime import datetime, timezone
from backend.db.client import db 
from backend.schemas.room_schema import room_schema, rooms_schema


collection = db.rooms

# --- CREATE ---
async def create_room(data: dict, user_email: str):
    now = datetime.now(timezone.utc)

    data["created_by"] = user_email
    data["updated_by"] = user_email
    data["created_at"] = now
    data["updated_at"] = now
    
    # Por defecto, una habitación nueva debe estar disponible para el dashboard
    if "is_available" not in data:
        data["is_available"] = True

    # Motor requiere await para insertar
    result = await collection.insert_one(data)
    
    # Buscamos el objeto recién creado para devolverlo con el esquema
    new_room = await collection.find_one({"_id": result.inserted_id})
    return room_schema(new_room)

# --- CREATE WITH IMAGES ---
async def create_room_with_images(data: dict, images: list[str], user_email: str):
    data["images"] = images

    if images:
        data["main_image"] = images[0]

    # Llamamos a la función asíncrona de arriba con await
    return await create_room(data, user_email)

# --- GET ONE ---
async def get_room(room_id: str):
    # Convertimos el string a ObjectId y esperamos el resultado
    room = await collection.find_one({"_id": ObjectId(room_id)})
    if not room:
        return None # Es mejor retornar None para que el router maneje el 404
    return room_schema(room)

# --- LIST WITH ADVANCED FILTER ---
async def get_rooms(page: int, limit: int, filters: dict):
    skip = (page - 1) * limit
    query = {}

    # Lógica de filtros (se mantiene igual, es solo construcción de diccionario)
    if filters.get("name"):
        query["name"] = {"$regex": filters["name"], "$options": "i"}
    if filters.get("active") is not None:
        query["active"] = filters["active"]
    if filters.get("min_price") is not None:
        query.setdefault("price", {})["$gte"] = filters["min_price"]
    if filters.get("max_price") is not None:
        query.setdefault("price", {})["$lte"] = filters["max_price"]

    # Motor usa cursores. Para convertirlos a lista usamos to_list()
    cursor = collection.find(query).skip(skip).limit(limit)
    rooms_list = await cursor.to_list(length=limit)
    
    # Contamos los documentos de forma asíncrona
    total = await collection.count_documents(query)

    return {
        "data": rooms_schema(rooms_list), # Asegúrate que rooms_schema acepte la lista
        "total": total,
        "page": page,
        "limit": limit,
    }

# --- UPDATE ---
async def update_room(room_id: str, data: dict, user_email: str):
    data["updated_by"] = user_email
    data["updated_at"] = datetime.now(timezone.utc)

    # Actualizamos con await
    await collection.update_one({"_id": ObjectId(room_id)}, {"$set": data})
    
    # Retornamos la habitación actualizada
    return await get_room(room_id)

# --- REMOVE IMAGE FROM ROOM ---
async def remove_room_image(room_id: str, url: str, user_email: str):
    room = await get_room(room_id)
    if not room:
        return None

    images = room.get("images", [])
    if url in images:
        images.remove(url)

    update_data = {"images": images}
    # Si borramos la imagen principal, ponemos la siguiente o None
    if room.get("main_image") == url:
        update_data["main_image"] = images[0] if images else None

    return await update_room(room_id, update_data, user_email)

# --- DELETE ---
async def delete_room(room_id: str):
    result = await collection.delete_one({"_id": ObjectId(room_id)})
    if result.deleted_count == 0:
        return False
    return True