import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel) :
    name:  str
    curso: str
    ativo: bool

@app.get("/")
def root():
    return {"status": "ok", "try": ["/helloworld", "/teste1", "/docs"]}

@app.get("/helloworld")
async def read_root():
    return {"Hello": "World"}

@app.get("/funcaoteste")

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return{"teste" : True, "num_aleatorio": random.randint(1,1000)}

@app.post("/estudantes/cadastro")
async def cadastro(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante:int):
    return id_estudante > 0

@app.delete("/estudantes/update/{id_estudante}")
async def delete_estudante(id_estudante:int):
    return id_estudante > 0

