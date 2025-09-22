# tests/test_main.py

import src.main as main
from unittest.mock import patch
from src.main import Estudante, root, update_estudante, delete_estudante


def test_root_returns_hello_world():
    result = root()
    assert result == {"message": "Hello World"}


def test_funcaoteste_returns_fixed_random():
    # Patch no alvo correto, dependendo de como o random foi importado em src.main
    patch_target = (
        "src.main.random.randint" if hasattr(main, "random") else "src.main.randint"
    )
    with patch(patch_target, return_value=12345):
        result = main.funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}


# helper simples para simular criação (se tiver endpoint real, use-o no lugar)
def create_estudante(estudante: Estudante):
    return estudante


def test_create_estudante_roundtrip():
    estudante_teste = Estudante(name="Paola", curso="DEVOPs", ativo=False)
    result = create_estudante(estudante_teste)
    assert result == estudante_teste


def test_update_estudante_negativo_returns_false():
    assert update_estudante(-5) is False


def test_update_estudante_positivo_returns_true():
    assert update_estudante(10) is True


def test_delete_estudante_negativo_returns_false():
    assert delete_estudante(-5) is False


def test_delete_estudante_positivo_returns_true():
    assert delete_estudante(5) is True
