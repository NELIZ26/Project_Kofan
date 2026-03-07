from fastapi import FastAPI
from backend.routers import admin, auth, earnings, register, users, bookings, rooms, bookings_sin_auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(bookings.router)
app.include_router(register.router)
app.include_router(earnings.router)
app.include_router(rooms.router)
app.include_router(bookings_sin_auth.router)
app.include_router(admin.router)