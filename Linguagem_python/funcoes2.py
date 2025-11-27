def somar(valor1, valor2):
    soma = valor1 + valor2
    #print(soma)
    return soma

primeiro_valor = float(input("Informe um valor: "))
segundo_valor = float(input("Informe um segundo valor: "))
#print(somar(primeiro_valor, segundo_valor))
soma = somar(primeiro_valor, segundo_valor)
media = soma/2
print(media)


