import json

class Usuarios():

    ARQUIVO_USUARIOS = "usuarios.json"

    def carregar_usuarios():
        try:
            with open(Usuarios.ARQUIVO_USUARIOS, "r") as f:
                return json.load(f)  
        except FileNotFoundError:
            return {} 

    def salvar_usuarios(usuarios):
        with open(Usuarios.ARQUIVO_USUARIOS, "w") as f:
            json.dump(usuarios, f, indent=4)
    
    def __init__(self, nome, tipo, senha):
        self.nome = nome
        self.tipo = tipo
        self.senha = senha

    def registro_usuario(self):
        usuarios = Usuarios.carregar_usuarios()

        self.nome = input("\nDigite seu nome:").strip()
        self.tipo = input("Aluno ou Professor:").strip().lower()
        self.senha = input("Digite sua senha de 6 números:")

        if self.tipo not in ["professor","aluno"]:
            print("Precisa ser aluno ou professor para entrar")
            return
        
        usuarios[self.nome] = [self.tipo, self.senha]
        Usuarios.salvar_usuarios(usuarios)
        print(f"Usuário registrado: \n{self.nome},{usuarios[self.nome]}")
        return True