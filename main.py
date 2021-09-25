import pytest

def print_hi(name):
    print(f'Oi, {name}')


# 1 - Crie a função calcular_fosforos()
# Na qual o usuário informa o número de caixas de fósforos, o script multiplica por 40 e informa o número de palitos.
# Exemplo: 1 = 40, 2 = 80, etc

def calcular_fosforos(caixa):
    if caixa > 0:
        return caixa * 40
    else:
        return 0


# 2 - Crie a função tabuada()
# Na qual você informa um número e exibe a tabuada daquele numero:
# Exemplo: 2, 4, 6, 8, etc

def tabuada(numero,vezes):
    for qtde in range(vezes):
        resultado = numero * qtde
        print(f'{numero}x{qtde}={resultado}')


if __name__ == '__main__':
    print_hi('KarlaDaiany')

# calcular palitos de fósforo
resultado = calcular_fosforos(3)
print(f'A quantidade de palitos de fósforos é de: {resultado}')

# calcular a tabuada
tabuada(3,11)


# 3 - Crie pelo menos um teste unitário para cada uma das funções anteriores

# Testes da função calcular_fosforos
def test_calcular_fosforos():
    assert calcular_fosforos(2) == 80

def test_calcular_fosforos_decimal():
    assert calcular_fosforos(1.5) == 60

def test_calcular_fosforos_negativo():
    assert calcular_fosforos(-1) == 0

# Teste da função tabuada
def test_tabuada():                         #Teste BUGADO! FALSO POSITIVO! VALIDAR!!!
    assert tabuada(2,3) == print(0,2,4)