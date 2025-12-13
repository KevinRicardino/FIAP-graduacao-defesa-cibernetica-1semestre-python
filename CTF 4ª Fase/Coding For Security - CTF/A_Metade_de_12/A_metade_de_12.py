"""
Construa um programa em python para revelar o
enigma contido no artefato nomes.txt.

Ao final pontue no formato de flag: FIAP{enigma}
"""

import os

def revelar_enigma():
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    arquivo_alvo = os.path.join(pasta_script, 'nomes.txt')

    if not os.path.exists(arquivo_alvo):
        print(f"Erro: O arquivo '{arquivo_alvo}' não foi encontrado.")
        return

    enigma = ""

    try:
        with open(arquivo_alvo, 'r', encoding='latin-1') as f:
            nomes = f.readlines()

        for nome in nomes:
            nome = nome.strip()
            if len(nome) == 12:
                enigma += nome[5]

        print("Tentativa 1:")
        print(f"FIAP{{{enigma}}}")

        enigma_alt = ""
        for nome in nomes:
            nome = nome.strip()
            if len(nome) == 6:
                enigma_alt += nome[0]

        if len(enigma_alt) < 100:
            print("\nTentativa 2:")
            print(f"FIAP{{{enigma_alt}}}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    revelar_enigma()
