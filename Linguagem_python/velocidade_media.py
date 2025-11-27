#Pedir a distância da viagem
distancia = float(input("Por favor, digite a distância percorrida: "))

#Pedir o tempo da viagem
tempo = float(input("Por favor, informe o tempo necessário para a viagem: "))

#Dividir a distância da viagem
velocidade_media = distancia / tempo

#Exibir o resultado para o usuário
print("A velocidade média foi de {:.2f} km/h".format(velocidade_media))
print(f"A velocidade média foi de {velocidade_media:.2f} km/h")