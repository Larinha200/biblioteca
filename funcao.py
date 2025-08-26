import os 
from classes import *

def ls():
    os.system('pause')
    os.system('cls')

def menu():
    print("\nOlá, seja bem-vindo(a) a nossa biblioteca! =)")
    print("Selecione:")
    print("\n 1- Cadastre um livro \n 2- Listar os livros pelo genero \n 3- Listar os livros pelo autor \n 4- Listar por livros emprestados \n 5- Fazer a devolução de um livro\n 6- Emprestar livro\n 7- Remover livros \n 8- Listar Todos os Livros\n 0- Sair")

# função para cadastro de novos livros
def cadastro(Livros, livros):
    while True:
        print('---VOCÊ ESCOLHEU CADASTRO---')
        print("Selecione um gênero: \n Digite:")
        print("\n 1- Romance \n 2- Ficção \n 3- Fantasia \n 4- Terror \n 5- Mistério \n 6- Distopia \n 7- Biografia \n 8- Autobiografia \n 9- Filosofia \n 10- Religião/Espiritualidade \n 11- Poesia \n 12- LGBTQIA+ \n 13- Literatura Infanto Juvenil \n 14- Clássicos \n 15- Mitologia\n") 
        resp2 = int(input('\n -->'))
    
        if resp2 == 1:
            print("---VOCÊ SELECIONOU ROMANCE--- \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Romance', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Romance foi adicionado com sucesso!')
            ls()


        elif resp2 == 2:
            print("---VOCÊ SELECIONOU FICÇÃO--- \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Ficção', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Ficção foi adicionado com sucesso!')
            ls()


        elif resp2 == 3:
            print("---VOCÊ SELECIONOU FANTASIA--- \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Fantasia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Fantasia foi adicionado com sucesso!')
            ls()


        elif resp2 == 4:
            print("---VOCÊ SELECIONOU TERROR--- \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Terror', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Terror foi adicionado com sucesso!')
            ls()


        elif resp2 == 5:
            pass

        elif resp2 == 6:
            pass

        elif resp2 == 7:
            pass

        elif resp2 == 8:
            pass

        elif resp2 == 9:
            pass

        elif resp2 == 10:
            pass

        elif resp2 == 11:
            pass

        elif resp2 == 12:
            pass

        elif resp2 == 13:
            pass

        elif resp2 == 14:
            pass

        elif resp2 == 15:
            pass

        else:
            pass

#função para listar todos os livros
def listar(livros):
    print("-- LISTAR TODOS OS LIVROS ---")
    print("\n")
    
    if len (livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for chave, valor in livros.items():
            print(f"{chave}° - \t{valor.GetNome()}")
            print(f"\tAutor: {valor.GetAutor()}")
            print(f"\tGênero: {valor.GetGenero()}")
            print(f"\tEditora: {valor.GetEditora()}")
            print(f"\tStatus: {valor.GetStatus()}")
            print("")