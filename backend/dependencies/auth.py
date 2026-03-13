from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.config import SECRET, ALGORITHM
from services.user_service import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        email = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if email is None:
            raise exception
    except JWTError:
        raise exception

    user = get_user_by_email(email)

    if user is None:
        raise exception

    return user


def require_admin(user=Depends(get_current_user)):

    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Requiere privilegios de administrador"
        )

    return user