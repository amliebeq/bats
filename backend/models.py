from pydantic import BaseModel, HttpUrl

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str
    job_title: str

class Applicant(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    phone_number: str
    recent_job: str
    email: str
    resume_url: HttpUrl = None


class Jobs(BaseModel):
    title: str
    pay_rate: float
    description: str
    location: str
    remote: bool
    user_id: int