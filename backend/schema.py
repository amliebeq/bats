from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    first_name: str
    last_name: str
    company: str
    job_title: str

    class Config:
        orm_mode = True