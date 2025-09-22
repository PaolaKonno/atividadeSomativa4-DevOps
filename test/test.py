from src.main import *
from unittest.mock import patch


import pytest

from src.main import root


@pytest.mark.asyncio
async def test_root():
    assert root() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_root():
    result =  await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
# helper simples para simular criação (se tiver endpoint real, use-o no lugar)
async  def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
        assert  result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Paola", curso="DEVOPs", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result