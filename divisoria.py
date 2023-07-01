import pyperclip

def criar_divisoria(frase):
    tamanho_total = 40  # Tamanho total da divisória
    tamanho_frase = len(frase)
    tamanho_linha = (tamanho_total - tamanho_frase - 2) // 2  # -2 para considerar os espaços antes e depois da frase
    linha = '-' * tamanho_linha
    divisoria = f"# {linha} {frase} {linha} #"
    if len(divisoria) < tamanho_total:
        divisoria += '-' * (tamanho_total - len(divisoria))  # Preenche o restante com '-'
    return divisoria

# Solicita a frase do usuário
frase = input("Digite a frase para a divisória: ")

# Cria a divisória
divisoria = criar_divisoria(frase)

# Copia a divisória para o clipboard
#pyperclip.copy(divisoria)

# Imprime a divisória
print(divisoria)