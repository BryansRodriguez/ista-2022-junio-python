from operaciones import sumar, multiplicar

def test_suma():
    assert sumar(2, 2) == 4

def test_suma_negativo():
    assert sumar(-2, 2) == 0

def test_evaluar_multiplicacion_por_uno():
    assert multiplicar(1, 4) == 4

def test_evaluar_multiplicar_diferentes():
    assert multiplicar(2, 3) == 6

def test_evaluar_multiplicar_cero():
    assert multiplicar(0, 5) == 0

def test_integracion_mulplicacion_y_suma():
    """(2 + 3) * 4 = 20"""
    multiplicar(sumar(2, 3), 4) == 20