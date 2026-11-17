# Manages the database engine, session factory, and FastAPI dependency injection for database sessions.
# -> session factory = object which generates database or web instances with fixed configurations.


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import setting # have to make this setting.py in config section

# 1. Create the SQLAlchemy engine
# pool_pre_ping=True prevents errors from dropped/stale database connections.

engine = create_engine(
    setting.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True, # To handle sudden operational crashes if cloud env like Docker silently close the conn
    pool_size=10,
    max_overflow=20
)

# 2. Create a configured "SessionLocal" class
# Each instance of SessionLocal will be a database session

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

# 3. Base class for our SQLAlchemy models to inherit from

Base = declarative_base()

# 4. Dependency function for FastAPI routes

def get_db():
    """
    Yields a database session per request, ensuring it is automatically closed after a
    request finishes, even if error occurs
    """
    db = SessionLocal()
    try:
        yield db # - Yiled used inside a dependency guarantees proper resource cleanup.
    finally:
        db.close()
