# The declarative base class for all our database models, adding automated timestamps (created_at, updated_at).

import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.core.database import Base

class TimeStampedModel(Base):
    """
    Abstract base model that adds UUID primary keys and
    automatic creation/update timestamps to all inherting models.
    """
    __abstract__ = True

    id = Column(
        UUID(uuid=True),
        primary_key=True,
        default=uuid.uuid4, # UUIDv4s are completely random and non-guessable not in a noraml format like 1, 2, 3, 4....
        index=True,
        nullable=False
    )
    created_at = Column(
        DateTime,
        default=datetime.now(datetime.timezone.utc),
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(datetime.timezone.utc),
        onupdate=datetime.now(datetime.timezone.utc),
        nullable=False
    )