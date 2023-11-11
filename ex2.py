# Exercício: Manipulação de Strings

# 1. Substituição de String
# a) Crie uma variável chamada 'frase' e atribua a ela a seguinte frase: "Eu gosto de programar em [linguagem]."
# b) Utilize o método de substituição para substituir "[linguagem]" pelo nome de uma linguagem de programação de sua escolha.
# c) Imprima a frase modificada.

# 2. Strings Personalizadas
# a) Crie duas variáveis: 'nome' e 'idade', atribuindo seu nome e idade a essas variáveis, respectivamente.
# b) Crie uma string personalizada que inclua seu nome e idade. Por exemplo, "Meu nome é [nome] e eu tenho [idade] anos."
# c) Imprima a string personalizada.

# Solução:

# 1. Substituição de String
frase = "Eu gosto de programar em [linguagem]."
linguagem_programacao = "Python"
frase_modificada = frase.replace("[linguagem]", linguagem_programacao)
print("1. Substituição de String:")
print(frase_modificada)
print()

# 2. Strings Personalizadas
nome = "SeuNome"
idade = 25
string_personalizada = f"Meu nome é {nome} e eu tenho {idade} anos."
print("2. Strings Personalizadas:")
print(string_personalizada)