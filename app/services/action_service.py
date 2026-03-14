
from app.repositories.action_repository import ActionRepository

repo=ActionRepository()

class ActionService:

    def log(self,db,user_id,action):
        return repo.log(db,user_id,action)

    def last_month(self,db,user_id):
        return repo.last_month(db,user_id)
