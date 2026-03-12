from fastapi import APIRouter, Depends, HTTPException, status
from backend.dependencies.auth import required_admin
from backend.services.user_service import delete_user_service, update_user_service, get_all_users_service
from backend.schemas.user_schema import AdminUserUpdate

router = APIRouter(
    prefix="/admin", 
    tags=["Módulo Administrativo"],
    dependencies=[Depends(required_admin)]
)

# 1. BIENVENIDA
@router.get("/dashboard")
async def admin_dashboard():
    return {"message": "Bienvenido al Panel de Control de Kofán Hospedaje"}

# LISTAR_USUARIOS
@router.get("/users")
async def list_users():
    users = await get_all_users_service()
    return users

# ACTUALIZAR_USUARIO
@router.patch("/users/{user_id}")
async def admin_update_user(user_id: str, data: AdminUserUpdate):
    update_dict = data.model_dump(exclude_unset=True)
    
    if not update_dict:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")

    user_updated = await update_user_service(user_id, update_dict)
    
    if not user_updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    user_updated["_id"] = str(user_updated["_id"])
    return {"message": "Usuario actualizado por el Administrador", "user": user_updated}



# ELIMINAR USUARIO
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, current_admin = Depends(required_admin)):
   
    if user_id == str(current_admin["_id"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No puedes eliminar tu propia cuenta de administrador."
        )

    deleted = await delete_user_service(user_id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado"
        )
    
    return None

#ACONTINUACION - se presenta una variacion a la eliminacion de usuarios, en vez de eliminarlos se desactivan, esto con el fin de no perder su historial de reservas, por ejemplo, y poder reactivarlos en caso de ser necesario. Esto aun no esta implementado en el router, pero es para tenerlo en cuenta para futuras mejoras.---------------------------------

# Dentro de la ruta de login
#user = await get_user_by_email(form_data.username)

#if not user:
    #raise HTTPException(status_code=401, detail="Correo no encontrado")

# 🚨 VERIFICACIÓN DE ESTADO:
# Usamos .get(..., True) por si algún usuario viejo aún no tiene el campo
#if user.get("is_active", True) is False:
    #raise HTTPException(
     #   status_code=status.HTTP_403_FORBIDDEN,
      #  detail="Tu cuenta ha sido desactivada. Comunícate con el administrador de Kofán Hospedaje."
   # )

# ... luego sigues con la verificación de la contraseña ...