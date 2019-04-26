

def receber_idade():
    idade = input('Digite a sua idade: ')
    idade = int(idade)
    if idade <= 0:
        raise Exception('idade menor do que zero')
    return idade

def imprimir_idade(idade):
    print('Você disse que tem {} anos.'.format(idade))

# fluxo feliz
try:
    idade = receber_idade()
    imprimir_idade(idade)
except ValueError:
    print('Voce digitou um caracter invalido')
except Exception as err:
    print(err)

exit()

# fluxo feliz
idade = input('Digite a sua idade: ')

# aqui entra a validação de caracter nao numerico
for letra in idade:
  if letra not in '0123456789':
    print('Caracter invalido')
    exit()

# aqui entra a validaçao se numero negativo
if int(idade) < 0:
  print('Numero negativo')
  exit()


# aqui entra a validacao de numero muito
if int(idade) > 100:
  print('Voce nao pode existir')
  exit()

idade = int()
