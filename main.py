from controller import ping, appointment, backoffice_appointment
from db import engine, metadata, database
from fastapi import FastAPI

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router, prefix="/appointment", tags=["health"])
app.include_router(appointment.router, prefix="/appointment/appoint/{user_id}", tags=["user_appoint"])
app.include_router(backoffice_appointment.router, prefix="/appointment/backoffice/{org_code}", tags=["org_appoint"])
