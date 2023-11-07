##Suponha que você está criando um programa para corrigir automaticamente palavras digitadas incorretamente. Você precisa criar uma função que recebe uma frase e substitui todas as ocorrências de uma palavra mal escrita por uma versão correta. Além disso, você deve verificar se a palavra mal escrita está contida na frase original e, se não estiver, adicionar a palavra mal escrita à lista de palavras desconhecidas.

def corrigir_frase(frase, palavra_mal_escrita, palavra_correta, palavras_desconhecidas):
    if palavra_mal_escrita in frase:
        frase_corrigida = frase.replace(palavra_mal_escrita, palavra_correta)
    else:
        frase_corrigida = frase
        palavras_desconhecidas.append(palavra_mal_escrita)
    return frase_corrigida

frase_original = "Eu gosto de pyton, é uma linguagem de programação incrível."
palavra_mal_escrita = "pyton"
palavra_correta = "Python"
palavras_desconhecidas = []

frase_corrigida = corrigir_frase(frase_original, palavra_mal_escrita, palavra_correta, palavras_desconhecidas)

print("Frase original: ", frase_original)
print("Frase corrigida: ", frase_corrigida)
print("Palavras desconhecidas: ", palavras_desconhecidas)