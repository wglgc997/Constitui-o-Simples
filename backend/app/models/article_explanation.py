"""Modelo das explicações educativas dos artigos constitucionais."""


from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.article import Article


class ArticleExplanation(Base):
    """Armazena explicações simplificadas de artigos."""

    __tablename__ = "article_explanations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    simplified_text: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    ai_model: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    review_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    article: Mapped["Article"] = relationship(
        "Article",
        back_populates="explanations",
    )
