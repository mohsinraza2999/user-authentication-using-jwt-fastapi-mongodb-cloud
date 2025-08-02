from fastapi import FastAPI
from api import routes_auth, routes_user

app = FastAPI(title="FastAPI Auth App")

app.include_router(routes_auth.router, prefix="/auth", tags=["auth"])
app.include_router(routes_user.router, prefix="/users", tags=["users"])