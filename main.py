from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/helloworld")
async def read_root():
    return {"Hello": "World"}

@app.get("/funcaoteste")

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return{"teste" : True, "num_aleatorio": random.randint(1,1000)}