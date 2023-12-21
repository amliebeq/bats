from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str
    job_title: str