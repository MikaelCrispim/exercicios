print("/Exercício/")
print("""Crie um programa que realiza as seguintes operações em uma frase fornecida pelo usuário:
1. Verifica se a frase contém apenas caracteres alfanuméricos.
2. Conta quantas vezes a letra 'a' aparece na frase.
3. Converte toda a frase para minúsculas.
4. Substitui espaços em branco por underline na frase.
5. Adiciona uma palavra extra à frase.
6. Divide a frase em linhas e exibe cada linha no console.
""")

frase = input("Digite uma frase: ")

# Verifica se a frase contém apenas caracteres alfanuméricos
if frase.isalnum():
    print("A frase contém apenas caracteres alfanuméricos.")
else:
    print("A frase contém caracteres não alfanuméricos.")

# Conta quantas vezes a letra 'a' aparece na frase
contagem_a = frase.lower().count('a')
print(f"A letra 'a' aparece {contagem_a} vezes na frase.")

# Converte toda a frase para maiuscula 
frase_maiuscula = frase.upper()
print(f"Frase em minúsculas: {frase_maiuscula}")

# Substitui espaços em branco por underscores na frase
frase_formatada = frase.replace(' ', '_')
print(f"Frase formatada: {frase_formatada}")

# Adiciona uma palavra extra à frase usando append() (no contexto de listas)
palavra_extra = "Python"
frase_com_palavra_extra = frase.split()  # Converte a frase em uma lista de palavras
frase_com_palavra_extra.append(palavra_extra)
print(f"Frase com palavra extra: {frase_com_palavra_extra}")

# Divide a frase em linhas e exibe cada linha no console
linhas = frase.splitlines()
print("\nLinhas da frase:")
for numero, linha in enumerate(linhas, 1):
    print(f"{numero}: {linha}")
    