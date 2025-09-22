from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio

from src.main import root

def test_root_returns_hello_world():
    assert root() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_root():
    result =  await root()
    yield result
    assert result == {"message": "Hello World"}



@pytest.mark.asyncio
# helper simples para simular criação (se tiver endpoint real, use-o no lugar)
async  def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
        yield result

        assert  result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Paola", curso="DEVOPs", ativo=False)
    result = await create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    yield result
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    yield result
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    yield result
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    yield result
    assert result