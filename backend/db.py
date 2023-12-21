import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ['SUPABASE_URL']
SUPABASE_ANON_KEY = os.environ['SUPABASE_ANON_KEY']

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise ValueError("Missing Supabase environment variables. Please set SUPABASE_URL and SUPABASE_ANON_KEY.")

supabase_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)