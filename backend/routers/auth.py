from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from core.security import create_access_token, create_refresh_token, verify_password
from services.user_service import get_user_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    

    user_db = get_user_db(form_data.username)

    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Correo electrónico no registrado"
        )

    if not verify_password(form_data.password, user_db.password):
        raise HTTPException(
            status_code=400,
            detail="Contraseña incorrecta"
        )

    access_token = create_access_token({
        "sub": user_db.email
    })

    refresh_token = create_refresh_token({
        "sub": user_db.email
    })

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }