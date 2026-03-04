import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Esto carga las variables del archivo .env
load_dotenv()

# Sacamos la URL del .env
MONGO_URL = os.getenv("MONGO_URI")

# Conectamos
cliente = MongoClient(MONGO_URL)

# El instructor usa "fastapi_db", puedes mantenerlo o cambiarlo a "hotel_kofan"
db = cliente["fastapi_db"]