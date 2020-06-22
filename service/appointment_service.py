from sqlalchemy import and_
from datetime import datetime
from db import appointment, database
from service.model.appointment_service_model import AppointmentCreate
from controller.model.appointment_approve_request import AppointmentApprove



async def create_appointment(payload: AppointmentCreate):
    query = appointment.insert().values(
        user_id = payload.user_id
        , user_id_aprv = payload.user_id_aprv
        , org_code = payload.org_code
        , org_name = payload.org_name
        , is_approved = payload.is_approved
        , appointment_datetime = payload.appointment_datetime       
        )
    appointment_id = await database.execute(query=query)
    return await get_appointment_by_user_id_and_appointment_id(payload.user_id, appointment_id)


async def get_all_org_appointments(org_code: int):
    query = appointment \
        .select() \
        .where(appointment.c.org_code == org_code)
    return await database.fetch_all(query=query)


async def get_org_appointments_by_appointment_id(org_code:int, appointment_id: int):
    query = appointment \
        .select() \
        .where(
            and_(
                appointment.c.org_code == org_code,
                appointment.c.id == appointment_id, 
                )
        )

    return await database.fetch_one(query=query)


async def get_appointment_by_user_id(user_id: str):
    query = appointment \
        .select() \
        .where(appointment.c.user_id == user_id)
    return await database.fetch_all(query=query)


async def get_appointment_by_user_id_and_appointment_id(user_id: str, appointment_id: int):
    query = appointment \
        .select() \
        .where(
        and_(
            appointment.c.id == appointment_id,
            appointment.c.user_id == user_id
        )
    )
    return await database.fetch_one(query=query)


async def delete_appointment(appointment_id: int):
    query = appointment \
        .delete() \
        .where(appointment.c.id == appointment_id)
    return await database.execute(query=query)


async def approve_appointment_by_appointment_id(org_code: int, appointment_id: int, payload: AppointmentApprove):
    query = appointment.update() \
        .values(
            appointment_datetime = payload.appointment_datetime,
            user_id_aprv = payload.user_id, 
            is_approved = True
            ) \
                .where(
                    and_(
                        appointment.c.org_code == org_code,
                        appointment.c.id == appointment_id
                    )
                )
    await database.execute(query = query)
    return await get_org_appointments_by_appointment_id(org_code, appointment_id)