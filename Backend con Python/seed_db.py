from pymongo import MongoClient
from core.security import hash_password 

# 1. Conexión Síncrona
# Asegúrate de que "fastapi_db" sea el nombre exacto de tu base de datos en MongoDB Compass
client = MongoClient("mongodb://localhost:27017/")
db = client.fastapi_db 

def seed():
    try:
        print("--- Iniciando proceso de población de datos ---")
        
        # 2. Limpiar datos existentes para evitar duplicados
        db.users.delete_many({})
        db.reservas.delete_many({})
        print("Configuración limpia: Colecciones 'users' y 'reservas' vaciadas.")

        # 3. Preparar datos del Usuario (Nelson)
        # Incluimos todos los campos para evitar que el JSON retorne 'null' en el GET inicial
        user_data = {
            "names": "Nelson",
            "surnames": "Contreras",
            "email": "nelson@example.com",
            "password": hash_password("12345"), # Genera el hash seguro
            "role": "user",
            "disabled": False,
            "tipo_persona": "Natural",  # Al ser Natural, no incluimos 'nombre_empresa'
            "document_type": "CC",      
            "document_number": "0000000000",
            "telefono": "0000000",
            "direccion": "Calle Falsa 123"
        }
        
        # Insertar usuario y recuperar el ID generado por MongoDB
        result = db.users.insert_one(user_data)
        user_id = result.inserted_id
        print(f"✅ Usuario 'Nelson' creado. ID: {user_id}")

        # 4. Crear Reservas vinculadas al ID del usuario creado
        reservas_data = [
            {
                "user_id": str(user_id),
                "descripcion": "Cabaña 2 personas",
                "fecha_reserva": "2025-01-08",
                "check_in": "2026-02-18",
                "check_out": "2026-02-20",
                "estado": "ACEPTADA"
            },
            {
                "user_id": str(user_id),
                "descripcion": "Cabaña 2 personas",
                "fecha_reserva": "2025-01-08",
                "check_in": "2025-08-20",
                "check_out": "2025-08-25",
                "estado": "PENDIENTE"
            }
        ]
        
        db.reservas.insert_many(reservas_data)
        print(f"✅ {len(reservas_data)} reservas insertadas correctamente.")
        
        print("--- Proceso finalizado con éxito ---")

    except Exception as e:
        print(f"❌ ERROR durante el seeding: {e}")

if __name__ == "__main__":
    seed()