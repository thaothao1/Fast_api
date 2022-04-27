from fastapi import APIRouter
from api.router import action , authentication


router = APIRouter() 

router.include_router(action.router, tags=["action"] , prefix="/action")
router.include_router(authentication.router, tags=["test"] , prefix="/test")