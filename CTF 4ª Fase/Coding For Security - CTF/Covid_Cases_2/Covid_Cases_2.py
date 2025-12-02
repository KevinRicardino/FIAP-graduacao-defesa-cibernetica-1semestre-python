"""
Adapte seu script Python anterior para descobrir sua flag, que agora é o
número de casos de Covid-19 registrados no dia 8 de fevereiro de 2020 no
arquivo COVID-19 us-counties.

Máscara: FIAP{qtd}
"""

# Soma o número de casos do dia 08/02/2020
total_casos = 0

with open("us-counties_2.csv", "r") as arquivo:
    for linha in arquivo:
        if linha.startswith("2020-02-08"):
            # Divide a linha em colunas separadas por vírgula
            colunas = linha.strip().split(",")

            # A coluna de "cases" é a 5ª (índice 4)
            casos = int(colunas[4])

            total_casos += casos

print(f"FIAP{{{total_casos}}}")