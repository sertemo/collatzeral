import pytest
import collatz

def test_generador_correcto():
    col = collatz.Collatz()
    assert list(col._generador(10)) == [10, 5, 16, 8, 4, 2, 1]
