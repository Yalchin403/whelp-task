from pydantic import BaseModel


class Ip(BaseModel):
    address: str