import os
from motor.motor_asyncio import AsyncIOMotorClient # <--- CAMBIO CLAVE: Usamos Motor
from dotenv import load_dotenv

load_dotenv()

# Aquí seguimos usando tu MONGO_URI de Atlas que tienes en el .env
uri = os.getenv("MONGO_URI") 

try:
    # Creamos el cliente asíncrono compatible con 'await'
    client = AsyncIOMotorClient(uri)
    
    # Asegúrate de que este nombre sea el de la base de datos en Atlas
    db = client.kofan_hospedaje_db 
    
    print("✅ ¡Conexión asíncrona preparada para MongoDB Atlas!")
except Exception as e:
    print(f"❌ Error al configurar la conexión: {e}")