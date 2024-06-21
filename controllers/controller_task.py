from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from domain.model.database import get_db
from domain.dto.dtos import TasksDTO, TasksCreateDTO, TasksUpdateDTO
from repository.task_repository import TaskRepository
from services.task_service import TaskService

# Definição do router com prefixo e tags
task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Função para obter o repositório de tarefas com a sessão do banco de dados
def get_tasks_repo(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)

# Endpoint para criar uma nova tarefa
@task_router.post("/", status_code=201, response_model=TasksDTO)
def create_task(request: TasksCreateDTO, task_repo: TaskRepository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.create_task(request)

# Endpoint para buscar uma tarefa pelo ID
@task_router.get("/{task_id}", status_code=200, response_model=TasksDTO)
def find_task_by_id(task_id: int, task_repo: TaskRepository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.read_task(task_id)

# Endpoint para buscar todas as tarefas
@task_router.get("/", status_code=200, response_model=list[TasksDTO])
def get_all_tasks(task_repo: TaskRepository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.find_all()

# Endpoint para atualizar uma tarefa
@task_router.put("/{task_id}", status_code=200, response_model=TasksDTO)
def update_task(task_id: int, request: TasksUpdateDTO, task_repo: TaskRepository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    return task_service.update_task(task_id, request)

# Endpoint para deletar uma tarefa
@task_router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, task_repo: TaskRepository = Depends(get_tasks_repo)):
    task_service = TaskService(task_repo)
    task_service.delete_task(task_id)
