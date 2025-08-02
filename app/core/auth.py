from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings
from db.models import User
from db.database import user_collection

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def authenticate_user(email: str, password: str):
    user = user_collection.find_one({"email": email})

    if user and verify_password(password, user["hashed_password"]):
        return User(**user)
    return False