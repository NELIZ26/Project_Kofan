from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

print(os.listdir())
load_dotenv()

uri = os.getenv("MONGO_URI")
print("URI:", uri)

try:
    client = AsyncIOMotorClient(uri)
    
    # Base de datos
    db = client["kofan_hospedaje_db"]
    
    print("✅ Cliente MongoDB creado correctamente")

except Exception as e:
    print(f"❌ Error al configurar la conexión: {e}")


# 🔎 función para probar conexión real
async def ping_mongodb():
    try:
        await client.admin.command("ping")
        print("✅ Conexión REAL con MongoDB Atlas exitosa")
    except Exception as e:
        print("❌ Error conectando a MongoDB:", e)