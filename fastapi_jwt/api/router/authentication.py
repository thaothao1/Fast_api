from fastapi import APIRouter, Depends , status , HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import schemas,database, test , token
from models.hashing import Hash
from sqlalchemy.orm import Session

router= APIRouter()

@router.post('/login')
# def login(request:OAuth2PasswordRequestForm = Depends(), db: Session= Depends(database.get_db)):
#     user = db.query(test.User).filter(test.User.email== request.username).first()
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
#                                         detail= f"Invalid Credentials")
#     if not Hash.verify(user.password, request.password):
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#                                         detail= f"Incorrect password")
    
#     access_token = token.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token , "token_type" :"bearer"}

def login(request: schemas.Login, db: Session= Depends(database.get_db)):
    user = db.query(test.User).filter(test.User.name == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                        detail=f"Incorrect password")
    return user