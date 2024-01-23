from models import User, Applicant
from db import supabase_client
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    users_response = supabase_client.table("users").select("*").execute()
    users = users_response.data
    return users

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user_response = supabase_client.table("users").select("*").eq("id", user_id).execute()
    user_data = user_response.data

    if user_data:
        user = user_data[0]

        user_applicants_response = supabase_client.table("applicants").select("*").eq("user_id", user_id).execute()
        user_applicants = user_applicants_response.data

        user_jobs_response = supabase_client.table("jobs").select("*").eq("user_id", user_id).execute()
        user_jobs = user_jobs_response.data

        user_lists_response = supabase_client.table("lists").select("*").eq("user_id", user_id).execute()
        user_lists = user_lists_response.data

        user['jobs'] = user_jobs
        user['applicants'] = user_applicants
        user['lists'] = user_lists

    return user

@app.post("/users")
async def create_user(user_data: User):
    insert_query = supabase_client.table("users").insert(user_data.dict())
    try:
        response = insert_query.execute()
        return {"message": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    delete_query = supabase_client.table("users").delete().eq("id", user_id)
    try:
        response = delete_query.execute()
        return {"message": "User deleted successfully"}
    except Exception as e:
        return {"error": str(e)}
    
@app.put("/users/{user_id}")
async def update_user(user_id: str, updated_user_data: User):
    update_query = supabase_client.table("users").update(updated_user_data.dict()).eq("id", user_id)
    try:
        response = update_query.execute()
        return {"message": "User updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/upload-resume/{applicant_id}")
async def upload_resume(applicant_id: int, file: UploadFile = File(...)):

    resume_url, upload_response = await _upload_file_to_supabase(applicant_id, file)
    
    await _update_applicant_resume(applicant_id, resume_url)

    return {
        "resume_url": resume_url
    }

async def _upload_file_to_supabase(applicant_id: int, file: UploadFile):
    bucket = 'applicants-resumes'
    file_path = f"resumes/{applicant_id}/{file.filename}"

    contents = await file.read()

    response = supabase_client.storage.from_(bucket).upload(file_path, contents, {"Content-Type": file.content_type})
    public_url = supabase_client.storage.from_(bucket).get_public_url(file_path)

    return public_url, response


async def _update_applicant_resume(applicant_id: int, resume_url: str):
    update_query = supabase_client.table("applicants").update({"resume_url": resume_url}).eq("id", applicant_id)
    try:
        response = update_query.execute()
        if response.error:
            raise Exception(response.error.message)
        return {"message": "Applicant resume updated successfully"}
    except Exception as e:
        return {"error": str(e)}