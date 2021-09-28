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
        return 'Numero inválido. Digite um número positivo.'


# 2 - Crie a função tabuada()
# Na qual você informa um número e exibe a tabuada daquele numero:
# Exemplo: 2, 4, 6, 8, etc

def tabuada(numero):
    lista_resultado = []
    for count in range(11):
        resultado = int((numero)) * count
        print(f'{numero}x{count}={resultado}')
        lista_resultado.insert(count, resultado)
    return lista_resultado


if __name__ == '__main__':
    print_hi('KarlaDaiany')

    # calcular palitos de fósforo
    caixa = input(f'Digite a quantidade de caixa de fósforo: ')
    resultado = calcular_fosforos(int(caixa))
    print(f'A quantidade de palitos de fósforos é de: {resultado}')

    # calcular a tabuada
    numero = input(f'Digite o número para gerar a tabuada: ')
    print(f'### TABUADA DO {numero} ###')
    tabuada(numero)


# 3 - Crie pelo menos um teste unitário para cada uma das funções anteriores

# Testes da função calcular_fosforos
def test_calcular_fosforos():
    assert calcular_fosforos(2) == 80

def test_calcular_fosforos_decimal():
    assert calcular_fosforos(1.5) == 60

def test_calcular_fosforos_negativo():
    assert calcular_fosforos(-1) == 'Numero inválido. Digite um número positivo.'

# Teste da função tabuada
def test_tabuada():

    #Configura
    numero = 3
    resultado_esperado = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    #Executa
    resultado_atual = tabuada(3)

    #Check
    assert resultado_atual == resultado_esperado