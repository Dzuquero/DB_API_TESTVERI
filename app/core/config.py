
import os
DATABASE_URL=os.getenv("DATABASE_URL","postgresql://postgres:postgres@localhost:5432/users")
SECRET_KEY="secret"
ALGORITHM="HS256"
