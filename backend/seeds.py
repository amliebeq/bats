from db import supabase_client
from faker import Faker
import random

print('seeding')

fake = Faker("en_US")

# def generate_user_data():
#     return {
#         "first_name": fake.first_name(),
#         "last_name": fake.last_name(),
#         "company": fake.company(),
#         "job_title": fake.job(),
#         "password_hash": fake.password(length=60),
#         "email": fake.email(),
#     }

# for _ in range(5):
#     user_data = generate_user_data()
#     insert_query = supabase_client.table("users").insert(user_data)
#     try:
#         insert_query.execute()
#         print(f"Inserted user: {user_data['first_name']} {user_data['last_name']}")
#     except Exception as e:
#         print(f"Error inserting user: {e}")

def generate_applicant_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number": fake.phone_number(),
        "recent_job": fake.job(),
        "user_id": random.randint(1, 5),
        "email": fake.email(),
    }

for _ in range(50):
    applicant_data = generate_applicant_data()
    insert_query = supabase_client.table("applicants").insert(applicant_data)
    try:
        insert_query.execute()
        print(f"Inserted applicant: {applicant_data['first_name']} {applicant_data['last_name']}")
    except Exception as e:
        print(f"Error inserting applicant: {e}")    

print('seeded')