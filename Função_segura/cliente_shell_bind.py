from socket import *

servidor = "127.0.0.1" #localhost #192.168.0.1 #10.0.0.1
porta = 5432
conexao = socket(AF_INET, SOCK_STREAM)

conexao.connect((servidor, porta))
resp = "s"

while resp == "S":
    msg_enviada = bytes(input("Qual o seu comando: "), "utf-8")
    conexao.send(msg_enviada)
    resposta = conexao.recv(1024)
    print("Dados Recebidos: ", resposta)

    resp = input("Digite S para continuar e N para terminar: ")

conexao.close()