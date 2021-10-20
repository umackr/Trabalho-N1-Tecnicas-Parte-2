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

def exibirPorNome(listaDeUsuarios):
    print("Usuarios cadastrados (Ordem Alfabetica):\n")
    for usuarios in sorted(listaDeUsuarios):
        print("NOME:",usuarios,"\tE-MAIL:",listaDeUsuarios[usuarios])
    input("\nPressione ENTER para continuar")
    clearConsole()

def verificarUsuario(listaDeUsuarios):
    nome = str(input("Qual usuario você gostaria de verificar?\n"))
    clearConsole()
    if nome in listaDeUsuarios:
        print(nome, "se encontra na lista de usuarios.\n")
        print("NOME:",nome,"\tE-MAIL:",listaDeUsuarios[nome])
        input("\nPressione ENTER para continuar")
        clearConsole()
        return
    else:
        print(nome, "não se encontra na lista de usuarios")
        input("\nPressione ENTER para continuar")
    clearConsole()

def removerUsuario(listaDeUsuarios):
    email = str(input("Insira o e-mail do usuario que você gostaria de remover?\n"))
    clearConsole()

    while True:
        for usuario in listaDeUsuarios:

            if listaDeUsuarios[usuario] == email:
                print("NOME:",usuario,"\tE-MAIL:",listaDeUsuarios[usuario],"\n")
                escolha = int(input("Você realmente quer deletar o usuario acima? \n1 - Sim \n2 - Não\n"))
                clearConsole()

                if escolha == 1:
                    del listaDeUsuarios[usuario] 
                    print("Usuario deletado com sucesso!\n")
                    sleep(1)
                    clearConsole()
                    return
                elif escolha == 2:
                    escolha = input("1 - Remover outro usuario \n\nPressione ENTER para sair\n")
                    if escolha == "1":
                        clearConsole()
                        return removerUsuario(listaDeUsuarios)
                    else: 
                        clearConsole()
                        return
                else: print("Valor invalido, tente novamente\n")
            else:print("E-MAIL não cadastrado")
        sleep(2)
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
        elif opçao == 3: exibirPorNome(listaDeUsuarios)
        elif opçao == 4: verificarUsuario(listaDeUsuarios)
        elif opçao == 5: removerUsuario(listaDeUsuarios)
        elif opçao == 6: print("teste")
        elif opçao == 7: return




if __name__ == "__main__":
    main()