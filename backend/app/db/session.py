"""Configuração de conexão e sessões PostgreSQL"""

from _collections_abc import Generator

from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# A engine gerencia o acesso ao banco e seu pool de conexões.
# A conexão efetiva normalmente ocorre na primeira operação.
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 5}
)

# Fábrica responsável por criar sessões independentes.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

def get_db() -> Generator[Session, None, None]:
    """Fornece uma sessão e garante o seu fechamento ao final."""
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
