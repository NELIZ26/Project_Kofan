from fastapi import APIRouter, Depends, HTTPException, status
from backend.dependencies.auth import required_admin, get_current_user
from backend.schemas.user_schema import UserUpdate
from backend.schemas.booking_schema import ReservaCreate
from backend.services.booking_service import create_booking_service
from backend.services.user_service import update_user_service, delete_user_service


router = APIRouter(
    prefix="/users", 
    tags=["users"], 
)

@router.get("/me")
async def read_me(user=Depends(get_current_user)):  # Dependencia que extrae el usuario actual del token
    user["_id"] = str(user["_id"])
    return user


@router.patch("/update-me")
async def update_me(data: UserUpdate, current_user = Depends(get_current_user)):
    update_dict = data.model_dump(exclude_unset=True)
    
    if not update_dict:
        raise HTTPException(status_code=400, detail="No enviaste datos para actualizar")

    user_id = str(current_user["_id"])
    user_updated = await update_user_service(user_id, update_dict)
    
    if not user_updated:
        raise HTTPException(status_code=404, detail="No se pudo actualizar el usuario")

    user_updated["_id"] = str(user_updated["_id"])
    user_updated.pop("password", None)
    
    return {"message": "¡Perfil actualizado con éxito!", "user": user_updated}


# 3. ELIMINAR MI PERFIL?
@router.patch("/delete-me") # Cambiamos a PATCH porque estamos actualizando un estado
async def delete_me(current_user = Depends(get_current_user)):
    user_id = str(current_user["_id"])
    
    # 1. ¿Tiene reservas activas? (Opcional: evitar que se borre si tiene viajes pendientes)
    # reservas_activas = await check_active_bookings(user_id)
    
    success = await deactivate_user_service(user_id)
    
    if not success:
        raise HTTPException(status_code=400, detail="No se pudo desactivar la cuenta")
    
    return {"message": "Cuenta desactivada correctamente. ¡Esperamos verte pronto!"}