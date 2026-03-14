
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from app.models.action import Action

class ActionRepository:

    def log(self,db:Session,user_id:int,action_type:str):
        a=Action(user_id=user_id,action_type=action_type)
        db.add(a)
        db.commit()
        return a

    def last_month(self,db:Session,user_id:int):
        month=datetime.utcnow()-timedelta(days=30)
        return db.query(Action).filter(Action.user_id==user_id).filter(Action.created_at>=month).all()
