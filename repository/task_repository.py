from sqlalchemy.orm import Session
from domain.model.models import Tasks

class ITaskRepository:
    def create(self, task: Tasks) -> Tasks:
        """Cria uma nova tarefa."""
        raise NotImplementedError
    
    def read(self, id: int) -> Tasks:
        """Lê uma tarefa pelo ID."""
        raise NotImplementedError
    
    def update(self, task: Tasks, task_data: dict) -> Tasks:
        """Atualiza uma tarefa com os dados fornecidos."""
        raise NotImplementedError
    
    def delete(self, task: Tasks) -> int:
        """Deleta uma tarefa e retorna seu ID."""
        raise NotImplementedError

class TaskRepository(ITaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: Tasks) -> Tasks:
        """Cria uma nova tarefa no banco de dados."""
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def update(self, task: Tasks, task_data: dict) -> Tasks:
        """Atualiza uma tarefa existente com novos dados."""
        for key, value in task_data.items():
            setattr(task, key, value)
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete(self, task: Tasks) -> int:
        """Deleta uma tarefa do banco de dados e retorna seu ID."""
        task_id = task.id
        self.session.delete(task)
        self.session.commit()
        return task_id

    def read(self, task_id: int) -> Tasks:
        """Lê uma tarefa pelo ID do banco de dados."""
        return self.session.query(Tasks).filter(Tasks.id == task_id).first()

        