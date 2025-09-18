from sqlalchemy import Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CommodityPrice(Base):
    __tablename__ = 'commodity_prices'
    
    id = Column(String, primary_key=True)
    state = Column(String, nullable=False)
    district = Column(String, nullable=False) 
    market = Column(String, nullable=False)
    commodity = Column(String, nullable=False)
    variety = Column(String)
    grade = Column(String)
    arrival_date = Column(Date, nullable=False)
    min_price = Column(Float)
    max_price = Column(Float)
    modal_price = Column(Float)
