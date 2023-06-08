import hashlib
import json
from cadastro import Usuario

def realizar_login():
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()


    def dict_to_usuario(d):
        return Usuario(**d)

    with open('cadastro.json', 'r') as arquivo:
        lista_usuarios_json = arquivo.read()
        lista_usuarios_dict = json.loads(lista_usuarios_json)
        lista_usuarios = list(map(dict_to_usuario, lista_usuarios_dict))

        for usuario in lista_usuarios:
            if login == usuario.login and senha_criptografada == usuario.senha:
                print("login feito com sucesso!")
                return usuario
        print("usuario desconhecido ;-;")