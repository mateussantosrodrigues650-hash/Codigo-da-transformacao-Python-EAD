usuarios_db = {
    "admin": "1234",
    "joao": "python2026",
    "maria": "senha123"
}

def validar_login(usuario, senha):
    if usuario in usuarios_db and usuarios_db[usuario] == senha:
        return True
    return False

user_input = input("Usuário: ")
pass_input = input("Senha: ")

if validar_login(user_input, pass_input):
    print("Login realizado com sucesso! Bem-vindo(a).")
else:
    print("Usuário ou senha incorretos.")