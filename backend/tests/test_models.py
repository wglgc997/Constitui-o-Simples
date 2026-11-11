
"""Testes dos modelos SQLAlchemy."""

from sqlalchemy import inspect
from sqlalchemy.orm import configure_mappers

from app.models.article import Article
from app.models.theme import Theme
from app.models.article_theme import article_themes


def test_article_table_name():
    """Verifica o nome da tabela de artigos."""
    assert Article.__tablename__ == "articles"


def test_theme_table_name():
    """Verifica o nome da tabela de temas."""
    assert Theme.__tablename__ == "themes"


def test_article_theme_association():
    """Verifica as colunas da tabela associativa."""
    assert article_themes.name == "article_themes"

    columns = {
        column.name
        for column in article_themes.columns
    }

    assert columns == {"article_id", "theme_id"}


def test_article_theme_relationship():
    """Verifica o relacionamento N:N entre artigos e temas."""
    configure_mappers()

    article_relationship = inspect(
        Article
    ).relationships["themes"]

    theme_relationship = inspect(
        Theme
    ).relationships["articles"]

    assert article_relationship.secondary is article_themes
    assert theme_relationship.secondary is article_themes

    assert article_relationship.back_populates == "articles"
    assert theme_relationship.back_populates == "themes"

    assert article_relationship.uselist is True
    assert theme_relationship.uselist is True
