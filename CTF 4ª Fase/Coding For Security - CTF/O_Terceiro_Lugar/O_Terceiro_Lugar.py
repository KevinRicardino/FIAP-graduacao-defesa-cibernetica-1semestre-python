"""
O TERCEIRO LUGAR

John está indignado por ter ficado em terceiro lugar e, além
disso, por sua senha ter sido vazada.

Diante disso, desenvolva um programa em Python para encontrar
a senha de John.
"""

def extrair_terceiros_caracteres(nome_arquivo):
    """
    Lê o arquivo de texto especificado e retorna uma string contendo o
    terceiro caractere (índice 2) de cada linha.
    """
    terceiros_caracteres = ""

    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                # Remove espaços em branco e quebras de linha
                linha_limpa = linha.strip()

                # O terceiro caractere está no índice 2
                if len(linha_limpa) >= 3:
                    terceiros_caracteres += linha_limpa[2]

    except FileNotFoundError:
        print("Certifique-se de que o arquivo 'hashes.txt' está no mesmo diretório do script Python.")
        return None

    return terceiros_caracteres


# Nome do arquivo de entrada
nome_do_arquivo = 'hashes.txt'

# Execução e exibição do resultado
sequencia_resultante = extrair_terceiros_caracteres(nome_do_arquivo)

if sequencia_resultante is not None:
    print(f"✅ Sequência de Terceiros Caracteres Extraída de '{nome_do_arquivo}':")
    # A saída será: 3F7CAA3D471688B704B73E9A77B1107F
    print(sequencia_resultante)