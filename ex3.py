# Exercício Matheus Silva:
# Imagine que você está desenvolvendo um programa de registro de usuários. Você recebe uma entrada do usuário para o nome e deseja validar se o nome fornecido é adequado para o registro. Crie uma função chamada "validar_nome" que recebe um nome como parâmetro e implementa as seguintes verificações:
# Remove os espaços em branco do início e do final da string.
# Verifica se o nome contém apenas letras ou números (não deve conter espaços, pontuações ou outros caracteres especiais).
# Retorna verdadeiro se o nome passar por todas as verificações e falso caso contrário.
# Possível resposta:
def validar_nome(nome):
    nome_sem_espacos = nome.strip()  # Remove espaços em branco do início e do final

    if nome_sem_espacos.isalnum():  # Verifica se contém apenas letras ou números
        return True
    else:
        return False
##Exemplo de uso da função
nome_usuario = input("Digite seu nome: ")
if validar_nome(nome_usuario):
    print("Nome válido! Registro bem-sucedido.")
else:
    print("Nome inválido! Por favor, insira apenas letras ou números, sem espaços ou caracteres especiais.")