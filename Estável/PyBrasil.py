# +----------------------------------------------------------+
# |   ________   __ ____________  ___   _____ _____ _        |
# |   | ___ \ \ / / | ___ \ ___ \/ _ \ /  ___|_   _| |       |
# |   | |_/ /\ V /  | |_/ / |_/ / /_\ \\ `--.  | | | |        |
# |   |  __/  \ /   | ___ \    /|  _  | `--. \ | | | |       |
# |   | |     | |   | |_/ / |\ \| | | |/\__/ /_| |_| |____   |
# |   \_|     \_/   \____/\_| \_\_| |_/\____/ \___/\_____/   |
# +----------------------------------------------------------+
# Design e Codígo por Guilherme Sodré/Designed and code by Guilheme Sodré|RIO DE JANEIRO - BRAZIL
#
# +----------------------------------------------------------+

print("+----------------------------------------------------------+")
print("|   ________   __ ____________  ___   _____ _____ _        |")
print("|   | ___ \ \ / / | ___ \ ___ \/ _ \ /  ___|_   _| |       |")
print("|   | |_/ /\ V /  | |_/ / |_/ / /_\ \\ `--.  | | | |        |")
print("|   |  __/  \ /   | ___ \    /|  _  | `--. \ | | | |       |")
print("|   | |     | |   | |_/ / |\ \| | | |/\__/ /_| |_| |____   |")
print("|   \_|     \_/   \____/\_| \_\_| |_/\____/ \___/\_____/   |")
print("+----------------------------------------------------------+")
print("Feito por Guilherme Sodré, 2024")

import math

#created by user #1
userdirs1 = []
userdirs1_files = []
#created by user #2
userdirs2 = []
userdirs2_files = []
#created by user #3
userdirs3 = []
userdirs3_files = []
#created by user #4
userdirs4 = []
userdirs4_files = []
#created by user #5
userdirs5 = []
userdirs5_files = []
#created by user #6
userdirs6 = []
userdirs6_files = []
#created by user #7
userdirs7 = []
userdirs7_files = []
#created by user #8
userdirs8 = []
userdirs8_files = []
#created by user #9
userdirs9 = []
userdirs9_files = []
#created by user #10
userdirs10 = []
userdirs10_files = []
#created by user #11
userdirs11 = []
userdirs11_files = []
#created by user #12
userdirs12 = []
userdirs12_files = []
#created by user #13
userdirs13 = []
userdirs13_files = []
#created by user #14
userdirs14 = []
userdirs14_files = []
#created by user #15
userdirs15 = []
userdirs15_files = []

#values
firsttime = True
loggedin = "defaultuser"
loginattempt = ""
password = ""
currentdir = "[~]"
userdirs_val = 0
userdirs = []
#files and dirs
all_dirs = ['Desktop', 'Documents', 'Downloads',]
home_dirs = ['Desktop', 'Documents', 'Downloads']
home_files = ['Hello.txt']
documents_files = []
downloads_files = []


def read_file(filename, currentdir):
    if currentdir == "[~]" and filename in home_files:
        with open(f"Home/{filename}", 'r') as file:
            content = file.read()
            print(content)
    elif currentdir == "Documents" and filename in documents_files:
        with open(f"Documents/{filename}", 'r') as file:
            content = file.read()
            print(content)
    else:
        print(f"File '{filename}' not found in the current directory.")

def write_file(filename, currentdir):
    if currentdir == "[~]":
        content = input("Enter the content you want to write: ")
        with open(f"Home/{filename}", 'w') as file:
            file.write(content)
        print(f"File '{filename}' created in Home directory.")
    elif currentdir == "Documents":
        content = input("Enter the content you want to write: ")
        with open(f"Documents/{filename}", 'w') as file:
            file.write(content)
        print(f"File '{filename}' created in Documents directory.")
    else:
        print("Cannot write a file in the current directory.")

if firsttime is True:
    print("Primeira vez detectada. Seguindo com as configurações iniciais.")
    user = input("Como devemos te chamar? ")
    while firsttime is True:
      password = input("Crie uma senha para" + user + ":")
      confirm = input("Confirme sua senha:")
      if password == confirm:
            print("Usuário" + user + " foi criado.")
            break
      else:
            print("As senhas não coincidem. Por favor tente novamente.")
firsttime = False
loggedin = user

if loggedin == user:
 print("\033[H\033[J")
 print("+----------------------------------------------------------+")
 print("|   ________   __ ____________  ___   _____ _____ _        |")
 print("|   | ___ \ \ / / | ___ \ ___ \/ _ \ /  ___|_   _| |       |")
 print("|   | |_/ /\ V /  | |_/ / |_/ / /_\ \\ `--.  | | | |        |")
 print("|   |  __/  \ /   | ___ \    /|  _  | `--. \ | | | |       |")
 print("|   | |     | |   | |_/ / |\ \| | | |/\__/ /_| |_| |____   |")
 print("|   \_|     \_/   \____/\_| \_\_| |_/\____/ \___/\_____/   |")
 print("+----------------------------------------------------------+")
 print("Feito por Guilherme Sodré, 2024")
 print("Perdido(a)? Digite help para uma lista de comandos.")

