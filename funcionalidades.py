from usuario import Usuarios

class Funcionalidades(Usuarios):
    postagens = {}
    enquetes = {}
    respostas_alunos = {}

    def criar_postagem(self, autor):
        conteudo = input("Digite o conteúdo:")
        self.postagens[autor] = conteudo
        print("Postagem adicionada!")
       
        self.menu_retorno()

    def visualizar_postagens(self):
        if not self.postagens:
            print("Sem postagens disponíveis")
        else:
            post = input("Digite o nome do professor:")
            if post in self.postagens:
                print(self.postagens[post])
            else:
                print("Professor ou título inválidos")

        self.menu_retorno()       

    def criar_enquete(self, professor):
        enquete = {}
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

        self.enquetes[professor] = enquete
        print("\nEnquete criada:")
        for pergunta, opcoes in enquete.items():
            print(f"\n{pergunta}")
            for i, opcao in enumerate(opcoes):
                print(f"{i + 1}. {opcao}")

        self.menu_retorno()

    def visualizar_enquete(self):
        print("Enquetes disponíveis:", list(self.enquetes.keys()))
        professor = input("Digite o nome do professor para acessar enquete:")

        if professor not in self.enquetes:
            print("Esse professor não criou uma enquete")
        else:
            print(self.enquetes[professor])
            resposta = input("Digite sua resposta para a enquete(ex: 1, 2):")
            if professor not in self.respostas_alunos:
                self.respostas_alunos[professor] = []
            self.respostas_alunos[professor].append(resposta)
        
        self.menu_retorno()

    def respostas_enquete(self):
        professor =input("Digite seu nome:")
        if professor in self.respostas_alunos:
            print("Respostas:", self.respostas_alunos[professor])
        else:
            print("Não há enquetes cadastradas para esse nome")
        
        self.menu_retorno()

    def menu_retorno(self):
        print("\n(1) Menu principal")
        print("(2) Sair")
        opcao = input("Digite para onde quer ir:")
        if opcao == "1":
            from login import Login
            usuarios = Usuarios.carregar_usuarios()
            Login.login(usuarios)
        else:
            exit()