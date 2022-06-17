from fastapi import FastAPI,Response,status,HTTPException
from typing import Union
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2 as pg
from psycopg2.extras import RealDictCursor 
import time

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

def find_post(id):
    pass
#    for p in my_posts:
#        if(p['id'] == id):
#             return p
#        else:
#            pass
#    cursor.execute("""SELECT * from posts where id = %
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if(p['id'] == id):
            return i

@app.get("/posts/{id}")
def get_post(id: int,response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""",(id))
    post = cursor.fetchone()
    print(post)
    #post = find_post(id)
    if not post:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message":f"Post with id {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return {"post_detail":post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    #post_dict = post.dict()
    #post_dict['id'] = randrange(0,1000000)
    #my_posts.append(post_dict)
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,
                  (post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {'data':new_post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist.")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist.")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data":post_dict}

