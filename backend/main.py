from fastapi import FastAPI
from routers import auth, users, products
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.mount("/static", StaticFiles(directory="static"), name="static")