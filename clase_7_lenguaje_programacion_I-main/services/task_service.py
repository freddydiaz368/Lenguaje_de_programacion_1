"""Contiene la lógica de negocio de mi aplicación."""
from models.task import User
from uuid import UUID
from repositories.task_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def find_all(self):
        return self.repository.find_all()

    def create_one(self, fname: str, lname: str, age: int, email: str):
        user = User(fname, lname, age, email)
        self.repository.create_one(user)

    def delete_one(self, uuid: UUID):
        self.repository.delete_one(uuid)

    def update_user(self, uuid: UUID, fname: str, lname: str, age: int, email: str):
        self.repository.update_user(uuid, fname, lname, age, email)
