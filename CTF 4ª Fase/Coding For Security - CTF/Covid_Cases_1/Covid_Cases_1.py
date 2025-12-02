"""
Crie um script em Python que retorne a quantidade de linhas referentes
ao dia 27 de setembro de 2021 no arquivo COVID-19 us-counties.csv

O retorno da quantidade de linhas é a flag deste CTF.

Máscara: FIAP{qtd}
"""

# Conta linhas do arquivo us-counties.csv do dia 27/09/2021
contador = 0

# Arquivo deve estar no mesmo diretório do script:
with open("us-counties.csv", "r") as arquivo:
    for linha in arquivo:
        if linha.startswith("2021-09-27"):
            contador += 1

print(f"FIAP{{{contador}}}")