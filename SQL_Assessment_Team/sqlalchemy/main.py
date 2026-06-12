from fastapi import FastAPI
from database import engine, get_db
import orm_models

from router import router

app = FastAPI()

app.include_router(router)

orm_models.Base.metadata.create_all(bind=engine)