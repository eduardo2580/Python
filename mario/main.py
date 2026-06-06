from cs50 import get_int

# Solicita a altura até que seja válida
while True:
    altura = get_int("Height:  ")
    if 1 <= altura <= 8:
        break

# Constrói a pirâmide
for linha in range(1, altura + 1):
    print(" " * (altura - linha) + "#" * linha)
