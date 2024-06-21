from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from .database import Base, engine

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Método para criar uma nova tarefa
    def create(self, session: Session):
        session.add(self)
        session.commit()
        session.refresh(self)
        return self

    # Método para atualizar uma tarefa existente
    def update(self, session: Session, task_data: dict):
        for key, value in task_data.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)
        return self

    # Método para deletar uma tarefa
    def delete(self, session: Session):
        session.delete(self)
        session.commit()
        return self.id

    # Método estático para ler uma tarefa pelo ID
    @staticmethod
    def read(session: Session, id: int):
        return session.query(Task).filter(Task.id == id).first()

    def __repr__(self):
        return (f'<Task(id={self.id}, title={self.title}, '
                f'description={self.description}, status={self.status}, '
                f'created_at={self.created_at})>')

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

