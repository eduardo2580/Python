from cs50 import get_string

texto = get_string("Text: ")

letras = 0
frases = 0

# Conta letras e frases
for char in texto:
    if char.isalpha():
        letras += 1
    elif char in ['.', '!', '?']:
        frases += 1

# Conta palavras separadas por espaços
palavras = len(texto.split())

# Calcular L e S, evitando divisão por zero
if palavras == 0:
    L = 0.0
    S = 0.0
else:
    L = (letras / palavras) * 100
    S = (frases / palavras) * 100

# Aplicar a fórmula Coleman-Liau
indice = 0.0588 * L - 0.296 * S - 15.8
indice_arredondado = round(indice)

# Determinar o resultado conforme o índice
if indice_arredondado >= 16:
    print("Grade 16+")
elif indice_arredondado < 1:
    print("Before Grade 1")
else:
    print(f"Grade {indice_arredondado}")
