"""
O código foi feito para geração de uma flag, porém antes, você deverá corrigi-lo.
"""

FIAP = [
    "python", "programação", "desafio", "criptografia", "segurança",
    "openai", "base64", "algoritmo", "inteligência", "artificial",
    "computação", "cifra", "cesar", "decodificação", "chave",
    "codificação", "criptografar", "decifrar", "encriptar", "decriptar",
    "algoritmo", "binário", "hexadecimal", "octal", "mensagem",
    "texto", "dados", "informação", "privacidade", "segredo"
]

palavras = FIAP

set_palavra = palavras[2]        # "desafio"
segunda_especifica = "FIAP"

terceira_palavra = set_palavra
palavra_especifica = segunda_especifica

frase_formada = f"{terceira_palavra}{palavra_especifica}"

flag = f"FIAP{{{frase_formada}}}"
print("Frase formada:", flag)


