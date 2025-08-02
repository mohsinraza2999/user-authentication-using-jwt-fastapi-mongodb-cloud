from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

import schemas.schemas as schemas,core.config as config
from db.database import user_collection
from db.models import User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Dependency
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user =user_collection.find_one({"email": email})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return User(**user)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Read user profile
@router.get("/me", response_model=schemas.UserCreate)
def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "username": current_user.username,
        "password": "********"
    }

# Update username
@router.put("/me")
def update_user(username: str, current_user: User = Depends(get_current_user)):
    user_collection.update_one({"email": current_user.email}, {"$set": {"username": username}})
    return {"msg": "Username updated"}

# Delete account
@router.delete("/me")
def delete_user(current_user: User = Depends(get_current_user)):
    user_collection.delete_one({"email": current_user.email})
    return {"msg": "User deleted"}