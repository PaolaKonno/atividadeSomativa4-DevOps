from fastapi import FastAPI
app = FastAPI()

@app.get("/helloworld")
async def read_root():
    return {"Hello": "World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste" : "deu certo"}