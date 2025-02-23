from passlib.context import CryptContext
from fastapi import Depends,APIRouter,HTTPException,Response,status
from database import get_db
from schemas import User1,ShowUser
from models import User

#prefix is used to add the prefix to the router like /user
#tags for diffrentiating the routers like for blogs and users etc
#check the name in swagger UI
router = APIRouter(
    tags=['User']
)
PWD_CONTEX = CryptContext(schemes=["bcrypt"],deprecated="auto")

def verify_password(password,hashed_password):
    return PWD_CONTEX.verify(password,hashed_password)

def hash_password(password):
    return PWD_CONTEX.hash(password)

@router.post('/signUp/',response_model = ShowUser | None)
def create_user(request:User1,db=Depends(get_db)):
    # Hashing password
    hashed_password = hash_password(request.password)
    
    new_user = User(
        name=request.userName,
        email=request.email,
        password=hashed_password
    )

    query = db.query(User).filter(User.email == request.email).first()

    if not new_user.name or not new_user.email or not new_user.password:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,detail="Few fields are missing")
    
    elif query:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already exists")

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return ShowUser(
        userName=request.userName,
        email=request.email
    )
    
    except Exception as e:
        db.rollback()
        return {'Detail':f"An exception {e} occured"}
    
