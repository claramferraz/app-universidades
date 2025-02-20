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
            print("Professor inválido ou sem postagens")
            return
        
enquetes = {}

def criar_enquete():
    professor = input("Digite seu nome:")
    enquete = {}
    enquetes[professor] = enquete
    num_perguntas = int(input("Digite o número de perguntas da enquete: "))

    for i in range(num_perguntas):
        pergunta = input(f"Digite o enunciado da pergunta {i + 1}: ")
        opcoes = []
        while True:
            opcao = input("Digite uma opção para a pergunta (ou 'fim' para terminar): ")
            if opcao.lower() == "fim":
                break
            opcoes.append(opcao)
        enquete[pergunta] = opcoes

    print("\nEnquete criada:")
    for pergunta, opcoes in enquete.items():
        print(f"\n{pergunta}")
        for i, opcao in enumerate(opcoes):
            print(f"{i + 1}. {opcao}")

    return enquete

respostas_alunos = {}

def visualizar_enquete():
    print(enquetes)
    enquete = input("Digite o nome do professor para acessar enquete:")

    if enquete not in enquetes:
        print("Esse professor não criou uma enquete")
    else:
        print(enquetes[enquete])
        respostas=[]
        resposta = input("Digite sua resposta para a enquete(ex: 1, 2):")
        respostas.append(resposta)
        respostas_alunos[enquete] = respostas

def respostas_enquete():
    enquete =input("Digite seu nome:")
    if enquete in respostas_alunos:
        print(respostas_alunos[enquete])
    else:
        print("Não há enquetes cadastradas para esse nome")


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
                    criar_enquete()
                else:
                    respostas_enquete()
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
                    visualizar_enquete()
while True:
    login()

