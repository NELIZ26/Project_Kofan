from typing import Optional

from fastapi import APIRouter, Depends
from backend.dependencies.auth import get_current_user, required_admin
from backend.schemas.booking_schema import ReservaCreate
from backend.services.booking_service import create_booking_service, get_all_bookings_service, get_user_bookings_service, update_booking_status_service
from fastapi import HTTPException, status
from enum import Enum
router = APIRouter(
    prefix="/reservar", 
    tags=["reservar"]
)

# PARA CREAR UNA RESERVA, SOLO USUARIOS AUTENTICADOS
@router.post("/")
async def registrar_reserva(reserva: ReservaCreate, user = Depends(get_current_user)):
    # Extraemos el ID del usuario directamente del token (el objeto 'user' que devuelve MongoDB)
    user_id_from_token = str(user["_id"])
    
    nueva_reserva_id = await create_booking_service(reserva, user_id_from_token)
    
    return {
        "message": "Reserva creada exitosamente",
        "reserva_id": nueva_reserva_id,
        "usuario_que_reservo": user["email"] # Opcional: para confirmar en la respuesta
    }

# SOLO ADMIN PUEDE CAMBIAR EL ESTADO DE UNA RESERVA
@router.patch("/{reserva_id}/estado")
async def cambiar_estado_reserva(
    reserva_id: str, 
    nuevo_estado: str, 
    admin_user = Depends(required_admin) 
):
    exito = await update_booking_status_service(reserva_id, nuevo_estado)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
        
    return {
        "message": "Estado actualizado",
        "admin_que_autorizo": admin_user["email"]
    }


@router.get("/mis-reservas")
async def listar_mis_reservas(user = Depends(get_current_user)):
    # 1. Extraemos el ID del usuario del token
    user_id = str(user["_id"])
    
    # 2. Llamamos al servicio para buscar sus reservas
    reservas = await get_user_bookings_service(user_id)
    
    return {
        "usuario": user["email"],
        "total_reservas": len(reservas),
        "reservas": reservas
    }


# 1. Definimos los estados oficiales del hotel
class EstadoReserva(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"

# 2. En el Router, usamos ese Enum
@router.get("/admin/all-bookings")
async def get_all_bookings(
    # Ahora FastAPI solo aceptará uno de los 4 estados de arriba
    estado: Optional[EstadoReserva] = None, 
    admin_user = Depends(required_admin)
):
    return await get_all_bookings_service(estado_filtro=estado)