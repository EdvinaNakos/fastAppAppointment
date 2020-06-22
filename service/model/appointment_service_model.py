from datetime import datetime

class AppointmentCreate:
    user_id: str
    user_id_aprv: str
    org_code: int
    org_name: str
    is_approved: int 
    appointment_datetime: datetime