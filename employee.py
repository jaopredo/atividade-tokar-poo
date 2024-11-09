from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    cpf: str
    salary: float
    position: str
    store: Store