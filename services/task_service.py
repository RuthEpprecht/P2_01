from pydantic import parse_obj_as
from typing import Type

from domain.dto.dtos import TasksCreateDTO, TasksDTO, TasksUpdateDTO
from domain.model.models import Tasks
from repository.task_repository import ITaskRepository

class ITaskService:
    def create_task(self, task_data: TasksCreateDTO) -> TasksDTO:
        """Cria uma nova tarefa."""
        raise NotImplementedError
    
    def read_task(self, task_id: int) -> TasksDTO:
        """Lê uma tarefa pelo ID."""
        raise NotImplementedError
    
    def update_task(self, task_id: int, task_update: TasksUpdateDTO) -> TasksDTO:
        """Atualiza uma tarefa existente pelo ID."""
        raise NotImplementedError
    
    def delete_task(self, task_id: int) -> int:
        """Deleta uma tarefa pelo ID."""
        raise NotImplementedError
    

class TaskService(ITaskService):
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def create_task(self, task_data: TasksCreateDTO) -> TasksDTO:
        """Cria uma nova tarefa a partir dos dados fornecidos."""
        task = Tasks(**task_data.dict())
        created_task = self.task_repository.create(task)
        return parse_obj_as(TasksDTO, created_task)

    def read_task(self, task_id: int) -> TasksDTO:
        """Lê uma tarefa existente pelo ID."""
        task = self.task_repository.read(task_id)
        if task is None:
            raise ValueError("Task não encontrada!")
        return parse_obj_as(TasksDTO, task)
    
    def update_task(self, task_id: int, task_data: TasksUpdateDTO) -> TasksDTO:
        """Atualiza uma tarefa existente com os novos dados fornecidos."""
        task = self.task_repository.read(task_id)
        if task is None:
            raise ValueError("Task não encontrada")

        updated_task = self.task_repository.update(task, task_data.dict(exclude_unset=True))
        return parse_obj_as(TasksDTO, updated_task)
    
    def delete_task(self, task_id: int) -> int:
        """Deleta uma tarefa existente pelo ID."""
        task = self.task_repository.read(task_id)
        if task is None:
            raise ValueError("Task não encontrada!")
        return self.task_repository.delete(task)
