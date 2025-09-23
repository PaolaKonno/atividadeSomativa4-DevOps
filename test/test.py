import pytest
from unittest.mock import patch

from src.main import (
    root,
    funcaoteste,
    Estudante,
    create_estudante,
    update_estudante,
    delete_estudante,
)

def test_root():
    result = root()
    # root deve retornar exatamente este dict:
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

def test_create_estudante():
    estudante_teste = Estudante(name="Paola", curso="BSI", ativo=False)
    result = create_estudante(estudante_teste)
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
    # Ajuste esta asserção conforme a regra da sua função:
    # Se deletar com id>0 retorna True (comum), então:
    assert result
    # Se sua implementação retorna False mesmo em sucesso, troque para:
    # assert not result
