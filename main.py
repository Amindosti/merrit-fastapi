from fastapi import FastAPI
from router import user, authenticate, newform, dataentry
from database import engine
from fastapi.middleware.cors import CORSMiddleware
import models

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(authenticate.router)
app.include_router(newform.router)
app.include_router(dataentry.router)
