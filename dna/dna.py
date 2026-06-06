import csv
import sys


def main():
    # Verificra os argumentos da linha de comando
    if len(sys.argv) != 3:
        print("Uso: python dna.py arquivo.csv arquivo.txt")
        sys.exit(1)

    # Lêr o banco de dados CSV
    pessoas = []
    strs = []
    with open(sys.argv[1], "r") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        strs = leitor.fieldnames[1:]  # Obtém os STRs (exclui 'name')
        for linha in leitor:
            pessoas.append(linha)

    # Lêr a sequência de DNA
    with open(sys.argv[2], "r") as arquivo_dna:
        sequencia = arquivo_dna.read().strip()

    # Calcular as repetições máximas de cada STR
    contagens = {}
    for str_atual in strs:
        contagens[str_atual] = longest_match(sequencia, str_atual)

    # Verificar cada pessoa no banco de dados
    for pessoa in pessoas:
        corresponde = True
        for str_atual in strs:
            # Compara as contagens convertendo para inteiro
            if int(pessoa[str_atual]) != contagens[str_atual]:
                corresponde = False
                break
        if corresponde:
            print(pessoa["name"])
            return

    # Se nenhum perfil corresponder
    print("No match")


def longest_match(sequencia, subsequencia):
    max_repeticao = 0
    tamanho_sub = len(subsequencia)
    tamanho_seq = len(sequencia)

    for i in range(tamanho_seq):
        contagem = 0
        # Verificar repetições consecutivas a partir da posição i
        while True:
            inicio = i + contagem * tamanho_sub
            fim = inicio + tamanho_sub
            if sequencia[inicio:fim] == subsequencia:
                contagem += 1
            else:
                break
        max_repeticao = max(max_repeticao, contagem)

    return max_repeticao


if __name__ == "__main__":
    main()

# I’ve studied programming since 2018, including a technical high school in informatics and a degree in Systems Analysis and Development. I’ve done many programming courses and watched CS50 in 2023/2024. My solutions now rely only on my own knowledge, without rewatching lectures. I’m sorry I didn’t check the academic rules sooner. Thank you for understanding.
