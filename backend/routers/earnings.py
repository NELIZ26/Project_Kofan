from fastapi import APIRouter, Depends
from backend.dependencies.auth import required_admin  # Tu guardia VIP

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/earnings")
async def get_financial_reports(user = Depends(required_admin)):
    # Si el código llega aquí, es porque el usuario ES admin
    return {"mensaje": f"Bienvenido {user['username']}, aquí están las cuentas..."}