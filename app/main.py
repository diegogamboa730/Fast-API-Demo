from . import models
from fastapi import FastAPI
from .database import engine 
from .routers import post, user, auth, vote, employer
from .config import settings

#This library will allow the api to talk to other domains
from fastapi.middleware.cors import CORSMiddleware

#This creates tables and now that alembic is 
#Implemented the code below isn't needed.
#models.Base.metadata.create_all(bind=engine)


app = FastAPI()

#List of Origins(URLS THAT CAN TALK TO MY API)
#IF I WANT IT TO BE PUBLIC THEN -> origins = ["*"]
#If api will power an application only applicatio 
#domiain should be used in the origins.
origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello,": "World"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(employer.router)
