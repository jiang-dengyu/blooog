from fastapi import FastAPI
from app.routes import posts

app = FastAPI()

# router
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(posts.router, prefix="/posts")