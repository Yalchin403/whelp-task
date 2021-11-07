from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from config.db import conn
from models.users import User as users
from schemas.user import User, UserLogin
from auth.auth import AuthHandler
from fastapi_jwt_auth import AuthJWT
from schemas.user import Settings


user = APIRouter()
auth_handler = AuthHandler()


@AuthJWT.load_config
def get_config():
    return Settings()


@user.post("/api/v1/auth")
async def login(user: UserLogin, Authorize: AuthJWT=Depends()):

    if user:
        
        try:
            user_obj = users.get(users.username==user.username)

            if user_obj:

                if auth_handler.verify_password(user.password, user_obj.password):

                    access_token = Authorize.create_access_token(subject=user_obj.username)

                    return {"access_token": access_token}
        
        except:
            raise HTTPException(status_code=401, detail="Invalid username/password")


@user.post("/api/v1/signup")
async def create_user(user: User):
    hashed_password = auth_handler.get_password_hash(user.password)

    is_exist = users.select().where(users.username == user.username)

    if not is_exist:
        user_obj = users(
            age=user.age,
            name=user.name,
            surname=user.surname,
            username=user.username,
            # we can check if it's really an email or not and make the email all lowercase
            email=user.email,
            gender=user.gender,
            password=hashed_password

        )
        user_obj.save()
        return {"name": user_obj.name,
                "surname": user_obj.surname,
                "username": user_obj.username,
                "email": user_obj.email,
                "gender": user_obj.gender,
                "age": user_obj.age
        }
    
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is taken")

@user.post("/api/v1/refresh")
async def refresh_token(user: UserLogin, Authorize: AuthJWT=Depends()):
    if user:

        try:

            user_obj = users.get(users.username==user.username)
                
            if user_obj:

                if auth_handler.verify_password(user.password, user_obj.password):
                    
                    refresh_token = Authorize.create_refresh_token(subject=user_obj.username)

                    return {"refresh_token": refresh_token}
        except:

            raise HTTPException(status_code=401, detail="Invalid username/password")


@user.get("/user")
async def get_current_user(Authorize: AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    username = Authorize.get_jwt_subject()
    current_user_obj = users.get(users.username == username)

    return {"name": current_user_obj.name,
            "surname": current_user_obj.surname,
            "username": current_user_obj.username,
            "email": current_user_obj.email,
            "gender": current_user_obj.gender,
            "age": current_user_obj.age
    }
