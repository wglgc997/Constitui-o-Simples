"""Associação entre tabelas theme e article"""
from sqlalchemy import Column, ForeignKey, Integer, Table

from app.db.base import Base

article_themes = Table(
    "article_themes",
    Base.metadata,
    Column(
        "article_id",
        Integer,
        ForeignKey("articles.id", ondelete="CASCADE"),
        primary_key=True,
    ),

    Column(
        "theme_id",
        Integer,
        ForeignKey("themes.id", ondelete="CASCADE"),
        primary_key=True,
    )
)
