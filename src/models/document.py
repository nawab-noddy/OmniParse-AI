# this file need for keeping thr track of the documents (e.g., pending → processing → indexed → failed)
# we can also store the data in vector DB too, however Vector stores are optimized for similarity search, not transactional state updates,
# foreign keys, or relational joins with users, audit logs, or chunks.

import enum
from sqlalchemy import Enum, String, Integer, Text
from sqlalchemy.orm import mapped_column, Mapped
from src.models.base import TimeStampedModel

class DocumentStatus(str, enum.Enum):
    """Tracks the asynchronous ingestion lifecycle of a document."""

    PENDING = "pending"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"

class Document(TimeStampedModel):
    """Represent an ingested enterprise document and its processing state."""

    __tablename__ = "documents"

    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    content_type: Mapped[str] = mapped_column(String(100), nullable=False)
    file_size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    file_hash: Mapped[str] = mapped_column(
        String(64), unique=True, index=True, nullable=False
    )
    storage_path: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus, name="document_status_enum"),
        default=DocumentStatus.PENDING,
        index=True,
        nullable=False,
    )
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    page_count: Mapped[int | None] = mapped_column(Integer, nullable=True)