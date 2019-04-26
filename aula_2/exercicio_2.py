
BANCO_DE_DADOS = []
BANCO_DE_DADOS.append({
    'email': 'lucas.salles@4linux.com.br',
    'idade': 25,
    'senha': 'admin'
})

class InvalidEmailError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UsuarioJaCadastradoError(Exception):
    pass

class SenhaInvalidaError(Exception):
    pass

def receber_novo_usuario():
    
    email = input('Digite seu email: ')

    if '@' not in email:
        raise InvalidEmailError
    
    idade = int(input('Digite sua idade: '))

    if idade <= 0:
        raise InvalidAgeError
        
    # retorna o usuário criado
    return {
        'email': email,
        'idade': idade,
        'senha': input('Digite sua senha: ')
    }

def cadastrar_usuario(usuario):
    for usuario_cadastrado in BANCO_DE_DADOS:
        if usuario_cadastrado['email'] == usuario['email']:
            raise UsuarioJaCadastradoError
    BANCO_DE_DADOS.append(usuario)

def verificar_senha(usuario):
    senha = input('Digite sua senha: ')
    if usuario['senha'] != senha:
        raise SenhaInvalidaError

try:
    usuario = receber_novo_usuario()
    cadastrar_usuario(usuario)
    verificar_senha(usuario)

    print('Usuário cadastrado com sucesso')

except InvalidEmailError as err:
    print('Email invalido')

except InvalidAgeError as err:
    print('Idade inválida')

except UsuarioJaCadastradoError:
    print('Usuário já cadastrado')
    
except SenhaInvalidaError:
    print('Senha inválida')
    
except ValueError as err:
    print('Erro da linguagem Python')