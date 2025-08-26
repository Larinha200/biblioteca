import os 
from classes import *

def ls():
    os.system('pause')
    os.system('cls')

def menu():
    print("Olá, seja bem-vindo(a) a nossa biblioteca! =)")
    print("Digite:")
    print("\n 1- Cadastre um livro \n 2- Listar os livros pelo genero \n 3- Listar os livros pelo autor \n 4- Listar por livros emprestados \n 5- Fazer a devolução de um livro\n 6-Emprestar livro\n 7- Remover livros \n 8- Listar Todos os Livros\n 0-Sair")

# função para cadastro de novos livros
def cadastro(Livros, livros):
    print('---VOCÊ ESCOLHEU CADASTRO---')
    print("Selecione um genero: \n Digite:")
    print("1-Romance \n2-Ficção \n3-Fantasia \n4-Terror \n5-Mistério \n6-Distopia \n7-Biografia \n8-Autobiografia \n9-Filosofia \n10-Religião/Espiritualidade \n11-Poesia \n12-LGBTQIA+ \n13-Literatura Infanto Juvenil \n14-Clássicos \n15-Mitologia")
    titulo = input('Qual o título: \n')
    autor = input('Qual o autor: \n')
    genero_literario = input('Qual o gênero literário: \n')
    editora = input('Qual a editora: \n')

    livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = genero_literario, Editora = editora, Status = False)
    print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero {genero_literario} foi adicionado com sucesso!')
    ls()

#função para listar todos os livros
def listar(livros):
    print("-- LISTAR TODOS OS LIVROS ---")
    print("")
    
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