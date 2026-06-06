import tkinter as tk
from tkinter import simpledialog, messagebox

def get_float(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    while True:
        value = simpledialog.askfloat("Input", prompt, parent=root)
        if value is None:
            # User cancelled – ask again
            continue
        return value

# Solicita o valor do troco até que seja não negativo
while True:
    dolares = get_float("Change: ")
    if dolares is not None and dolares >= 0:
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
# Also show in a message box for convenience (optional)
messagebox.showinfo("Result", f"Minimum coins: {moedas}")
