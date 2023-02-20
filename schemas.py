from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    email: str
    password: str
    role: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Login(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: Optional[str] = None


class Form(BaseModel):
    Author: str
    Form: str
    Form_Name: str
    Privacy: str


class Data(BaseModel):
    writer: str
    formId: str
    answer: str
