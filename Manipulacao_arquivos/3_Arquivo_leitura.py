with open("primeiro_arquivo.txt", "r") as arquivo:
    #conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)