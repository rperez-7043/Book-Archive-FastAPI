from pydantic import BaseModel, EmailStr


class BookBase(BaseModel):
    title: str
    author: str
    price: float

class BookPublish(BookBase):
    pass

class Book(BookBase):
    id: int



class UserBase(BaseModel):
    email: EmailStr

class UserRegister(UserBase):
    password: str

class Users(UserBase):
    id: int

class User(Users):
    books: list[Book]



class Token(BaseModel):
    access_token: str
    token_type: str
