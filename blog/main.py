from fastapi import FastAPI
from typing import List
from database import engine,get_db
from routers import blog,user,login
import models

app =FastAPI()


models.base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)


# @app.get('/blogs')
# # to run this http://127.0.0.1:8000/blogs?limit=50&published=true
# def index(limit,published:bool=True,sort : Optional[str]=None):
#     if published:
#         return {'data':f'{limit} published blogs from db'}
#     return {'data':f'{limit} all blogs from db'}

# @app.get('/blogs/unpublished')
# def unpublished():
#     return {'data':"all unpublished bloogs"}

# '''
# hint move all the dynamic routing below the static writings 
# that is like these /about/{id} if both blogs and about are same
# '''

# @app.get('/about/{id}') 
# # {id} is for query parameters 
# # id:int it accepts only interger if string is given then it display the error
# # by defasult the (id) received is string
# def show(id:int):
#     return {'data':id}

# @app.get('/about/{id}/comments') 
# # {id} is for query parameters 
# def show(id:int):
#     return {'data':[1,2]}
