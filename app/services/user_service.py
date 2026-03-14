
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password,verify_password,create_token

repo=UserRepository()

class UserService:

    def register(self,db,name,email,password):
        if repo.get_by_email(db,email):
            raise Exception("Email exists")
        return repo.create(db,name,email,hash_password(password))

    def login(self,db,email,password):
        user=repo.get_by_email(db,email)
        if not user or not verify_password(password,user.password):
            raise Exception("Invalid credentials")
        return create_token({"user_id":user.id})
