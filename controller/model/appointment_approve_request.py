from datetime import datetime

from pydantic import BaseModel


class AppointmentApprove(BaseModel):
    appointment_datetime: datetime 
    user_id: str