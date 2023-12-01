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





"""
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        elif cantidad > self.saldo:
            print("Error: Fondos insuficientes.")
        else:
            print("Error: La cantidad a retirar debe ser mayor que cero.")

    def obtener_saldo(self):
        return self.saldo
"""