from typing import Optional

from pydantic import BaseModel

class TasksDTO(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: str

    class Config:
        from_attributes = True


class TasksCreateDTO(BaseModel):
    title: str
    description: str
    status: str
    created_at: str

    class Config:
        from_attributes = True


class TasksUpdateDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
        