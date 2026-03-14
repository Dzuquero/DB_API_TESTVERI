
from fastapi import FastAPI
from app.api.v1 import auth, actions

app = FastAPI(title="User's Activity API")

app.include_router(auth.router)
app.include_router(actions.router)
