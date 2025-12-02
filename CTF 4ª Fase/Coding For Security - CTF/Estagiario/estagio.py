"""
Você está treinando um estagiário em defesa cibernética para
construir scripts em Python que facilitem o reconhecimento de alvos.

Ele criou um script, mas ele contém vários erros.

Você poderia corrigi-los para ele? O estagiário precisa do script
correto para obter uma flag.
"""

import os

def generate_secret_agent():

    # Lê o arquivo corretamente
    with open("wordlist.txt", "r") as file:
        words = file.read().splitlines()

    # Remove espaços extra
    words = [word.strip() for word in words]

    # Índices fornecidos
    indices = [0, 2, 10, 2, 3, 14, 19]

    # Monta as letras conforme a regra
    letters = [
        (words[i][0] if idx % 2 == 0 else words[i][-1])
        for idx, i in enumerate(indices)
    ]

    # Junta tudo numa string
    secret_agent = "".join(letters)

    return secret_agent


# Gera o valor final
secret_agent = generate_secret_agent()

# Comando curl usando o User-Agent
curl_command = f'curl -A "{secret_agent}" http://161.35.250.58/secreto/'

# Executa o comando
os.system(curl_command)
