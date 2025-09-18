import os
from sqlalchemy import create_engine
from models.marketplace import Base as MarketplaceBase
from models.commodity import Base as CommodityBase
from main import Base

def reset_database():
    # Remove existing database file
    if os.path.exists("krishiai.db"):
        print("Removing existing database...")
        os.remove("krishiai.db")
    
    # Create new database with updated schema
    print("Creating new database...")
    DATABASE_URL = "sqlite:///./krishiai.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    
    # Create all tables from all models
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    MarketplaceBase.metadata.create_all(bind=engine)
    CommodityBase.metadata.create_all(bind=engine)
    
    print("Database reset complete!")

if __name__ == "__main__":
    reset_database()
