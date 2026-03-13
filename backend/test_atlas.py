import os
from dotenv import load_dotenv
from pymongo import MongoClient

# 1. Intentamos cargar el .env
load_dotenv()

# 2. Imprimimos para depurar (esto te ayudará a ver qué pasa)
print(f"Directorio actual: {os.getcwd()}")
print(f"¿Existe el archivo .env?: {os.path.exists('.env')}")

uri = os.getenv("MONGO_URI")

if not uri:
    print("❌ Error: No se encontró MONGO_URI. Verifica que el archivo .env esté en la carpeta 'backend'.")
else:
    try:
        client = MongoClient(uri)
        client.admin.command('ping')
        print("✅ ¡CONEXIÓN EXITOSA! Python ya lee tu .env y conecta a Atlas.")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")