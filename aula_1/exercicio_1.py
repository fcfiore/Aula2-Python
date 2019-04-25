
import banco

print(banco.lista_de_usuarios)

# exercício 1:
# Imprima somente os usuários 
# cujos emails contenham as letras: 
# 'a' ou 'k' ou 'm' ou 'l'
# e cujas idades sejam
# maior que 30 e menor que 40

# Dica do exercício

# Condições OU 
if 2 < 4 or 5 < 10:
  print('Condição OU')

# Condição E
if 2 < 4 and 5 < 10:
  print('Condição AND')

# Testar se um letra está em uma string
if 'c' in 'LuCaS'.lower():
  print('Lucas tem C')

# Obs: A Função lower() converte uma string
# para letra minuscula
print('LUCAS'.lower()) # Imprime 'lucas' tudo minusculo

condicao_1 = 'c' in 'Lucas'
condicao_1 = condicao_1 or 'c' in 'Ricciardi'
condicao_1 = condicao_1 or 's' in 'Salles'

condicao_2 = 20 < 40

if condicao_1 and condicao_2:
  print('opaa')


# Primeira parte
for usuario in banco.lista_de_usuarios:

  email = usuario['email'].lower()
  idade = usuario['idade']

  condicao_1 = 'a' in email
  condicao_1 = condicao_1 or 'k' in email
  condicao_1 = condicao_1 or 'm' in email
  condicao_1 = condicao_1 or 'l' in email

  condicao_2 = idade > 30 and idade < 40

  if condicao_1 and condicao_2:
    print(usuario)

# Solução 2
for usuario in banco.lista_de_usuarios:

  chave_email = 'email'
  chave_idade = 'idade'

  email = usuario[chave_email].lower()
  idade = usuario[chave_idade]

  condicao_1 = False
  letras = [ 'a', 'k', 'm', 'k' ]
  for letra in letras:
    condicao_1 = condicao_1 or letra in email
  
  condicao_2 = idade in range(30, 41)

  if condicao_1 and condicao_2:
    print(usuario)

