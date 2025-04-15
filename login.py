import random
from usuario import Usuarios
from funcionalidades import Funcionalidades

class Login():


    def esqueci_senha(usuarios):
        usuarios = Usuarios.carregar_usuarios()
        usuario = input("\nDigite seu nome de usuário:")

        if usuario not in usuarios:
            print("Usuário não encontrado:")
        else:
            codigo = random.randint(100000, 999999)
            print(f"Código de verificação:",codigo)
            codigo_correto = codigo
            print("\nPara trocar a senha digite o código recebido")
            verificacao = int(input("Digite o código:"))
            if verificacao == codigo_correto:
                nova_senha = input("Digite sua nova senha:")
                usuarios[usuario][1] = nova_senha
                Usuarios.salvar_usuarios(usuarios)
                print("\nSenha redefinida com sucesso!")
                Login.login(usuario)
            else:
                print("\nCódigo incorreto!")
                return Login.esqueci_senha(usuario)

    def login(usuarios):
        usuarios = Usuarios.carregar_usuarios()

        usuario = input("\nDigite seu nome igual no cadastro:").strip()
        senha = input("Digite sua senha:")

        if usuario not in usuarios:
            print("Usuário não cadastrado")
            novo_usuario = Usuarios("", "", "")
            novo_usuario.registro_usuario(usuarios)
        else:
            if senha != usuarios[usuario][1]:
                print("\nSenha incorreta")
                print("(1)Esqueci minha senha")
                print("(2)Tentar novamente")
                opçao = int(input("Digite a opção:"))
                if opçao == 1:
                    Login.esqueci_senha(usuario)
                else:
                    Login.login()
                
            else:
                print(f"Bem vindo(a),{usuario}!")
                func = Funcionalidades()

            if "professor" in usuarios[usuario]:
                print("Menu:")
                print("(1) Criar postagem")
                print("(2) Criar enquete")
                print("(3) Ver respostas enquetes")
                menu = int(input("Digite uma opção:"))
                if menu not in [1, 2, 3]:
                    print("Escolha uma opção válida")
                    return
                else:
                    if menu == 1:
                        func.criar_postagem()
                    elif menu == 2:
                        func.criar_enquete()
                    else:
                        func.respostas_enquete()
            else:
                print("Menu:")
                print("(1) Visualizar postagens")
                print("(2) Visualizar enquetes")
                menu = int(input("Digite uma opção:"))
                if menu not in [1,2]:
                    print("Escolha uma opção válida")
                    return
                else:
                    if menu == 1:
                        func.visualizar_postagens()
                    else:
                        func.visualizar_enquete()




