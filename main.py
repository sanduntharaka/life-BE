from fastapi import FastAPI
from api.v1 import users

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
