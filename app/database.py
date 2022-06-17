from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import time
import psycopg2 as pg
from psycopg2.extras import RealDictCursor
from .config import settings

#SQLALCHEMY_DATABSE_URL = 'postgresql://<username>:<password>@<ip-addresss/hostname>/<database_name>'
#SQLALCHEMY_DATABSE_URL = 'postgresql://postgres:gamboa12@localhost/fastapi'
SQLALCHEMY_DATABSE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Connects to postgres database
#while True:
#    try:
#        conn = pg.connect(host='localhost',database='fastapi',user='postgres',password='gamboa12',cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print('Successful Database Connection!')
#        break
#    except Exception as error:
#        print('Database connection ERROR\n',f'Error: {error}')
#        time.sleep(2)
