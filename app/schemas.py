from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

## Models for Users ##
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

## Models for Posts ##
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
# Model which inherits PostBase
class PostCreate(PostBase):
    pass

class Post(PostBase):
    #... all other fields are inherited
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    #Addign this subclass model is able to
    #read non dictionary responses.
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

## Models for Token ##
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

## Models for Votes ##
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

## Models for employers ##
class Employer(BaseModel):
    name: str #= Column(String, nullable=False)
    employee_count: int #= Column(Integer, nullable=False, server_default=0)
    bed_count: int #= Column(Integer, nullable=False, server_default=0)
    cell_phone: str #= Column(String, nullable=True)
    address: str#= Column(String,

class EmployerOut(BaseModel):
    id: int #Column(Integer, primary_key=True, nullable=False)
    name: str #= Column(String, nullable=False)
    employee_count: int #= Column(Integer, nullable=False, server_default=0)
    bed_count: int #= Column(Integer, nullable=False, server_default=0)
    cell_phone: str #= Column(String, nullable=True)
    address: str#= Column(String,
    class Config:
        orm_mode = True



