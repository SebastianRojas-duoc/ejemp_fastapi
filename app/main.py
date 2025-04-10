
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def root():
    return{"mensaje":"hola mundo api"}

@api.get("/{id}")
def getAuto(id : int):
    autos = {
        1:{"marca" : "toyota", "modelo" : "supra"},
        2:{"marca" : "nissan", "modelo" : "v16"}
    }
    return autos.get(id)