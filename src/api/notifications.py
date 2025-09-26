from fastapi import APIRouter
from pydantic import BaseModel

#  Creates a Router object.
router = APIRouter(prefix="/notifications")


# Define data contract for the incoming request.
# Returns 400 if data is missing or wrong type.
class NotificationRequest(BaseModel):
    tenant_id: str
    user_id: str
    channel_id: str   # "email" | "sms" | "push"
    message: str


#  Set up a notification api module.
@router.post("/")
async def send_notifications(req: NotificationRequest):
    # Placeholder: just echo
    return {"status": "queued", "notification": req.model_dump()}
