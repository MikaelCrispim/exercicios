# # Suponha que você tenha uma lista com informações de detentos em uma delegacia. 
# # Crie um programa que aceita uma lista de nomes, idade e artigo criminalista, em seguida, exibe a lista alinhada à esquerda, 
# # à direita e centralizada em colunas com largura fixa e usando os metodos de quebra e separação de string
# #para separa as informações.
# #Exercico usando o posicionamento, quebra e separação de string:
# #Dados em forma de string com nomes e idades e artigo crimianlista separados por vírgula

dados = "Paulo,16,157\nCesar,52,155\nRian,30,155\nMikael,20,157\nXarelli,17,171"
#Quebra os dados em linhas usando splitlines()
linhas = dados.splitlines()

print("-" * 60)
print("Lista com as informações: \nNome | Idade | Artigo Criminalista")
print("-" * 60)

for linha in linhas:
    # Separar cada linha em nome,idade e artigo criminalista usando split.
    nome, idade, artigo = linha.split(',')

#Formata e exibe as informações centralizando o nome e alinhando a idade à direita
    print(f"Nome: {nome.ljust(10)} | Idade: {idade.center(7)} | Artigo Criminalista: {artigo.rjust(2)}")

print("-" * 60)