from bson import ObjectId
from models.user_model import UserBase


def user_schema(client) -> dict:
    if not client: return {}

    #Extraemos el ID
    client_id = str(client.get("_id")) if "_id" in client else client.get("id")

    #  Construyo el diccionario base
    res ={
        "id": client_id,
        "person_type": client.get("person_type") or client.get("tipo_persona"), 
        "full_name": client.get("full_name"),
        "document_type": client.get("document_type"),
        "document_number": client.get("document_number"),
        "email": client.get("email"),
        "rol_id": client.get("rol_id", "client"),
        "disabled": client.get("disabled", False),
        "phone": client.get("phone") or client.get("telefono"),      
        "address": client.get("address") or client.get("direccion")
    }

    # Lógica para mostrar company_name si es Jurídica
    p_type = res.get("person_type")
    if p_type in ["Jurídica", "Juridica", "juridica"]:
        res["company_name"] = client.get("company_name") or client.get("nombre_empresa")
    else:
        res["company_name"] = None

    return res

def users_schema(clients) -> list:
    return [user_schema(user) for user in clients]