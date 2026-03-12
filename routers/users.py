from fastapi import APIRouter, Depends, HTTPException, status
from models.user_model import UserBase, UserUpdate 
from db.client import db
from jose import jwt
from schemas.user_schema import user_schema
from core.config import SECRET, ALGORITHM
from fastapi import Request
from dependencies.auth import get_current_user, require_admin
from services.user_service import (
    get_users as get_users_service,
    get_user_by_id,
    create_user as post_create_service,
    update_user as update_user_service,
    delete_user,
    get_user_by_email,
    get_user_by_document
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_user)]
)


'''@router.get("/me", response_model=UserBase, response_model_exclude_none=True)
def read_me(user_dict: dict = Depends(get_current_user)):
    # get_current_user devuelve el diccionario directo de la DB
    return user_schema(user_dict)'''

@router.get("/me")
async def read_me(request: Request):
    try:
        # 1. Identificación por token (como ya lo tienes)
        auth_header = request.headers.get("Authorization")
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        
        # 2. Buscar en 'clients' (con await)
        user_db = await db.clients.find_one({"email": payload.get("sub")})
        
        if user_db:
            user_db["_id"] = str(user_db["_id"])
            
            if "password" in user_db:
                del user_db["password"]
            return user_db 

    except Exception as e:
        raise HTTPException(status_code=401, detail="Sesión inválida")

# Crear usuario
@router.post("/", status_code=201)
async def create_user(New_user: dict, user=Depends(require_admin)):

    user_email =await  get_user_by_email(New_user["email"])

    if user_email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El correo ya se encuentra registrado"
        )
    
    user_document =await  get_user_by_document(New_user["document_number"])

    if user_document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El número de documento ya se encuentra registrado"
        )

    user_dic = dict(New_user)
    if user_dic.get("id"):
        del user_dic["id"]

    resp = await post_create_service(user_dic)
    return resp


# Actualizar usuario
@router.put("/")
async def update_user(data_user: dict, user=Depends(require_admin)):

    id = data_user.get("id")
    if not id:
        raise HTTPException(
            status_code=400,
            detail="ID de usuario es requerido"
        )   
    
    resp = await update_user_service(data_user)
    if not resp:
        raise HTTPException(
            status_code=404,
            detail="Id de usuario invalido"
        )
    return resp


# Eliminar usuario
@router.delete("/{user_id}")
def delete_existing_user(user_id: str, user=Depends(require_admin)):

    db_user = get_user_by_id(user_id)

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    delete_user(user_id)

    return {
        "message": "Usuario eliminado correctamente"
    }

@router.patch("/me/update", response_model=UserBase, response_model_exclude_none=True)
async def update_my_profile(
    user_update: UserUpdate, 
    current_user: UserBase = Depends(get_current_user)
): 
    try:
        # 1. Datos enviados por el usuario
        update_data = user_update.model_dump(exclude_unset=True)

        # 2. Mapeo manual de campos (Soporta nombres en español e inglés)
        if hasattr(user_update, 'telefono') and user_update.telefono:
            update_data["phone"] = update_data.pop("telefono")
        if hasattr(user_update, 'direccion') and user_update.direccion:
            update_data["address"] = update_data.pop("direccion")

        # --- INICIO DE LA SUGERENCIA (LÓGICA ROBUSTA) ---
        
        # Obtenemos person_type de forma segura (funciona si current_user es dict u objeto)
        tipo_actual = getattr(current_user, "person_type", None) or (current_user.get("person_type") if isinstance(current_user, dict) else None)
        tipo = update_data.get("person_type", tipo_actual)

        # Obtenemos el email y company_name de forma segura también
        email_actual = getattr(current_user, "email", None) or (current_user.get("email") if isinstance(current_user, dict) else None)
        empresa_actual = getattr(current_user, "company_name", None) or (current_user.get("company_name") if isinstance(current_user, dict) else None)

        # --- FIN DE LA SUGERENCIA ---

        if tipo in ["Juridica", "Jurídica"]:
            update_data["document_type"] = "NIT"
            # Mantenemos el nombre de la empresa si no se envió uno nuevo
            if "Company_name" not in update_data and empresa_actual:
                update_data["Company_name"] = empresa_actual
            
            await db.clients.update_one({"email": email_actual}, {"$set": update_data})
        else:
            # Si es Natural, eliminamos el campo Company_name
            await db.clients.update_one(
                {"email": email_actual}, 
                {"$set": update_data, "$unset": {"Company_name": ""}}
            )

        # 4. Recuperamos y limpiamos respuesta
        updated_user_db = await db.clients.find_one({"email": email_actual})
        
        if not updated_user_db:
            raise HTTPException(status_code=404, detail="Error al recuperar usuario actualizado")

        return user_schema(updated_user_db)

    except Exception as e:
        print(f"❌ Error en update_user_me: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error interno al actualizar el perfil: {str(e)}"
        )