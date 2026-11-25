"""Contiene la lógica de negocio de mi aplicación."""
from models.task import Task
from repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def find_all(self):
        return self.repository.find_all()

    def create_one(self, title: str, description: str):
        task = Task(title, description)
        self.repository.create_one(task)