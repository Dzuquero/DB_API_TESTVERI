
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.user_service import UserService

router=APIRouter()
service=UserService()

def get_db():
    db=SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/register")
def register(name:str,email:str,password:str,db:Session=Depends(get_db)):
    try:
        u=service.register(db,name,email,password)
        return {"id":u.id}
    except Exception as e:
        raise HTTPException(400,str(e))

@router.post("/login")
def login(email:str,password:str,db:Session=Depends(get_db)):
    try:
        token=service.login(db,email,password)
        return {"access_token":token}
    except Exception as e:
        raise HTTPException(401,str(e))
