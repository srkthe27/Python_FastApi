from schemas import Login
from fastapi import APIRouter,Depends,HTTPException,status,Response
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from models import User
from .user import verify_password
from .token import create_access_token

router = APIRouter(
    tags=['Authentication']
)

@router.post('/signIn/')
def login(response:Response,request:OAuth2PasswordRequestForm = Depends(),db = Depends(get_db)):
    email = request.username
    password = request.password
    try:

        user = db.query(User).filter(User.email == email).first()
        print(user)
        
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"User with {email} is not found")
        
        hashed_password = user.password
        if(verify_password(password,hashed_password)):
            access_token = create_access_token({"sub": user.email})

            return {"access_token": access_token, "token_type": "bearer"}
        else:
            return {"Detail":"Invalid Credentials","code":status.HTTP_401_UNAUTHORIZED}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")