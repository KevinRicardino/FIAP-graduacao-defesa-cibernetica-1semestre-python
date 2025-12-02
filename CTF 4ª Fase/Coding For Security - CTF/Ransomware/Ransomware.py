"""
Após pagar o resgate ao atacante, você recebeu um script em python
que faz a descriptografia da imagem anexa. O problema é que o código
veio incompleto! Corrija-o, rode o script, e abra a imagem para
descobrir o número que aparece na foto, que é sua flag.

Chave para descriptografia: 0143256879fravtr
"""

from Crypto.Cipher import AES
from Crypto.Util import Counter

# chave usada na descriptografia
key = b"0143256879fravtr"

# contador igual ao usado pelo pyaes (CTR inicia em 1)
ctr = Counter.new(
    128,          # tamanho do bloco em bits
    initial_value=1,    # contador começa em 1
    little_endian=False # big-endian, igual pyaes
)

# abre o arquivo criptografado
with open("ctfoto.pyransom", "rb") as f:
    data = f.read()

# cria o objeto de descriptografia AES-CTR
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

# realiza a descriptografia
decrypted = cipher.decrypt(data)

# salva a imagem final
with open("ctfoto_decrypted.jpg", "wb") as f:
    f.write(decrypted)
