from datetime import datetime

from pydantic import BaseModel


class AppointmentCreateRequest(BaseModel):
    org_code: int
    org_name: str
    appointment_datetime: datetime 
    

