## LinuxApp File
## This file is used to implement code used to run scripts for Linux

from Linux import Core
from Linux import FileSystem

def Main():
    Core.VerifyFolders()
    print("="*80)
    print(">> MENU")
    print("="*80)
    print(">> 1. Criar Projeto")
    print(">> 2. Criar Nova Classe")
    print(">> 3. Listar Projetos")
    print()
    Opc = int(input(">> Escolha uma opção: "))

    if Opc == 1:
        Core.CreateProject()
    elif Opc == 2:
        FileSystem.CreateBridge()
        print("COLOCAR OUTRA FUNCAO AQUI")
    # Habilitar escolha de nome do app para o usuario
    # Colocar tudo dentro da pasta "Projetos" em "Documents"
    
Main()
