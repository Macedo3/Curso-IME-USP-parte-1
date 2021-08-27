import math


def numero_binomial(n, k):
    print(math.factorial(n) / math.factorial(k) * (math.factorial(n - k)))

numero_binomial(10, 2)

def teste_numeroBino():
    if math.factorial(5) / math.factorial(2) * math.factorial(5 - 2) == 10:
        print('Binomial de 5 por 2 está funcionando.')
    else:
        print('Binomial de 5 por 2 não está funcioando.')
    if math.factorial(5) / math.factorial(0) * math.factorial(5 - 0) == 1:
        print('Binomial de 5 por 0 está funcionando.')
    else:
        print('Binomial de 5 por 0 não está funcioando.')
    if math.factorial(20) / math.factorial(0) * math.factorial(20 - 0) == 1:
        print('Binomial de 20 por 0 está funcionando.')
    else:
        print('Binomial de 20 por 0 não está funcioando.')