
import banco

TOLERANCIA = 35

acertos = 0

while acertos < 3:

    for usuario in banco.lista_de_usuarios:
        idade = usuario['idade']
        numero = input('Tente adivinhar a idade {}: '.format(usuario['idade']))
        numero = int(numero)
        if numero in range(idade - TOLERANCIA, idade + TOLERANCIA):
            acertos = acertos + 1
            print('Voce já acertou: ' + str(acertos))
            if acertos == 3:
                break
print('Ganhou o jogo')