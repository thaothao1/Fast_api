from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from models import schemas, database , oauth2
from api.repository import blog
from sqlalchemy.orm import Session


router = APIRouter()
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/' , status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user : schemas.User= Depends(oauth2.get_current_user)):
    return blog.create(request)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}' , status_code = 200 , response_model = schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)