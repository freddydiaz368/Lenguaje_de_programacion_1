"""Esta clase modela los datos de una tarea"""
from dataclasses import dataclass, field
from uuid import UUID, uuid4

# Decorador -> Extiende la funcionalidad de mi class o funciones
@dataclass
class Task:
    title: str
    description: str
    uuid: UUID = field(default_factory=uuid4)