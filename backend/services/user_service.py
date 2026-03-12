from backend.db.client import db # Esta es la buena, donde está MongoClient
from backend.core.security import hash_password
from bson import ObjectId 


async def create_user_service(user_data):
    user_dict = user_data.model_dump()
    
    user_dict["password"] = hash_password(user_data.password)
    
    result = await db.users.insert_one(user_dict)
    
    return str(result.inserted_id)



async def update_user_service(user_id: str, update_data: dict):
    # 1. Ejecutar la actualización en la DB
    await db.users.update_one(
        {"_id": ObjectId(user_id)}, 
        {"$set": update_data}
    )
    # 2. Traer el usuario actualizado para devolverlo
    return await db.users.find_one({"_id": ObjectId(user_id)})


async def delete_user_service(user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    
    return result.deleted_count > 0



#PARA REGISTRO DE USUARIOS NUEVO CON EMAIL Y DOCUMENTO
async def get_user_by_email(email: str):
    return await db.users.find_one({"email": email})

async def get_user_by_document(doc: str):
    return await db.users.find_one({"document_number": doc})

#PARA OBTENER USUARIOS POR ID (POR EJEMPLO, PARA EL TOKEN)
async def get_user_by_id(user_id: str):
    return await db.users.find_one({"_id": ObjectId(user_id)})

async def get_all_users_service():
    users_cursor = db.users.find()
    users = await users_cursor.to_list(length=100) # Trae los primeros 100
    for user in users:
        user["_id"] = str(user["_id"])
        user.pop("password", None) # NUNCA envíes contraseñas al frontend
    return users


#Esto aun no esta implementado en el router, pero es para desactivar usuarios sin borrarlos (por ejemplo, para no perder su historial de reservas)---------------------------------
async def deactivate_user_service(user_id: str):
    result = await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"is_active": False}}
    )
    # Cambiamos modified_count por matched_count
    return result.matched_count > 0