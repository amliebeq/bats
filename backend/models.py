from pydantic import BaseModel

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

class Jobs(BaseModel):
    title: str
    pay_rate: float
    description: str
    location: str
    remote: bool


def get_user_with_applicants(user_id: int):
    user = supabase_client.table("User").select("*").eq("id", user_id).execute()
    applicants = supabase_client.table("Applicant").select("*").eq("user_id", user_id).execute()
    return user, applicants