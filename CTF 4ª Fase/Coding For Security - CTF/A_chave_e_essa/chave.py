"""
Título: A chave é essa

Você recebeu a missão de descobrir a senha de um sistema legado da 
empresa que ninguém lembra.

Para isso, você deve utilizar uma chave para gerar a hash em md5, 
que é justamente a senha que você está procurando.

Sua flag é essa hash.
"""

import hashlib,binascii
nome = input('Insira a chave: ')
hash = hashlib.new('md5', nome.encode('utf-8')).digest()
print ("O hash gerado é: ", binascii.hexlify(hash))