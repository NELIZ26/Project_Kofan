from db.client import db
from models.user_model import UserBase
from bson import ObjectId
from bson.errors import InvalidId
from core.security import hash_password 
from schemas.user_schema import user_schema


collection = db["clients"]


async def get_user_by_email(email: str):

    client = await collection.find_one({"email": email})
    return user_schema(client) if client else None 

async def get_user_by_document(document: str):

    client = await collection.find_one({"document": document})
    if not client:
        return None
    return user_schema(client)
 

async def get_user_db(email: str):
    print(f"DEBUG: Buscando exactamente: '{email}'") 
    user = await collection.find_one({"email": email})
    if user:
        print(f"DEBUG: Usuario encontrado en Atlas: {user.get('email')}")
    else:
        print("DEBUG: Usuario NO encontrado")
    return user


async def get_users(page: int, limit: int):

    skip = (page - 1) * limit

    cursor = collection.find().skip(skip).limit(limit)
    clients = []

    async for client in cursor:
        clients.append(user_schema(client))

    return clients



async def get_user_by_id(client_id: str):
    try:
        objeto_id = ObjectId(client_id)
        client = await collection.find_one({"_id": objeto_id})
        return user_schema(client) if client else None
    except Exception:
        return None



async def create_user(data: dict):
    if "password" in data:
        data["password"] = hash_password(data["password"])
    result = await collection.insert_one(data)
    new_user = await collection.find_one({"_id": result.inserted_id})
    return UserBase(**user_schema(new_user))


async def update_user(data: dict):
    if "password" in data:
        data["password"] = hash_password(data["password"])

    try:
        user_id=data.get("id")
        object_id = ObjectId(user_id)
    except (InvalidId, TypeError):
        return None

    client_dict = dict(data)
    if "id" in client_dict:
        del client_dict["id"]


    result = await collection.find_one_and_replace(
        {"_id": object_id},
        client_dict,
        return_document= True
    )
    if not result:
        return None
    
    update_user = await get_user_by_id(user_id)
    return UserBase(**update_user) if update_user else None


async def delete_user(client_id: str):
    return await collection.delete_one({"_id": ObjectId(client_id)})
