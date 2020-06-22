import os

from databases import Database
from sqlalchemy import (Column, TIMESTAMP, Integer, MetaData, String, Table, Boolean, create_engine)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = "postgresql://localhost/APIPROJECT?user=postgres&password=password12"


# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
appointment = Table(
    "appointment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", String(36), nullable=False),
    Column("user_id_aprv", String(36), nullable=True),
    Column("org_code", Integer, nullable=False),
    Column("org_name", String(50), nullable=True),
    Column("is_approved", Boolean, default=0, nullable=False),
    Column("appointment_datetime", TIMESTAMP(timezone=True), nullable=False),
    Column("created_datetime", TIMESTAMP(timezone=True), default=func.now(), nullable=False)
)

# databases query builder
database = Database(DATABASE_URL)
