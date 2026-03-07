from backend.db.client import db
from bson import ObjectId
from backend.schemas.booking_schema import ReservaCreate
from datetime import datetime
from fastapi import HTTPException, status # Asegúrate de tener estas importaciones


async def create_booking_service(reserva: ReservaCreate, user_id: str):
    # 1. BUSCAR LA HABITACIÓN PRIMERO
    # Convertimos a ObjectId aquí para asegurar la búsqueda
    habitacion_obj_id = ObjectId(reserva.habitacion_id)
    habitacion = await db.rooms.find_one({"_id": habitacion_obj_id})

    
    # 2. VALIDACIÓN DE EXISTENCIA Y DISPONIBILIDAD
    if not habitacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La habitación no existe."
        )
    
    if not habitacion.get("is_available", True):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Lo sentimos, esta habitación ya se encuentra ocupada o reservada."
        )

    # 3. PREPARAR EL DICCIONARIO
    reserva_dict = reserva.model_dump()

    # Asegurar estado por defecto
    if not reserva_dict.get("estado"):
        reserva_dict["estado"] = "pendiente"
    
    # Conversiones de fecha para MongoDB
    reserva_dict["fecha_entrada"] = datetime.combine(reserva.fecha_entrada, datetime.min.time())
    reserva_dict["fecha_salida"] = datetime.combine(reserva.fecha_salida, datetime.min.time())
    
  
    # Si user_id viene del token como string, DEBE ser ObjectId en la DB.
    reserva_dict["cliente_id"] = ObjectId(user_id) 
    reserva_dict["habitacion_id"] = habitacion_obj_id

    # 4. GUARDAR RESERVA
    result = await db.bookings.insert_one(reserva_dict)
    
    # 5. MARCAR HABITACIÓN COMO OCUPADA
    await db.rooms.update_one(
        {"_id": habitacion_obj_id},
        {"$set": {"is_available": False}}
    )

    return str(result.inserted_id)


async def update_booking_status_service(reserva_id: str, nuevo_estado: str):
    # Actualizar el estado de la reserva
    result = await db.bookings.update_one(
        {"_id": ObjectId(reserva_id)},
        {"$set": {"estado": nuevo_estado}}
    )
    
    # LÓGICA DE NEGOCIO: Si se cancela o finaliza, la habitación queda libre
    if nuevo_estado in ["cancelada", "finalizada"]:
        reserva = await db.bookings.find_one({"_id": ObjectId(reserva_id)})
        if reserva:
            db.rooms.update_one(
                {"_id": ObjectId(reserva["habitacion_id"])},
                {"$set": {"is_available": True}} # Volvemos a poner True
            )
            
    return result.modified_count > 0


async def get_user_bookings_service(user_id: str):
    # 1. Buscamos todas las reservas del usuario
    cursor = db.bookings.find({"cliente_id": ObjectId(user_id)})
    
    mis_reservas = []

    # USAMOS UN SOLO BUCLE. Una vez que este bucle termina, el cursor se agota.
    async for reserva in cursor:
        # A. BUSCAMOS LOS DATOS DE LA HABITACIÓN (El "Join" manual)
        habitacion = await db.rooms.find_one({"_id": reserva["habitacion_id"]})
        
        # B. Preparamos el nombre legible (esto lo tenías bien, pero hay que usarlo abajo)
        info_habitacion = f"Hab. {habitacion['numero_unidad']} - {habitacion['tipo']}" if habitacion else "Habitación no encontrada"
    
        # C. CONVERSIÓN MANUAL Y LLENADO DE LA LISTA
        mis_reservas.append({
            "id": str(reserva["_id"]),
            "habitacion": info_habitacion, # <-- Agregamos el nombre legible aquí
            "habitacion_id": str(reserva["habitacion_id"]),
            "fecha_entrada": reserva["fecha_entrada"].strftime("%Y-%m-%d"),
            "fecha_salida": reserva["fecha_salida"].strftime("%Y-%m-%d"),
            "monto_total": reserva["monto_total"],
            "estado": reserva.get("estado", "pendiente"),
            "observaciones": reserva.get("observaciones", "")
        })
    
    return mis_reservas



async def get_all_bookings_service(estado_filtro: str = None):
    # 1. Filtro base
    query = {}
    if estado_filtro:
        query["estado"] = estado_filtro

    # 2. Obtener las reservas
    cursor = db.bookings.find(query).sort("fecha_entrada", -1)
    
    lista_global = []
    # Contadores para el resumen
    conteo_pendientes = 0

    async for reserva in cursor:
        habitacion = await db.rooms.find_one({"_id": reserva["habitacion_id"]})
        cliente = await db.users.find_one({"_id": reserva["cliente_id"]})
        
        estado = reserva.get("estado", "pendiente")
        if estado == "pendiente":
            conteo_pendientes += 1

        lista_global.append({
            "id": str(reserva["_id"]),
            "cliente": cliente["full_name"] if cliente else "N/A",
            "habitacion": f"Hab. {habitacion['numero_unidad']}" if habitacion else "N/A",
            "monto": reserva["monto_total"],
            "estado": estado
        })

    # 3. LÓGICA EXTRA: Contar cuántas habitaciones físicas están ocupadas hoy
    # Esto es independiente de las reservas filtradas
    habitaciones_ocupadas = await db.rooms.count_documents({"is_available": False})
    total_habitaciones = await db.rooms.count_documents({})

    # 4. Devolvemos el "Súper Objeto"
    return {
        "resumen": {
            "total_encontradas": len(lista_global),
            "pendientes_por_aprobar": conteo_pendientes,
            "ocupacion_actual": f"{habitaciones_ocupadas}/{total_habitaciones}",
            "porcentaje_ocupacion": f"{(habitaciones_ocupadas/total_habitaciones)*100:.1f}%" if total_habitaciones > 0 else "0%"
        },
        "reservas": lista_global
    }