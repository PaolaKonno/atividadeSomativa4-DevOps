import src.main as m
from unittest.mock import patch


import pytest

from src.main import root

def test_root():
    assert m.root() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_root():
    result =  await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
# helper simples para simular criação (se tiver endpoint real, use-o no lugar)
async  def test_funcaoteste():
    with patch('src.main.random.randint', return_value=12345):
        assert  m.funcaoteste() == {"teste:":True, "num_aleatorio":12345}

@pytest.mark.asyncio
async def test_create_estudante():
    est = m.Estudante(name="Paola", curso="DEVOPs", ativo=False)
    assert m.create_estudante(est) == est

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    assert m.update_estudante(-5) is False

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    assert m.update_estudante(10) is True

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    assert m.delete_estudante(-5) is False

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    assert m.delete_estudante(5) is True