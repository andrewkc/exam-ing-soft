from fastapi import Form
from data.DB import DB, Ops
from datetime import datetime
from models.Operation import Operation

def show_contacts_(minumero: str = Form(...)) -> dict:
    print(DB)
    try:
        contacts = []
        for acc in DB:
            if acc.number == minumero:
                contacts = acc.contacts

        contacts_dict = {}
        for acc in DB:
            if acc.number in contacts:
                contacts_dict[acc.number] = acc.name
        return {
            'status_code': '200', 
            'content': contacts_dict
        }
    
    except Exception as e:
        return {
            'status_code': '404', 
            'content': str(e)
        }

def show_history_(minumero: str = Form(...)) -> dict:
    try:
        contact_dict = {}
        for acc in DB:
            if acc.number == minumero:
                contact_dict['nombre'] = acc.name
                contact_dict['saldo'] = acc.saldo
                contact_dict['operaciones'] = acc.operations

        return {
            'status_code': '200', 
            'content': contact_dict
        }

    except Exception as e:
        return {
            'status_code': '404', 
            'content': str(e)
        }

def pay_(minumero: str = Form(...), destnumero: str = Form(...), valor: str = Form(...)) -> dict:
    try:
        op = Operation(
            destNumber=destnumero,
            date=str(datetime.now()),
            value=valor
        )
        print("----------")
        print("----------")
        print(op)
        print("----------")
        Ops.append(op)
        
        for acc in DB:
            if acc.number == minumero:
                acc.saldo = acc.saldo + int(valor)
                acc.operations.append(op)

        return {
            'status_code': '200', 
            'realizado': str(op.date)
        }
    except Exception as e:
        return {
            'status_code': '404', 
            'content': str(e)
        }
