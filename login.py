usuarios = {}

def registro_usuario():
    nome = input("Digite seu nome:").strip()

    if nome in usuarios:
        print("Usuário já cadastrado")
        return
    
    tipo = input("Aluno ou Professor:").strip().lower()

    if tipo not in ["professor","aluno"]:
        print("Precisa ser aluno ou professor para entrar")
        return

    usuarios[nome]= tipo
    print(f"Usuário registrado: {nome} como {tipo}")
    return login()

postagens = {}

def criar_postagem():

    conteudo = input("Digite o conteúdo:")
    autor = input("Nome do autor:")
    postagens[autor]=conteudo
    print("Postagem adicionada!")

def visualizar_postagens():
    if not postagens:
        print("Sem postagens disponíveis")
    else:
        post = input("Digite o nome do professor:")
        print(postagens[post])
        if post not in postagens:
            print("Professor ou título inválidos")
            return
        
def login():
    user = input("Digite seu nome igual no cadastro:").strip()

    if user not in usuarios:
        print("Usuário não cadastrado")
        registro_usuario()
    else:
        print(f"Bem vindo(a),{user}!")
        if usuarios.get(user) == "professor":
            print("Menu:")
            print("(1) Criar postagem")
            print("(2) Criar enquete")
            print("(3) Ver respostas enquetes")
            menu = int(input("Digite um número para escolher uma opção:"))
            if menu not in [1, 2, 3]:
                print("Escolha uma opção válida")
            else:
                if menu == 1:
                    criar_postagem()
                elif menu == 2:
                    print("CRIAR ENQUETE")
                else:
                    print("VER ENQUETE")
        else:
            print("Menu:")
            print("(1) Visualizar postagens")
            print("(2) Visualizar enquetes")
            menu = int(input("Digite um número para escolher uma opção:"))
            if menu not in [1,2]:
                print("Escolha uma opção válida")
            else:
                if menu == 1:
                    visualizar_postagens()
                else:
                    print("VISUALIZAR ENQUETE")
while True:
    login()

