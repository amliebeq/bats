from models import User
from fastapi import FastAPI
from db import supabase_client

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    response = supabase_client.table("users").select("*").execute()
    users = response.data
    return users

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