n = int(input('Digite um número inteiro: '))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print('O fator é {} e a multiplicidade é {}'.format(fator, multiplicidade))

    multiplicidade += 1
    fator += 1