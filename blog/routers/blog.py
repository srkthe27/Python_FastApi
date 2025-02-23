from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from models import Blog
from schemas import Blog1,Showblog,TokenData
from database import get_db
from .oauth2 import get_current_user

#prefix is used to add the prefix to the router like /blog
#tags for diffrentiating the routers like for blogs and users etc
#check the name in swagger UI
router = APIRouter(
    tags=['Blog']
)

# storing blogs in db
@router.post('/blog/',status_code=201)
def create_blog(blog:Blog1,db=Depends(get_db),get_current_user: TokenData = Depends(get_current_user)):
    
    new_blog = Blog(
        title=blog.title,
        body=blog.body,
        email=get_current_user.email
    )
    try:
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog.title
    except Exception as e:
        db.rollback()
        return {'Detail':f"An exception {e} occured"}


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
# Remove the specific blog from the db
def remove(id,db=Depends(get_db),get_current_user: TokenData = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id ==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} is not found")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/blog/{id}/',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:Blog1,db=Depends(get_db),get_current_user: TokenData = Depends(get_current_user)):
    qur = db.query(Blog).filter(Blog.id == id)
    if not qur.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with {id} is not found")
    qur.update(request)
    db.commit()
    return "Updated"

# # get all blog from the database
@router.get('/get_blogs/',response_model=List[Showblog],status_code=status.HTTP_200_OK)
def get_blogs(db=Depends(get_db),get_current_user: TokenData = Depends(get_current_user)):
    blogs = db.query(Blog).all()
    return blogs

# get specific blog from the DB using query parameter
# Custom status code based on the program flow
@router.get('/get_blog/{id}',response_model=Showblog,status_code=200)
def get_single_blog(id,response:Response,db=Depends(get_db),get_current_user: TokenData = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the id {id} is not found"}
        # OR
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not found")
    return blog
