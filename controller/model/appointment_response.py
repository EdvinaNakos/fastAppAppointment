from datetime import datetime

from pydantic import BaseModel


class AppointmentResponse(BaseModel):
    id: int
    user_id: str
    user_id_aprv: str
    org_code: int
    org_name: str
    is_approved: bool
    appointment_datetime: datetime
    created_datetime: datetime
