from hola import saludar

def test_saludar():
    resultado = saludar("Ana")
    assert "Ana" in resultado
    assert "Hola" in resultado
    assert len(resultado) > 0

def test_saludar_diferentes_nombres():
    resultado1 = saludar("Pedro")
    resultado2 = saludar("Maria")
    assert "Pedro" in resultado1
    assert "Maria" in resultado2
    assert len(resultado1) > 0
    assert len(resultado2) > 0

def test_saludar_formato():
    resultado = saludar("Juan")
    assert "¡Hola, Juan! ¿Cómo estás?" == resultado
