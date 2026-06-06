from cs50 import get_float

# Solicita o valor do troco até que seja não negativo
while True:
    dolares = get_float("Change: ")
    if dolares >= 0:
        break

# Converte dólares para centavos (arredondado)
centavos = round(dolares * 100)

# Calcula o número de moedas
moedas = 0

# Quarters
moedas += centavos // 25
centavos %= 25

# Dimes
moedas += centavos // 10
centavos %= 10

# Nickels
moedas += centavos // 5
centavos %= 5

# Pennies
moedas += centavos

# Exibe o resultado
print(moedas)
