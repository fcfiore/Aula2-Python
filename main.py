#!/usr/bin/python3

lista_de_usuarios = [
  {
    "nome": "qMHHOwoAaYECgB",
    "idade": 49,
    "email": "yMEpqGsegWXw@4linux.com",
    "sexo": "?",
    "endereco": "Rua NIbCtFYJpZtRJg"
  },
  {
    "nome": "GJBxVjGYtVEqmRasx",
    "idade": 23,
    "email": "mBZWAcaUDCVioOQEdIu@4linux.com",
    "sexo": "?",
    "endereco": "Rua VFJGPBuNRnz"
  },
  {
    "nome": "TFeiNzjMuAfyYHksx",
    "idade": 39,
    "email": "BEjDyrdxPJoniHIDFgZ@4linux.com",
    "sexo": "?",
    "endereco": "Rua AEhMBiFAuGgSAiuIyx"
  },
  {
    "nome": "EguHnoFTrUAuUUoery",
    "idade": 37,
    "email": "QzqgJRboorIzKjKp@4linux.com",
    "sexo": "?",
    "endereco": "Rua LgktJSYDjo"
  },
  {
    "nome": "zDjQIfYyTwtzetXMJvDs",
    "idade": 25,
    "email": "CZBArUyyMa@4linux.com",
    "sexo": "F",
    "endereco": "Rua DEPwqBeLgyylX"
  },
  {
    "nome": "FDLtOesbqzdqzGe",
    "idade": 47,
    "email": "MakWfrgesmuBb@4linux.com",
    "sexo": "F",
    "endereco": "Rua qVLKGbVYOPRNTdrRYA"
  },
  {
    "nome": "xrffFndgNldHhb",
    "idade": 20,
    "email": "MUvdkHayaYULCTkSDH@4linux.com",
    "sexo": "F",
    "endereco": "Rua ZwkeJCYdeZgEcX"
  },
  {
    "nome": "RyfOocoNhyuEDSN",
    "idade": 50,
    "email": "ggQNSQvIOmDqZj@4linux.com",
    "sexo": "M",
    "endereco": "Rua kvvnDojQEMsHMXzc"
  },
  {
    "nome": "GAXCbICkOjzNZxU",
    "idade": 31,
    "email": "ClNJyJMhNfmTvyQxxYvQ@4linux.com",
    "sexo": "?",
    "endereco": "Rua yIParNvhlayIcGup"
  },
  {
    "nome": "wvaTNhfqPOlnt",
    "idade": 29,
    "email": "EwTJHbRTCrfYF@4linux.com",
    "sexo": "F",
    "endereco": "Rua bGCVdBFXSzcVBeLvKYUZ"
  },
  {
    "nome": "qhDBAYlbwaSMar",
    "idade": 27,
    "email": "AwDWEkwtZcGgaHlsaW@4linux.com",
    "sexo": "M",
    "endereco": "Rua hVYSkEHTmaBIJG"
  },
  {
    "nome": "fAZzfzvEySnSei",
    "idade": 44,
    "email": "wrzgKwORTAnliywEq@4linux.com",
    "sexo": "M",
    "endereco": "Rua cSdMqmMvebnTd"
  },
  {
    "nome": "HJBLhUuMHeAogrtbeq",
    "idade": 47,
    "email": "akKkICosKJbUdVcLTCnQ@4linux.com",
    "sexo": "F",
    "endereco": "Rua IhyoOwKTUCQlBvDuVVYS"
  },
  {
    "nome": "vEeSluRuOmIJTFrgNA",
    "idade": 35,
    "email": "wrCGKAsQRlWLKUSH@4linux.com",
    "sexo": "?",
    "endereco": "Rua ZRfcRxPsJPO"
  },
  {
    "nome": "OyehQbxCsnSGPBLcviBs",
    "idade": 23,
    "email": "fnndYbeFLPmhB@4linux.com",
    "sexo": "?",
    "endereco": "Rua cnquXCCUji"
  },
  {
    "nome": "JDZdCgzulyGWW",
    "idade": 30,
    "email": "brPbOrQBWfIBikDA@4linux.com",
    "sexo": "M",
    "endereco": "Rua HgtuwqKeMin"
  },
  {
    "nome": "MoinSGxEySEgrb",
    "idade": 36,
    "email": "qolygpBXCKEeur@4linux.com",
    "sexo": "?",
    "endereco": "Rua xoVGMdTrFKHboQRzFd"
  },
  {
    "nome": "XStrcVVPyieJJznYZ",
    "idade": 49,
    "email": "doKMuRYdKwolzgkq@4linux.com",
    "sexo": "M",
    "endereco": "Rua jeTpYoJAHnSeWAUWG"
  },
  {
    "nome": "uWVZbFSfdE",
    "idade": 30,
    "email": "WpRAukMAAygh@4linux.com",
    "sexo": "?",
    "endereco": "Rua QQvsljaHXnhqjHlg"
  },
  {
    "nome": "jgVjBVFVVKui",
    "idade": 43,
    "email": "SCUVGmVBRpREfAMIleo@4linux.com",
    "sexo": "?",
    "endereco": "Rua ioMdZJPBgdMUzWsDg"
  }
]

TEMPLATE = '{nome};{idade};{email};{sexo};{endereco};'

for usuario in lista_de_usuarios:
    if usuario['idade'] > 30:
        usuario_formatado = TEMPLATE.format(
            nome=usuario['nome'],
            idade=usuario['idade'],
            email=usuario['email'],
            sexo=usuario['sexo'],
            endereco=usuario['endereco']
        )
        print(usuario_formatado)
        
exit()

# interpolação

mensagem = 'Olá {nome}, {boasVindas}'
print(mensagem.format(
    boasVindas='seja bem vindo ao mundo do Python',
    nome='Lucas'
))
print(mensagem)

mensagem = 'Olá {nome}, seja bem vindo ao mundo do Python'
mensagem = mensagem.format(nome='Lucas Ricciardi de Salles')
print(mensagem)


exit()

# 0 1 1 2 3 5 8 13 21 34
# f(n) = f(n-1) + f(n-2), se n > 1
# 1 se n <= 1

n = 5

i = 0
j = 1

for x in range(n):
    j, i = i + j, j
print(j)    # fib = j


exit()

for letra in 'Lucas Ricciardi de Salles':
    print(letra)

lista_de_numeros = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
for numero in lista_de_numeros:
    if numero % 2 == 0:
        print(numero)

exit()

print('hello, world')

nome = input('Qual é a melhor linguagem de programação: ')

if nome == 'python':
    if 5 > 10:
        print('Nunca será')
        if 343 > 199:
            print('nfdsfosd')
    else:
        print('Ae beleza')
    print('Você acertou')
    print('Lucas Ricciardi de Salles')
else:
    print('Errou :(')
    print('Derrrr')

print('ndiaoshdioashiodsa')
