from sqlalchemy import *
from datetime import datetime
from database.db import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True)

    asset_code = Column(String, unique=True)

    asset_name = Column(String)
    category = Column(String)
    subcategory = Column(String)

    make = Column(String)
    model = Column(String)

    serial_number = Column(String)

    capacity = Column(String)
    rating = Column(String)

    site = Column(String)
    building = Column(String)
    floor = Column(String)
    room = Column(String)

    vendor = Column(String)

    purchase_cost = Column(Float)

    status = Column(String, default="Active")

    warranty_start = Column(Date)
    warranty_end = Column(Date)

    qr_code_path = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

class AMCContract(Base):
    __tablename__ = "amc_contracts"

    id = Column(Integer, primary_key=True)

    contract_number = Column(String, unique=True)

    contract_name = Column(String)

    vendor_name = Column(String)

    amc_type = Column(String)

    start_date = Column(Date)
    end_date = Column(Date)

    contract_cost = Column(Float)

    sla_hours = Column(Integer)

    covered_services = Column(Text)

    excluded_services = Column(Text)

    status = Column(String, default="Active")

    created_at = Column(DateTime, default=datetime.utcnow)