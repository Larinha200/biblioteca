from funcao import *
from  classes import *

livros = {}

while True:
    menu()
    resp = int(input("--->"))

    if resp == 1:
        ls()
        cadastro(Livros, livros)

    if resp == 2:
        ls()
        listar(livros)
        pass

    if resp == 3:
        pass

    if resp == 4:
        pass

    if resp == 5:
        pass

    if resp == 6: 
        pass

    if resp == 0:
        ls()
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")