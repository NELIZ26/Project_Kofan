from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.config import SECRET, ALGORITHM
from services.user_service import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise exception
    except JWTError:
        raise exception

    # CORRECCIÓN: Debe llevar AWAIT porque el servicio es async
    user = await get_user_by_email(email) 

    if user is None:
        raise exception
    return user

async def require_admin(user=Depends(get_current_user)):
    # OJO: Verifica si en tu modelo es 'role' o 'rol_id'
    # Si usaste mi sugerencia del schema anterior, el campo es 'rol_id'
    if getattr(user, "rol_id", None) != "admin" and getattr(user, "rol_Id", None) != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Requiere privilegios de administrador"
        )

    return user