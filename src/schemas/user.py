from pydantic import BaseModel
import dotenv
import os


dotenv.load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


class User(BaseModel):
    age: int
    name: str
    surname: str
    username: str
    email: str
    gender: str
    password: str

    class Config:
        show_extra = {
            "example": {
                "age": "21",
                "name": "Yalchin",
                "surname": "Mammadli",
                "username": "Yalchin403",
                "email": "yalchinmammadli@yalchin.info",
                "gender": "M",
                "password": "DummyPassword-1234"
            }
        }


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "exampple": {
                "username": "Yalchin403",
                "password": "DummyPassowrd-1234"
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str = SECRET_KEY