
"""Fixtures de integração com PostgreSQL."""


from pathlib import Path

import pytest
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

import app.models  # Registra todos os mapeamentos.


@pytest.fixture(scope="session")
def test_engine():
    """Cria o engine exclusivo dos testes."""

    env_file = (
        Path(__file__).resolve().parents[1] / ".env.test"
    )

    database_url = dotenv_values(env_file).get("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL ausente em backend/.env.test"
        )

    url = make_url(database_url)

    if url.database != "constituicao_simples_test":
        raise RuntimeError(
            "Banco de testes inválido. "
            "Esperado: constituicao_simples_test"
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
                join_transaction_mode="create_savepoint",
            ) as session:
                yield session
        finally:
            transaction.rollback()
