##utilizando os métodos de formatações de strings ensinados faça:
##Espaçando 10 caracteres a esquerda, imprima uma mensagem formatada falando seu nome e quantos anos você tem (lembrando, o nome e a idade devem estar contidos em uma variavel). 
##Em seguida transforme o valor da sua idade em número binário e veja qual caractere ele representa na tabela Unicode.

mensagem = "O meu nome é {}, eu tenho {} anos"
nome = "Mikael"
idade = 17
mensagem_formatada = mensagem.format(nome, idade)
print("{0:>10}".format(mensagem_formatada))
print("{0:>10}".format("{:b}".format(idade)))
print("{0:>10}".format("{:c}".format(idade)))

