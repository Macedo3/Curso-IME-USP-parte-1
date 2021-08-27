decrescente = True

anterior = int(input('Digite o 1° número: '))
valor =  1

while(decrescente and valor != 0):
    valor = int(input('Digite outro valor: '))
    if valor > anterior:
        decrescente = False
    anterior = valor

if(decrescente):
    print('Está em ordem decrescente!')

else:
    print('Não está em ordem decrescente.')

