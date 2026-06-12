from fastapi import FastAPI
from SQL_Assessment_Team.sqlalchemy.database import engine, get_db
import SQL_Assessment_Team.sqlalchemy.orm_models as orm_models

from router import router

app = FastAPI()

# Include all routes
app.include_router(router)

orm_models.Base.metadata.create_all(bind=engine)