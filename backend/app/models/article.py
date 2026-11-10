"""Modelo de armazenamento dos artigos da Constituição"""

from typing import TYPE_CHECKING

from datetime import datetime

from app.db.base import Base
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.models.article_theme import article_themes

if TYPE_CHECKING:
    from app.models.theme import Theme

class Article(Base):
    """Representa um artigo da Constituição"""

    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    #Nunca deve receber conteúdo simplificado pela IA. As explicações serão armazenadas em outra tabela,
    # garantindo a separação entre a Constituição oficial e o conteúdo educativo.
    original_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    structure: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
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

    themes: Mapped[list["Theme"]] = relationship(
        secondary=article_themes,
        back_populates="articles",
    )
