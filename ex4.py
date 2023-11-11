print("Exercício")
print("""Faça um programa que leia uma frase digitada pelo usuário e mostre na tela:
	- Calcule o comprimento total da frase;
	- Conte quantas vezes cada vogal aparece na frase;
	- Conte quantos espaços a frase teve;
	- Encontre a posição da aparição da letra "v";
	- Encontre a posição da última aparição da letra "p".
""")

print("Resolução")
frase = input("Digite uma frase: ").lower()
print(f"O comprimento total da frase é: {len(frase)}")
print(f"""A vogal 'a' apareceu: {frase.count('a')}
A vogal 'e' apareceu: {frase.count('e')}
A vogal 'i' apareceu: {frase.count('i')}
A vogal 'o' apareceu: {frase.count('o')}
A vogal 'u' apareceu: {frase.count('u')}""") #Vogais
print(f'Na frase teve: {frase.count(" ")} espaços')
print("Não foi achado nenhuma letra 'v'." if frase.find('v') == -1 else f"Foi achado a primeira aparição da letra 'v' no índice {frase.find('v')}.")
print("Não foi achado nenhuma letra 'p'." if frase.rfind('p') == -1 else f"Foi achado a última aparição da letra 'p' no indice {frase.rfind('p')}")