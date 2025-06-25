from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "AI Today backend is working!"}

@app.get("/api/hello")
def say_hello():
    return {"message": "Fadl Ghaddar1"}

@app.get("/api/test-supabase")
def test_supabase():
    try:
        response = supabase.table("Articles").select("*").execute()
        return {"data": response.data}
    except Exception as e:
        return {"error": str(e)}