from fastapi import APIRouter
from backend.schemas.booking_schema import ReservaPublicCreate
from backend.services.booking_service import create_booking_service

router = APIRouter(
    prefix="/reservar-publico", 
    tags=["Reservas Públicas (Sin Autenticación)"]
)

@router.post("/")
async def registrar_reserva_publica(reserva: ReservaPublicCreate):
   
    nueva_reserva_id = await create_booking_service(reserva, user_id=None)
    
    return {
        "message": "¡Reserva recibida con éxito! Pronto nos comunicaremos contigo para confirmar el pago.",
        "reserva_id": nueva_reserva_id,
        "cliente": reserva.cliente_nombre
    }

