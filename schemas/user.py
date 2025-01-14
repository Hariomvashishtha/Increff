from typing import Optional
from pydantic import BaseModel
class User(BaseModel):
    name:str
    email:str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
