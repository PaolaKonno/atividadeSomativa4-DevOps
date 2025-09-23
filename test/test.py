from src.main import *
from unittest.mock import patch

def test_create_estudante():
    estudante_teste = Estudante(name= "Paola", curso= "Curso 1", ativo=False)
    assert estudante_teste == create_estudante(estudante_teste)

async def test_create_estudante():
    def test_root():
        assert root() == {"message": "Hello World"}

async def test_funcaoteste():
    assert funcaoteste() == {"teste" : True, "num_aleatorio": random.randint(1,1000)}
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

async def cadastro(estudante: Estudante):
    return estudante

async def teste_update_estudante_negativo():
    assert not update_estudante(-5)


async def teste_update_estudante_positivo():
    assert update_estudante(5)

async def teste_delete_estudante_negativo():
    assert not delete_estudante(-5)

async def teste_delete_estudante_positivo():
    assert  delete_estudante(5)

class Estudante(BaseModel) :
    name:  str
    curso: str
    ativo: bool