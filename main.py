from login import Login
from usuario import Usuarios

def main():
    usuarios = Usuarios.carregar_usuarios()
    Login.login(usuarios)

if __name__ == "__main__":
    main()