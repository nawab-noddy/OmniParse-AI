# Manages the database engine, session factory, and FastAPI dependency injection for database sessions.
# -> session factory = object ehich generates database or web instances with fixed configurations.


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import setting # have to make this setting.py in congig section

