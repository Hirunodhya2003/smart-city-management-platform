from fastapi import FastAPI

app = FastAPI(
    title="Smart City Management Platform API",
    description="Backend API for the Smart City Management Platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart City Management Platform",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "smart-city-backend",
    }
