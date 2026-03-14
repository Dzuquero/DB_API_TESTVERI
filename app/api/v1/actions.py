
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.action_service import ActionService

router=APIRouter()
service=ActionService()

def get_db():
    db=SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/actions")
def log_action(user_id:int,action_type:str,db:Session=Depends(get_db)):
    return service.log(db,user_id,action_type)

@router.get("/user_actions")
def user_actions(user_id:int,db:Session=Depends(get_db)):
    return service.last_month(db,user_id)
