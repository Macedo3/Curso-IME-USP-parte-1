crescente = True

anterior = float(input('Digite o 1° número: '))
valor = 1

while(crescente and valor != 0):
    valor = float(input('Digite outro número: '))
    if valor < anterior:
        crescente = False
        print('Os ultimos valores digitados foram {} e {}'.format(anterior, valor))
    else:
        continue

print('Até!')

