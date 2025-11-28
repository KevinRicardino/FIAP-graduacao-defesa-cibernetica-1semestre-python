import subprocess
from socket import *

servidor = "127.0.0.1" #localhost #192.168.0.1 #10.0.0.1
porta = 5432

conexao = socket(AF_INET, SOCK_STREAM)
conexao.bind((servidor, porta))
conexao.listen(2)

print("Esperando Conexão........")

resp = "S"
while True:
    con, cliente = conexao.accept()
    print("Você esta conectado com: ", cliente)

    while resp == "S":
        msg_recebida = str(con.recv(1024))
        data_string = str(msg_recebida)[2:-1]
        print("Recebemos: ", data_string)

        proc = subprocess.Popen(data_string, shell=True, stdout=subprocess.PIPE)
        data = str(proc.stdout.read())
        msg_enviada = bytes(data, "utf-8")
        con.send(msg_enviada)

        resp = input("Digite S para continuar e N para terminar: ")

    con.close()