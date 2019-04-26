
while True:

  try:
    soma, tamanho = 0, 0

    arquivo = open('argumentos.txt', 'r')
    for numero in arquivo.readlines():
      soma += int(numero)
      tamanho += 1

    media = soma / tamanho
    print(media)

  except KeyboardInterrupt:
    print('hahahahahaja')