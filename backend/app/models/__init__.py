"""Registro centralizado dos modelos SQLAlchemy."""

from app.models.article import Article
from app.models.article_explanation import ArticleExplanation
from app.models.article_theme import article_themes
from app.models.glossary_term import GlossaryTerm
from app.models.practical_example import PracticalExample
from app.models.theme import Theme

__all__ = [
    "Article",
    "Theme",
    "article_themes",
    "ArticleExplanation",
    "PracticalExample",
    "GlossaryTerm",
]
