from fastapi import FastAPI
from typing import List
from models.Account import Account
from routes.wallet import routes_wallet
from fastapi.middleware.cors import CORSMiddleware
from data.DB import DB

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(routes_wallet, prefix="/billetera")

"""
Ultima pregunta:
Se tendria que agregar nuevos métodos para que se tomen en cuenta estos casos. Por ejemplo, algun metodo que limite el monto de transferencia diara.
Podriamos agregar tambien una clase que se encarga de administrar o llevar los logs de las personas que más veces han intententado pagar un valor superior al permitido
No hay mucho riesgo porque el codigo esta correctamente estructurado siguiendo los patrones de diseño Vista-Controlador.

"""