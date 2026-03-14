
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime
from app.db.database import Base

class Action(Base):
    __tablename__="actions"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    action_type=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)
