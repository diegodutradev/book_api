from fastapi import FastAPI
from routers import users, books
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)
