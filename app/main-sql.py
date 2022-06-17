from fastapi import FastAPI,Response,status,HTTPException
from typing import Union
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2 as pg
from psycopg2.extras import RealDictCursor 
import time

from . import models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

#dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

app = FastAPI()

my_posts = [{"title":"Post 1 Title","content":"Post 1 Content","id":1},
            {"title":"Post 2 Title","content":"Post 2 Content","id":2}]

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True
    
while True:
    try: 
        conn = pg.connect(host='localhost',database='fastapi',user='postgres',password='gamboa12',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Successful Database Connection!')
        break
    except Exception as error:
        print('Database connection ERROR\n',f'Error: {error}')
        time.sleep(2)

@app.get("/")
def read_root():
    return {"Hello,": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * from posts""")
    posts = cursor.fetchall()
    return {'data':posts}

@app.get("/posts/{id}")
def get_post(id: int,response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return {"post_detail":post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,
                  (post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {'data':new_post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""",
                  (post.title,post.content,post.published,(str(id))))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist.")
    return {"data":updated_post}

