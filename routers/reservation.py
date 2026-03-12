from fastapi import APIRouter, Depends, HTTPException, Request
from db.client import db 
from services.reservation_services import get_reservation_stats
#from dependencies.auth import oauth2_scheme # Importo el esquema directamente
from core.config import SECRET, ALGORITHM 
from jose import jwt
from bson import ObjectId

router = APIRouter(
    prefix="/reservations",
    tags=["reservations"]
)


@router.get("/history")
async def get_reservation_history(
    request: Request,
    entry_date: str = None, # Parámetro opcional del calendario 1
    exit_date: str = None     # Parámetro opcional del calendario 2
):
    try:
        # 1. IdentificO el usuario (Nelson)
        auth_header = request.headers.get("Authorization")
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])

        user_db = await db.clients.find_one({"email": payload.get("sub")})
        if not user_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        user_id = str(user_db["_id"])


        # 2. Construyo la Query dinámica
        query = {"client_id": user_id}
        
        if entry_date and exit_date:
            query["entry_date"] = {"$gte": entry_date}
            query["exit_date"] = {"$lte": exit_date}

        reservas_cursor = db.bookings.find(query)
        reservas = []
        
        async for res in reservas_cursor:
            res["_id"] = str(res["_id"])
            reservas.append(res)

        return {"status": "success", "results": reservas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el historial :{str(e)}")


@router.delete("/limpiar")
async def delete_filtered_reservations(request: Request):
    try:
        # 1. Obtengo las fechas del JSON enviado por el botón filtrar (boton naranja)
        data = await request.json()
        fecha_inicio = data.get("entry_date")
        fecha_fin = data.get("exit_date")
        
        # 2. Identifico al cliente Nelson de forma manual  
        auth_header = request.headers.get("Authorization")
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        
        user_db =await  db.clients.find_one({"email": payload.get("sub")})
        if not user_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        user_id_str = str(user_db["_id"])

        # 3. Borro directamente en MongoDB para evitar confusiones de archivos
        query = {
            "client_id": user_id_str,
            "entry_date": {"$gte": fecha_inicio},
            "exit_date": {"$lte": fecha_fin}
        }
        
        result = await db.bookings.delete_many(query)
        if result.deleted_count == 0:
             return {
                "status": "success",
                "message": "No se encontraron reservas en ese rango para eliminar.",
                "count": 0
            }

        return {
            "status": "success",
            "message": f"Se eliminaron {result.deleted_count} reservas de tu historial.",
            "count": result.deleted_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al borrar: {str(e)}")
    

@router.get("/stats")
async def get_my_reservation_stats(request: Request):
    try:
        # 1. Identifico al usuario manualmente por el token 
        auth_header = request.headers.get("Authorization")
        if not auth_header: 
            raise HTTPException(status_code=401, detail="No autorizado")

        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        
        user_db = await db.clients.find_one({"email": payload.get("sub")})
        if not user_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        user_id_str = str(user_db["_id"])

        confirmadas = await db.bookings.count_documents({
            "client_id": user_id_str,
            "state": "confirmada"
        })
        pendientes = await db.bookings.count_documents({
            "client_id": user_id_str, 
            "state": "pendiente"
        })
        
        canceladas = await db.bookings.count_documents({
            "client_id": user_id_str, 
            "state": "cancelada"
        })
        return {
            "status": "success",
            "data": {
                "confirmadas": confirmadas,
                "pendientes": pendientes,
                "canceladas": canceladas,
                "total": confirmadas + pendientes + canceladas
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en estadísticas: {str(e)}")