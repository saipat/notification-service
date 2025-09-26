from fastapi import FastAPI
from src.api import notifications

app = FastAPI(title="Notification Service")


# Register a GET route at /health
@app.get("/health")
async def health_check():
    return {"status": "ok"}


# hook in the notification API
app.include_router(notifications.router)
