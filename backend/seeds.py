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

# for _ in range(10):
#     user_data = generate_user_data()
#     insert_query = supabase_client.table("users").insert(user_data)
#     try:
#         insert_query.execute()
#         print(f"Inserted user")
#     except Exception as e:
#         print(f"Error inserting user: {e}")


# def generate_job_data():
#     return {
#         "title": fake.job(),
#         "pay_rate": round(random.uniform(15.00, 100.00), 2),
#         "description": fake.text(max_nb_chars=200),
#         "location": fake.city(),
#         "remote": fake.boolean(),
#         "user_id": random.randint(1,10)
#     }

# for _ in range(50):
#     job_data = generate_job_data()
#     insert_query = supabase_client.table("jobs").insert(job_data)
#     try:
#         insert_query.execute()
#         print(f"Inserted job")
#     except Exception as e:
#         print(f"Error inserting job: {e}")    

# def generate_list_data():
#     return {
#         "name": fake.job(),
#         "user_id": random.randint(1,10)
#     }

# for _ in range(50):
#     list_data = generate_list_data()
#     insert_query = supabase_client.table("lists").insert(list_data)
#     try:
#         insert_query.execute()
#         print(f"Inserted list")
#     except Exception as e:
#         print(f"Error inserting list: {e}")

def generate_applicant_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number": fake.phone_number(),
        "recent_job": fake.job(),
        "user_id": random.randint(1, 10),
        "email": fake.email(),
        "job_id": random.randint(2013,2062),
        "list_id": random.randint(501,550)
    }

for _ in range(200):
    applicant_data = generate_applicant_data()
    insert_query = supabase_client.table("applicants").insert(applicant_data)
    try:
        insert_query.execute()
        print(f"Inserted applicant")
    except Exception as e:
        print(f"Error inserting applicant: {e}")
 

print('seeded')