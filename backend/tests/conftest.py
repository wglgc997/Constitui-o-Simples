"""Fixtures de integração com PostgreSQL."""

import os
from pathlib import Path

import pytest
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session


@pytest.fixture(scope="session")
def test_engine():
    """Cria o engine exclusivo dos testes."""

    env_file = Path(__file__).resolve().parents[1] / ".env.test"

    # Prioriza a variável de ambiente exclusiva de testes.
    # Utiliza o arquivo .env.test como fallback local.
    database_url = os.getenv("TEST_DATABASE_URL") or dotenv_values(env_file).get(
        "DATABASE_URL"
    )

    if not database_url:
        raise RuntimeError(
            "Configure TEST_DATABASE_URL ou DATABASE_URL em backend/.env.test"
        )

    # Impede a utilização de um banco com nome diferente do esperado.
    url = make_url(database_url)

    if url.database != "constituicao_simples_test":
        raise RuntimeError(
            "Banco de testes inválido. Esperado: constituicao_simples_test"
        )

    engine = create_engine(database_url, pool_pre_ping=True)

    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture
def db_session(test_engine):
    """Fornece uma sessão isolada por transação."""

    with test_engine.connect() as connection:
        transaction = connection.begin()

        try:
            with Session(
                bind=connection,
            ) as session:
                yield session
        finally:
            transaction.rollback()
