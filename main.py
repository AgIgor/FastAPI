from typing import Union
from fastapi import FastAPI
import datetime

app = FastAPI()

vendas = {
    1: {"item": "lata",
        "preco_unitario": 4.00,
        "qunatidade": 5
        },

    2: {"item": "garrafa",
        "preco_unitario": 9.00,
        "qunatidade": 8
        },

    3: {"item": "garrafa 750ml",
        "preco_unitario": 3.00,
        "qunatidade": 3
        },

    4: {"item": "lata mini",
        "preco_unitario": 4.00,
        "qunatidade": 5
        },
}

@app.get("/")
def read_root():
    return {"Olá mundo"}

@app.get("/time")
def time():
    return datetime.datetime.now()

@app.get("/items")
def items():
    return vendas.items()

# @app.get("/update/{key}/{val}")
# def items(key:str,val:str):
#     igor.update({key:val})
#     print(igor)
#     return igor.items()
#
# @app.get("/vendas/{id}/{name}")
# def saida(id=None,name=None):
#     return users[id][name]
#
# @app.get("/itens/{item_id}")
# def read_item(item_id: int):
#     return {"item_id":item_id}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# uvicorn main:app --reload