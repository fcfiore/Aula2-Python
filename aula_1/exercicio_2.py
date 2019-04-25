
# Exercício 2
# Dada uma lista de números
# escrever um algoritmo que calcula
# a média dos números nesta lista
# salvar em uma variavel e imprimir

lista_de_numeros = [ 1, 2, 3, 4, 5, 6 ]

soma = 0
tamanho = 0

for numero in lista_de_numeros:
    soma = soma + numero
    tamanho = tamanho + 1

media = soma / tamanho
print(media)