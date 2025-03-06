from supabase import create_client
from django.conf import settings

supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def create_tables():
    try:
        supabase_client.postgrest.rpc("create_user_table").execute()
        supabase_client.postgrest.rpc("create_explore_table").execute()
        supabase_client.postgrest.rpc("create_search_table").execute()
        print("✅ Supabase Tables Created Successfully")
    except Exception as e:
        print("❌ Connection Failed:", e)