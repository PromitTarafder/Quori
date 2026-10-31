import uuid
from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id : Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    user_id : Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    amount : Mapped[Decimal] = mapped_column(
        Numeric(12,2),
        nullable=False
    )

    type: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description : Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    transaction_date : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda : datetime.now(timezone.utc),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )