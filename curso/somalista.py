def soma_elementos(list):
    soma = 0
    for i in list:
        soma += i
    return soma

lista = [1, 2, 3, 4, 5, 6]
print(soma_elementos(lista))