from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer   
from jose import JWTError, jwt
from backend.core.config import SECRET, ALGORITHM
from backend.services.user_service import get_user_by_email, get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):  #dependencia que extrae el token del header Authorization
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user_by_id(user_id)  # Aquí asumimos que el "sub" es el ID del usuario, no el email
    if user is None:
        raise credentials_exception
    return user

async def required_admin(user = Depends(get_current_user)):
    if user ["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acceso no autorizado")
    return user