while True:
        realcommands = ["help", "cd", "exit", "read", "write", "ls", "mkdir", "rm", "rmdir", "clear", "whoami", "whereami", "cd..", "usrdir-value", "usrdir1", "usrdirs2", "usrdir3", "usrdir4", "usrdir5", "usrdir6", "usrdir7", "usrdir8", "usrdir9", "usrdir10", "usrdir11", "usrdir12", "usrdir13", "usrdir14", "usrdir15"]
        command = input(user + "@computer:" + currentdir + "$ ")
        if command in realcommands:
            success = True
        else:
            print("Comando não encontrado. Escreva 'help' para uma lista de comandos.")            
          #CD
        if command == "cd":
          currentdir = input("Qual diretório você deseja ir? ")
          if currentdir in all_dirs:
            cdsucess = True
          else:
            print("Diretoŕio não encontrado.")
            currentdir = "[~]"
            
          #CD ..
        if command =="cd..":
           currentdir = "[~]"
          #EXIT
        if command == "exit":
          sair = False
          while True:
              sure = input("Tem certeza? Essa ação encerrará a sessão atual e todos os seus arquivos e pastas. [S]/[N]")
              if sure == "s" or "S":
                 sair = True
                 break
              elif sure == "n" or "N":
                print("Tarefa cancelada.")
                break
              else:
                      print("Resposta inválida. Responda com S para 'sim' ou N para 'não'.")
          if sair:
            break
            #MKDIR
        if command == "mkdir":
          if currentdir == "[~]":
              if userdirs_val >= 0:
                  all_dirs.insert(0, input("O nome do diretório que deseja criar:"))
                  userdirs_val += 1
              elif userdirs_val == 15:
                print("Você atingiu o máximo de diretórios que podem ser criados pelo usuário(15). Para remover um diretório, use o comando rmdir")
          else:
              print("Um diretório não pode ser criado aqui.")
        #RM
        if command == "rm":
            print("To remove a file, type rm followed by the name of the file you wish to remove. Ex: rm mytext.txt")
       #RMDIR 
        #RMDIR 
        if command == "rmdir":
            remove = input("Qual diretório você deseja remover?:")   
            if remove in home_dirs:
              print("Você não pode remover os diretórios padrões.")
              
            if remove in all_dirs:
              all_dirs.remove(remove)
              userdirs_val -= 1
                       
            else:
                print(f"Diretório '{remove}' não foi encontrado.")
         #READ
        if command == "read":
          filename = input("Enter the name of the file to read: ")
          if filename in currentdir +  "_files":
            print(filename)
               
        #write
        if command == "write":
            filename = input("Enter the name of the file to write: ")
            write_file(filename, currentdir)
        #HELP
        if command == "help":
          print("Está perdido(a)? Bem vindo ao help!")
          print("-----------------------------------------------")
          print("Cd stands for 'Change Directory' and is used to change the current directory")
          print("-------------------------------------------------")
          print("Help is used to get a list of commands")
          print("-------------------------------------------------")
          print("Too much junk filled up yout screen? Clean it with clear.")
          print("-------------------------------------------------")
          print("Exit is used to exit the current session.")
          print("-------------------------------------------------")
          print("Read is used to read a file.")
          print("Write is used to create/edit/write a file.")
          print("-------------------------------------------------")
          print("'ls' stands for 'List' and is used to list the contents of the current directory.")
          print("-------------------------------------------------")
          print("'Mkdir' stands for 'Make directory' and is used to create a directory.")
          print("-------------------------------------------------")
          print("'RM' stands for 'Remove' and is used to remove a file.")
          print("-------------------------------------------------")
          print("Rmdir stands for 'Remove directory' and is used to remove a directory.")
          print("-------------------------------------------------")
          print("Whoami is used to get the name of the user current logged in")
                
        #CLEAR
        if command == "clear":
            print("\033[H\033[J")
        #WHOAMI
        if command == "whoami":
            print(user)
        #WHEREAMI
        if command == "whereami":
            print("You are at " + currentdir)

        #LS
        if command == "ls":
            if currentdir == "[~]":
              if userdirs_val == 0:
                print(home_dirs + home_files)
              else:
                print(all_dirs + home_files)
            elif currentdir == "Documentos":
                if len(documents_files) == 0:
                    print("This directory is empty.")
                else:
                    print(documents_files)
            elif currentdir == "Downloads":
                print(documents_dirs + documents_files)
            elif currentdir == userdirs1:
               print(userdirs1_files)
                
            elif currentdir == userdirs2:
              print(userdirs2_files)
              
            elif currentdir == userdirs3:
              print(userdirs3_files_)

        #USRDIR
        if command == "usrdir-value":
          print(userdirs_val)
        if command == "usrdir1":
          print(userdirs1)

        if command == "usrdir2":
          print(userdirs2)

        if command == "usrdir3":
          print(userdirs3)
        if command == "usrdir4":
          print(userdirs4)
        if command == "usrdir5":
          print(userdirs5)
        if command == "usrdir6":
          print(userdirs6)
        if command == "usrdir7":
          print(userdirs7)
        if command == "usrdir8":
          print(userdirs8)
        if command == "usrdir9":
          print(userdirs9)
        if command == "usrdir10":
          print(userdirs10)
        if command == "usrdir11":
          print(userdirs11)
        if command == "usrdir12":
          print(userdirs12)
        if command == "usrdir13":
          print(userdirs13)
        if command == "usrdir14":
          print(userdirs14)
        if command == "usrdir15":
          print(userdirs15)


