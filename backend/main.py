from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS: Allow frontend (temporarily allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev: allow all; later restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Today backend is working!"}

@app.get("/api/hello")
def say_hello():
    return {"message": "Hello from your AI Today backend!"}
