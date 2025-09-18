from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class MarketListing(Base):
    __tablename__ = "market_listings"
    
    id = Column(String, primary_key=True)
    seller_name = Column(String, nullable=False)  # Changed from farmer_id
    crop_name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    price_per_kg = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    state = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="available")
