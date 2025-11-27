# Função de soma
def somar(a:float, b:float):
    return float(a) + float(b)

# Função de subtração
def subtrair(a:float, b:float):
    return float(a) - float(b)

# Função de divisão
def dividir(a:float, b:float):
    if b == 0:
        return 0
    return float(a) / float(b)

# Função de multiplicar
def multiplicar(a:float, b:float):
    return float(a) * float(b)
