from database import engine, get_db
import orm_models


orm_models.Base.metadata.create_all(bind=engine)