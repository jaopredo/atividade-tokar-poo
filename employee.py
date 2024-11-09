from dataclasses import dataclass
from store import Store


@dataclass
class Employee:
    name: str
    cpf: str
    salary: float
    position: str
    store: Store