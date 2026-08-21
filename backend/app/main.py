from fastapi import FastAPI
from app.database import client
from app.routes.chargebacks import router as chargeback_router

app = FastAPI(
    title="AI Risk Manager",
    description="AI-powered chargeback and fraud risk management system",
    version="1.0.0"
)

app.include_router(chargeback_router)


@app.get("/")
def home():
    return {
        "message": "AI Risk Manager API is running"
    }


@app.get("/health")
def health():

    try:
        client.admin.command("ping")

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }