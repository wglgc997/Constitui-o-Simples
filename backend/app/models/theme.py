"""Modelo dos temas educativos da Constituição"""

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from app.models.article_theme import article_themes

if TYPE_CHECKING:
    from app.models.article import Article

class Theme(Base):
    """Representa um tema de navegação constitucional"""


    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    articles: Mapped[list["Article"]] = relationship(
        secondary=article_themes,
        back_populates="themes",
    )
