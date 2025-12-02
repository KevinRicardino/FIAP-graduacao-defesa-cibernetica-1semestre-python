"""
O telefone +15045811112 é de um renomado restaurante, porém você
precisa descobrir a cidade onde ele se localiza. E, como você é
fera em python, prefere utilizar seu script para isso.

Sua flag é o nome da cidade onde está localizado esse restaurante.

Como exemplo, sua flag deve estar no formato FIAP{Las_Vegas}.
"""

from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers

numbers = input("Enter phone number : ")

# Localização (cidade/região)
ch_num = phonenumbers.parse(numbers, 'CH')
print("Localização:", geocoder.description_for_number(ch_num, "en"))

# Operadora (não influencia na flag, mas o script original mostrava isso)
service_num = phonenumbers.parse(numbers, "RO")
print("Carrier:", carrier.name_for_number(service_num, "en"))
