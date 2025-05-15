from fastapi import FastAPI
from app.config.database import Base, engine
from app.routers import auth

app = FastAPI(title="FastAPI Auth API", description="API for user registration and login", version="1.0.0")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Auth API"}