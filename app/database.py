from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#variable that stores the path to the database
DATABASE_URL = "sqlite:///./campushub.db"

#variable holding the connection to the database with a function call to initializethe dayabase connection
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
