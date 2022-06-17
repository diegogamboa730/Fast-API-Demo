#LIBRARIES
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models,schemas,utils
from ..database import get_db

router = APIRouter(
    prefix = "/employers",
    tags = ["Employers"]
)

@router.get("/",response_model=List[schemas.EmployerOut])
def get_employers(db: Session = Depends(get_db)):
    users = db.query(models.Employer).all()
    return users

#@router.get("/{id}",response_model=schemas.UserOut)
#def get_user(id: int, db: Session = Depends(get_db)):
#    user = db.query(models.User).filter(models.User.id == id).first()
#    if not user:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} not found!")
#    return user

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.EmployerOut)
def create_employer(employer: schemas.Employer, db: Session = Depends(get_db)):
#    #cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,
    #              (post.title,post.content,post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    #print(post)

    #Hash the Password - user.password
    #hashed_password = utils.hash(user.password)
   #user.password = hashed_password
    new_employer = models.Employer(**employer.dict())
    db.add(new_employer)
    db.commit()
    db.refresh(new_employer)
    return new_employer
#    new_user = models.User(**user.dict())
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user) #will return the new object == RETURNING *
#    return new_user

#@router.delete("/{id}")
#def delete_user(id: int, db: Session = Depends(get_db)):
#    deleted_user = db.query(models.User).filter(models.User.id == id)
#    if deleted_user.first() == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist.")
#    deleted_user.delete(synchronize_session=False)
#    db.commit()
#    return Response(status_code=status.HTTP_204_NO_CONTENT)

#@router.put("/{id}",response_model=schemas.UserOut)
#def update_user(id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
#    user_query = db.query(models.User).filter(models.User.id == id)
#    if user_query.first() == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist.")
#    user_query.update(updated_user.dict(),synchronize_session=False)
#    db.commit()
#    return user_query.first()

