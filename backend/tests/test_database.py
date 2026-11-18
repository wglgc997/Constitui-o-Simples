
"""Testes de integração com PostgreSQL."""

from uuid import uuid4

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.models import (
    Article,
    article_themes,
    ArticleExplanation,
    GlossaryTerm,
    PracticalExample,
    Theme,
)


def unique_value():
    """Gera identificador exclusivo para cada teste."""
    return uuid4().hex[:12]


def make_article():
    """Cria um artigo fictício para testes."""
    return Article(
        number=f"TEST-{unique_value()}",
        title="Artigo de teste",
        original_text="Texto constitucional fictício.",
    )


def test_article_persistence(db_session):
    """Valida inserção e leitura de um artigo."""

    article = make_article()

    db_session.add(article)
    db_session.commit()

    article_id = article.id
    db_session.expire_all()

    saved = db_session.get(Article, article_id)

    assert saved is not None
    assert saved.number == article.number
    assert saved.original_text == "Texto constitucional fictício."


def test_article_theme_relationship(db_session):
    """Valida relacionamento muitos para muitos."""

    article = make_article()
    identifier = unique_value()

    theme = Theme(
        name=f"Direitos Sociais {identifier}",
        slug=f"direitos-sociais-{identifier}",
        description="Tema de teste.",
    )

    article.themes.append(theme)

    db_session.add(article)
    db_session.commit()

    article_id = article.id
    db_session.expire_all()

    saved = db_session.get(Article, article_id)

    assert saved is not None
    assert len(saved.themes) == 1
    assert saved.themes[0].slug == theme.slug


def test_article_explanation_persistence(db_session):
    """Valida armazenamento de explicações."""

    article = make_article()

    explanation = ArticleExplanation(
        simplified_text="Explicação simplificada de teste.",
        device_reference="caput",
        ai_model="test-model",
        review_status="pending",
        review_level="none",
    )

    article.explanations.append(explanation)

    db_session.add(article)
    db_session.commit()

    article_id = article.id
    db_session.expire_all()

    saved = db_session.get(Article, article_id)

    assert saved is not None
    assert len(saved.explanations) == 1
    assert saved.explanations[0].review_status == "pending"
    assert saved.explanations[0].review_level == "none"
    assert saved.explanations[0].article_id == article_id


def test_practical_example_persistence(db_session):
    """Valida múltiplos exemplos para um artigo."""

    article = make_article()

    article.practical_examples.extend([
        PracticalExample(
            title="Educação",
            description="Exemplo fictício sobre educação.",
            device_reference="caput",
        ),
        PracticalExample(
            title="Saúde",
            description="Exemplo fictício sobre saúde.",
            device_reference="caput",
        ),
    ])

    db_session.add(article)
    db_session.commit()

    article_id = article.id
    db_session.expire_all()

    saved = db_session.get(Article, article_id)

    assert saved is not None
    assert len(saved.practical_examples) == 2

    titles = {
        example.title
        for example in saved.practical_examples
    }

    assert titles == {"Educação", "Saúde"}


def test_article_explanation_cascade_delete(db_session):
    """Valida ON DELETE CASCADE no PostgreSQL."""

    article = make_article()

    article.explanations.append(
        ArticleExplanation(
            simplified_text="Explicação fictícia.",
            review_status="pending",
            review_level="none",
        )
    )

    db_session.add(article)
    db_session.flush()

    article_id = article.id
    explanation_id = article.explanations[0].id

    # DELETE direto: testa a FK do PostgreSQL.
    db_session.execute(
        Article.__table__.delete().where(
            Article.id == article_id
        )
    )

    remaining = db_session.scalar(
        select(ArticleExplanation.id).where(
            ArticleExplanation.id == explanation_id
        )
    )

    assert remaining is None


def test_article_number_unique_constraint(db_session):
    """Impede dois artigos com o mesmo número."""

    number = f"TEST-{unique_value()}"

    db_session.add(
        Article(
            number=number,
            original_text="Primeiro texto.",
        )
    )
    db_session.flush()

    db_session.add(
        Article(
            number=number,
            original_text="Segundo texto.",
        )
    )

    with pytest.raises(IntegrityError):
        db_session.flush()


def test_article_original_text_not_null(db_session):
    """Impede artigo sem texto constitucional."""

    article = Article(
        number=f"TEST-{unique_value()}",
        original_text=None,
    )

    db_session.add(article)

    with pytest.raises(IntegrityError):
        db_session.flush()


def test_explanation_article_foreign_key(db_session):
    """Impede explicação associada a artigo inexistente."""

    explanation = ArticleExplanation(
        article_id=999999999,
        simplified_text="Explicação sem artigo.",
        review_status="pending",
        review_level="none",
    )

    db_session.add(explanation)

    with pytest.raises(IntegrityError):
        db_session.flush()


def test_glossary_term_persistence(db_session):
    """Valida gravação e leitura do glossário."""

    term_name = f"Termo {unique_value()}"

    term = GlossaryTerm(
        term=term_name,
        definition="Definição jurídica simplificada.",
    )

    db_session.add(term)
    db_session.commit()

    db_session.expire_all()

    saved = db_session.scalar(
        select(GlossaryTerm).where(
            GlossaryTerm.term == term_name
        )
    )

    assert saved is not None
    assert saved.definition == (
        "Definição jurídica simplificada."
    )


def test_glossary_term_unique_constraint(db_session):
    """Impede duplicação de termos do glossário."""

    term_name = f"Termo {unique_value()}"

    db_session.add(
        GlossaryTerm(
            term=term_name,
            definition="Primeira definição.",
        )
    )
    db_session.flush()

    db_session.add(
        GlossaryTerm(
            term=term_name,
            definition="Segunda definição.",
        )
    )

    with pytest.raises(IntegrityError):
        db_session.flush()
