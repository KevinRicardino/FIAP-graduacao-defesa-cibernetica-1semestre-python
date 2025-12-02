"""
A terceira letra de tudo aquilo que for falso poderá lhe garantir a "flag".

Crie um programa em python e tente decifrar este enigma.
"""

# abre o arquivo passwd
with open("passwd", "r") as f:
    lines = f.read().splitlines()

flag_letters = []

for line in lines:
    if not line.strip():  # ignora linhas vazias
        continue

    parts = line.split(":")
    username = parts[0]
    shell = parts[-1]

    if shell in ["/usr/bin/false", "/usr/sbin/false"]:
        # pega a terceira letra do username
        if len(username) >= 3:
            flag_letters.append(username[2])

# monta a flag
flag = "".join(flag_letters)
print("Flag:", flag)
