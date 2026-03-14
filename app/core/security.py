
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
from .config import SECRET_KEY,ALGORITHM

pwd=CryptContext(schemes=["bcrypt"])

def hash_password(p):
    return pwd.hash(p)

def verify_password(p,h):
    return pwd.verify(p,h)

def create_token(data):
    d=data.copy()
    d["exp"]=datetime.utcnow()+timedelta(hours=24)
    return jwt.encode(d,SECRET_KEY,algorithm=ALGORITHM)
