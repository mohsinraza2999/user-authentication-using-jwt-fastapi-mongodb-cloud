from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: str
    username: str
    hashed_password: str

class UserInDB(User):
    pass