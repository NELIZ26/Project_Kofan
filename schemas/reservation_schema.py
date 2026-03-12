from bson import ObjectId

def reservation_schema(reserva) -> dict:
    return{
        "id": str(reserva["_id"]),
        "users_id": str(reserva["users_id"]),
        "descripcion": reserva.get("detalle"),
        "fecha_reserva": reserva.get("fecha_reserva"),
        "check_in": reserva.get("check_in"),
        "check_out": reserva.get("check_out"),
        "estado": reserva.get("estado", "PENDIENTE"),

    }

def reservations_schema(reservas) -> list:
    return [reservation_schema(res) for res in reservas]