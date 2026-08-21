from fastapi import FastAPI

app = FastAPI(
    title="AI Risk Manager",
    description="AI-powered chargeback and fraud risk management system",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Risk Manager API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }