from pymongo import MongoClient

SECRET = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 
REFRESH_TOKEN_EXPIRE_DAYS = 7

UPLOAD_DIR = "static/images"
ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp"]

# --- CONFIGURACIÓN DE MONGODB ---
# Si tu MongoDB es local, usa esta URL:
MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

# Aquí definimos 'db'. Cámbialo por el nombre que quieras para tu base de datos
db = client["mi_base_de_datos_python"]