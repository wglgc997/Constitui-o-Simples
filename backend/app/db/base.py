"""Classe-base para os modelos do banco"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base compartilhada pelos modelos SQLAlchemy"""
