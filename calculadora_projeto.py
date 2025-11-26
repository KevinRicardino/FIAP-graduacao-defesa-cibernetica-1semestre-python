#import calculadora_funcoes
#from calculadora_funcoes import somar, subtrair, dividir, multiplicar
from calculadora_funcoes import *

op = -1
while (op != 5):
    print("1 - somar dois valores")
    print("2 - subtrair dois valores")
    print("3 - dividir dois valores")
    print("4 - Multiplicar dois valores")
    print("5 - Sair")
    op = int(input("Digite a sua opção! "))

    if op == 1:
        print(somar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 2:
        print(subtrair(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 3:
        print(dividir(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 4:
        print(multiplicar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 5:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente!")