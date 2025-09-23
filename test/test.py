import pytest
import random
from src.main import root, funcaoteste, update_estudante, delete_estudante, create_estudante, Estudante
from unittest.mock import patch


# O teste foi corrigido para usar 'await' e a asserção correta.
@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


# O teste foi corrigido para usar 'await'.
@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 12345}


# O teste foi corrigido para criar um objeto Estudante e asserir a resposta da função.
@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Paola", curso="BSI", ativo=False)
    result = await create_estudante(estudante_teste)
    assert result is not None and result.name == "Paola"


# O teste foi corrigido para usar 'await'.
@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result


# O teste foi corrigido para usar 'await'.
@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


# O teste foi corrigido para usar 'await'.
@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


# O teste foi corrigido para usar 'await'.
@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10)
    assert result
