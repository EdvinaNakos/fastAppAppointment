from fastapi import APIRouter, HTTPException
from typing import List
from controller.model.appointment_response import AppointmentResponse
from controller.model.appointment_approve_request import AppointmentApprove
from service import appointment_service

router = APIRouter()


@router.get("/", response_model=List[AppointmentResponse])
async def get_appointment(org_code: int):
    appointment = await appointment_service.get_all_org_appointments(org_code)
    return appointment


@router.get("/{appointment_id}", response_model=AppointmentResponse)
async def get_appointment(org_code: int, appointment_id: int):
    appointment = await appointment_service.get_org_appointments_by_appointment_id(org_code, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Note not found")
    return appointment


@router.put("/{appointment_id}/approve", response_model=AppointmentResponse)
async def get_appointment(org_code: int, appointment_id: int, payload: AppointmentApprove):
    appointment = await appointment_service.approve_appointment_by_appointment_id(org_code, appointment_id, payload)
    if not appointment:
        raise HTTPException(status_code=404, detail="Note not found")
    return appointment