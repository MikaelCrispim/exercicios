# Exercício: Manipulação de Strings

# Substituição de String
# a) Crie uma variável chamada 'frase' e atribua a ela a seguinte frase: "Eu gosto de programar em [linguagem]."
# b) Utilize o método de substituição para substituir "[linguagem]" pelo nome de uma linguagem de programação de sua escolha.
# c) Imprima a frase modificada.

# Solução:

# 1. Substituição de String
frase = "Eu gosto de programar em [linguagem]."
linguagem_programacao = "Python"
frase_modificada = frase.replace("[linguagem]", linguagem_programacao)
print("1. Substituição de String:")
print(frase_modificada)
print()