
"""Testes dos modelos SQLAlchemy."""

from sqlalchemy import inspect
from sqlalchemy.orm import configure_mappers
from sqlalchemy import ForeignKey

from app.models.article import Article
from app.models.theme import Theme
from app.models.article_theme import article_themes
from app.models.practical_example import PracticalExample


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



from app.models.article_explanation import ArticleExplanation


def test_article_explanation_table():
    """Verifica a estrutura da tabela de explicações."""
    assert ArticleExplanation.__tablename__ == "article_explanations"

    columns = {
        column.name
        for column in ArticleExplanation.__table__.columns
    }

    assert {
        "id",
        "article_id",
        "simplified_text",
        "ai_model",
        "review_status",
        "created_at",
        "updated_at",
    }.issubset(columns)


def test_article_explanation_relationship():
    """Verifica o relacionamento 1:N com Article."""
    configure_mappers()

    article_relationship = inspect(
        Article
    ).relationships["explanations"]

    explanation_relationship = inspect(
        ArticleExplanation
    ).relationships["article"]

    assert article_relationship.uselist is True
    assert explanation_relationship.uselist is False

    assert article_relationship.back_populates == "article"
    assert explanation_relationship.back_populates == "explanations"


def test_article_explanation_foreign_key():
    """Verifica a chave estrangeira para articles."""
    column = ArticleExplanation.__table__.columns["article_id"]

    foreign_keys = list(column.foreign_keys)

    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "articles.id"


def test_practical_example_table():
    """Verifica a estrutura da tabela de exemplos práticos."""
    assert PracticalExample.__tablename__ == "practical_examples"

    columns = {
        column.name
        for column in PracticalExample.__table__.columns
    }

    assert {
        "id",
        "article_id",
        "title",
        "description",
        "device_reference",
        "created_at",
    }.issubset(columns)


def test_practical_example_relationship():
    """Verifica o relacionamento 1:N com Article."""
    configure_mappers()

    article_relationship = inspect(
        Article
    ).relationships["practical_examples"]

    example_relationship = inspect(
        PracticalExample
    ).relationships["article"]

    assert article_relationship.uselist is True
    assert example_relationship.uselist is False

    assert article_relationship.back_populates == "article"
    assert example_relationship.back_populates == "practical_examples"


def test_practical_example_foreign_key():
    """Verifica a chave estrangeira para articles."""
    column = PracticalExample.__table__.columns["article_id"]

    foreign_keys = list(column.foreign_keys)

    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "articles.id"


def test_practical_example_device_reference():
    """Verifica se a referência ao dispositivo é opcional."""
    column = PracticalExample.__table__.columns["device_reference"]

    assert column.nullable is True
