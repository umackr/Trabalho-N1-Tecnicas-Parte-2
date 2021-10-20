from io import open_code
import os
from typing import Optional
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
from time import sleep

def cadastrarUsuario(listaDeUsuarios):
    nome = str(input("Insira o nome do usuario.\n")).lower()
    email = str(input("\nInsira o e-mail do usuario.\n")).lower()

    listaDeUsuarios[nome] = email
    clearConsole()
    print("Usuario cadastrado com sucesso!")
    sleep(1)
    clearConsole()
    return listaDeUsuarios

def exibirUsuarios(listaDeUsuarios):
    print("Usuarios cadastrados (Ordem de Cadastro):\n")
    for usuarios in listaDeUsuarios:
        print("NOME:",usuarios,"\tE-MAIL:",listaDeUsuarios[usuarios])
    input("\nPressione ENTER para continuar")
    clearConsole()

def menu():
    print("-------------MENU---------------")
    print("1 - Cadastrar usuario")
    print("2 - Exibir usuarios (Cadastro)")
    print("3 - Exibir usuarios (Alfabetica)")
    print("4 - Verificar usuario")
    print("5 - Remover cadastro")
    print("6 - Renomear usuario")
    print("7 - Sair")

def main():
    listaDeUsuarios = {}
    opçao = 1

    while True:
        menu()
        opçao = int(input("-------Escolha uma opção--------\n"))
        clearConsole()
        if opçao == 1: cadastrarUsuario(listaDeUsuarios)
        elif opçao == 2: exibirUsuarios(listaDeUsuarios)
        elif opçao == 3: print("teste")
        elif opçao == 4: print("teste")
        elif opçao == 5: print("teste")
        elif opçao == 6: print("teste")
        elif opçao == 7: return


if __name__ == "__main__":
    main()