from fastapi import FastAPI
from routers import auth, users, reservation
from fastapi.staticfiles import StaticFiles
from db.client import ping_mongodb

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(reservation.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.on_event("startup")
async def startup_event():
    await ping_mongodb()