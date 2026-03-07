from fastapi import APIRouter, HTTPException, status
from backend.services.user_service import get_user_by_email, get_user_by_document, create_user_service
from backend.schemas.user_schema import UserCreate

router = APIRouter(
    prefix="/register",
    tags=["register"]
)

@router.post("/register", status_code=201)
async def register_user(new_user: UserCreate):
    # 1. Verificar si el correo ya existe en la base de datos
    if get_user_by_email(new_user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado."
        )
    
    # 2. Verificar si el documento ya existe en la base de datos
    if get_user_by_document(new_user.document_number):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El número de documento ya está registrado."
        )

    # 3. Guardar en la base de datos
    # Aquí es donde ocurre la magia: el servicio hashea y guarda.
    new_id = create_user_service(new_user)
    
    return {
        "message": "Usuario registrado exitosamente en Kofán Hospedaje",
        "user_id": new_id
    }