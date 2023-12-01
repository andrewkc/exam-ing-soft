from typing import List
from models.Operation import Operation

class Account:
    def __init__(self, number, name, saldo, contacts) -> None:
        self.number: str = number 
        self.name: str = name
        self.saldo: int = saldo
        self.contacts: List[str] = contacts
        self.operations: List[Operation] = []

    def history() -> None:
        pass

    def pay(destination: str, value: int) -> None:
        pass
