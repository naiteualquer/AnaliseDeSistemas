#TODO:Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário
# qual operação ele deseja realizar: adição (+),
# subtração (-), multiplicação (*) ou divisão
# (/). Exiba na tela o resultado da operação desejada

print('CALCULADORA')
print('+')
print('-')
print('/')
print('*')

numA = float(input('digite o primeiro número:'))
numB = float(input('digite o segundo número: '))
oper = input('qual operação deseja fazer: ')

if oper == '+':
    print(numA + numB)
if oper == '-':
    print(numA - numB)
if oper == "/":
    print(numA / numB)
else:
    print(numA * numB)


