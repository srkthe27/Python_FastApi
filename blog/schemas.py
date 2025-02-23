from pydantic import BaseModel,EmailStr
from typing import Optional

class Blog1(BaseModel):
    title : str
    body : str  
    published : Optional[bool]=True

# By declaring this we can hide the ID while diplaying the data 
# on only the decorator whic is mentioned as response_model=
            
class Showblog(Blog1):
    class Config():
        from_attributes = True 

            # OR
# We can display only the fields that are required
# class Showblog(BaseModel):
#     title: str
#     class config():
#         from_attributes = True

class User1(BaseModel):
    userName:str
    email:EmailStr
    password:str

class ShowUser(BaseModel):
    userName:str
    email:EmailStr
    class Config:
        from_attributes = True

class Login(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:str | None = None