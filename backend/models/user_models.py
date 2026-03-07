from bson import ObjectId

def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "role": user["role"],
        "hashed_password": user["hashed_password"],
    }