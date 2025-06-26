from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv
from groq import Groq
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
    
@app.get("/api/test-groq")
def test_groq():
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a a traditional conservative person."},
                {
                    "role": "user",
                    "content": (
                        "Tell your opinion about cutting cost of reusable energy "
                    ),
                },
            ],
        )

        return {"data": chat_completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
