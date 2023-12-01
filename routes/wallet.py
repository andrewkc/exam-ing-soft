from fastapi import APIRouter
from controllers.WalletCtrl import show_contacts_, show_history_, pay_

routes_wallet = APIRouter()

@routes_wallet.post('/contactos/mimumero/{minumero}')
def show_contacts(minumero: str) -> dict:
    return show_contacts_(minumero)


@routes_wallet.post('/historial/mimumero/{minumero}')
def show_history(minumero: str) -> dict:
    return show_history_(minumero)


@routes_wallet.post('/pagar/mimumero/{minumero}/destnumero/{destnumero}/valor/{valor}')
def pay(minumero: str, destnumero: str, valor: str) -> dict:
    return pay_(minumero, destnumero, valor)
