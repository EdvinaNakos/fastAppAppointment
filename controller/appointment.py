from fastapi import APIRouter, HTTPException

from typing import List
from controller.model.appointment_create_request import AppointmentCreateRequest
from controller.model.appointment_response import AppointmentResponse
from service import appointment_service
from service.model.appointment_service_model import AppointmentCreate

router = APIRouter()


@router.post("/", response_model=AppointmentResponse, status_code=201)
async def create_appointment(user_id: str, payload: AppointmentCreateRequest):
    appointment_create = AppointmentCreate()
    appointment_create.user_id = user_id
    appointment_create.user_id_aprv = ""
    appointment_create.org_code = payload.org_code
    appointment_create.org_name = payload.org_name
    appointment_create.is_approved = False
    appointment_create.appointment_datetime = payload.appointment_datetime
    appointment = await appointment_service.create_appointment(appointment_create)

    return appointment


@router.get("/", response_model=List[AppointmentResponse])
async def get_appointment(user_id: str):
    appointment = await appointment_service.get_appointment_by_user_id(user_id)
    return appointment


@router.get("/{appointment_id}", response_model=AppointmentResponse)
async def get_appointment(user_id: str, appointment_id: int):
    appointment = await appointment_service.get_appointment_by_user_id_and_appointment_id(user_id, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Note not found")
    return appointment


@router.delete("/{appointment_id}", response_model=AppointmentResponse)
async def delete_appointment(user_id: str, appointment_id: int):
    appointment = await appointment_service.get_appointment_by_user_id_and_appointment_id(user_id, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Note not found")

    await appointment_service.delete_appointment(appointment_id)
    return appointment
