from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from backend.core.security import create_access_token, create_refresh_token, verify_password
from backend.services.user_service import get_user_by_email

router = APIRouter(
    prefix="/auth", 
    tags=["auth"])

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_email(form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Correo electrónico no encontrado"
        )
    
    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Contraseña incorrecta"
        )

    # IMPORTANTE: Usamos el ID del usuario (convertido a string) como "sub"
    user_id_str = str(user["_id"])
    access_token = create_access_token(data={"sub": user_id_str})
    refresh_token = create_refresh_token(data={"sub": user_id_str})
    
    return {
        "access_token": access_token, 
        "refresh_token": refresh_token, 
        "token_type": "bearer"
    }
