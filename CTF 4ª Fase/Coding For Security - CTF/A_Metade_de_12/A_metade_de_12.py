"""
Construa um programa em python para revelar o
enigma contido no artefato nomes.txt.

Ao final pontue no formato de flag: FIAP{enigma}
"""

import os

def revelar_enigma():
    arquivo_alvo = 'nomes.txt'

    if not os.path.exists(arquivo_alvo):
        print(f"Erro: O arquivo '{arquivo_alvo}' não foi encontrado.")
        return

    enigma = ""

    try:
        # Usando latin-1 para evitar o erro de 'utf-8 codec'
        with open(arquivo_alvo, 'r', encoding='latin-1') as f:
            nomes = f.readlines()

            for nome in nomes:
                nome = nome.strip()  # Remove espaços e quebras de linha

                # NOVA LÓGICA:
                # 1. Filtramos apenas nomes com exatamente 12 letras
                if len(nome) == 12:
                    # 2. Pegamos a "metade" (o caractere no índice 5 ou 6)
                    # O índice 5 é a 6ª letra (exatamente a metade matemática de 12)
                    enigma += nome[5]

        print(f"Tentativa 1 (Nomes com 12 letras, índice 5):")
        print(f"FIAP{{{enigma}}}")

        # Caso a lógica acima não forme uma frase, tente esta alternativa:
        # Às vezes "A metade de 12" significa buscar nomes de tamanho 6 (12/2)
        enigma_alt = ""
        for nome in nomes:
            nome = nome.strip()
            if len(nome) == 6:
                enigma_alt += nome[0]  # Pega a primeira letra de nomes com 6 letras

        if len(enigma_alt) < 100:  # Só imprime se não for lixo gigante
            print(f"\nTentativa 2 (Nomes com 6 letras, primeira letra):")
            print(f"FIAP{{{enigma_alt}}}")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    revelar_enigma()