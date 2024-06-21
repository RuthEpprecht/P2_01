from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from typing import Generator

# URL de conexão do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Criação do motor de conexão ao banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configuração da fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para os modelos ORM
Base = declarative_base()

# Função geradora para obter uma sessão do banco de dados
@contextmanager
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db  # Entrega a sessão para ser usada
    finally:
        db.close()  # Fecha a sessão após o uso
