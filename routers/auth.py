from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from core.security import create_access_token, create_refresh_token, verify_password
from services.user_service import get_user_by_email, get_user_db
from models.user_model import UserPassword

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=None)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    

    client_db = await get_user_db(form_data.username)

    if not client_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Correo electrónico no registrado"
        )

    if not verify_password(form_data.password, client_db["password"]):
        raise HTTPException(
            status_code=400,
            detail="Contraseña incorrecta"
        )
    
    access_token = create_access_token({
        "sub": client_db["email"]
    })

    refresh_token = create_refresh_token({
        "sub": client_db["email"]
    })
   
    try:
        client_db["id"] = str(client_db["_id"])
        if "_id" in client_db:
            del client_db["_id"]

        client_db["phone"]= client_db.get("phone", "")
        client_db["person_type"]= client_db.get("person_type", "")

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    except Exception as e:
        print(f"❌ ERROR DE VALIDACIÓN: {e}")
        raise HTTPException(status_code=500, detail=f"Error en datos: {str(e)}")