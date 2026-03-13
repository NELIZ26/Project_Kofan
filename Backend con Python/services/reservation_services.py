from db.client import db
from schemas.reservation_schema import reservation_schema, reservations_schema

collection = db.reservas

def get_reservations_by_user(user_id: str, check_in: str = None, check_out: str = None):
    query = {"user_id": user_id}
    
    # cuando el usuario en Vue usa los filtros de fecha,aqui es donde mongo los procesa 
    if check_in or check_out:
        date_query = {}
        if check_in: date_query["$gte"] = check_in
        if check_out: date_query["$lte"] = check_out
        query["check_in"] = date_query

    reservas = list(collection.find(query))
    return reservations_schema(reservas)

def create_reservation(reservation_data: dict):
    id = collection.insert_one(reservation_data).inserted_id
    return reservation_schema(collection.find_one({"_id": id}))

def bulk_delete_reservations(user_id: str, fecha_inicio: str, fecha_fin: str):
    try:
        query = {
            "user_id": user_id,
            "fecha_reserva": {
                "$gte": fecha_inicio,
                "$lte": fecha_fin
            }
        }
        
        result = db.reservas.delete_many(query)
        return result.deleted_count # Retorna cuántas se borraron
    except Exception as e:
        print(f"Error en el servicio de borrado: {e}")
        return None
    
async def get_reservation_stats(user_id: str):
    try:
        # Contamos cada estado de forma independiente
        aceptadas = db.reservas.count_documents({"user_id": user_id, "estado": "ACEPTADA"})
        pendientes = db.reservas.count_documents({"user_id": user_id, "estado": "PENDIENTE"})
        canceladas = db.reservas.count_documents({"user_id": user_id, "estado": "CANCELADA"})
        total = db.reservas.count_documents({"user_id": user_id})

        return {
            "total": total,
            "aceptadas": aceptadas,
            "pendientes": pendientes,
            "canceladas": canceladas
        }
    except Exception as e:
        print(f"Error al obtener estadísticas: {e}")
        return None