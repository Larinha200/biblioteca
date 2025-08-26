import os
from classes import *

def ls():
    os.system('pause')
    os.system('cls')

def menu():
    print("Olá, seja bem-vindo(a) a nossa biblioteca! =)")
    print("Digite:")
    print("\n 1-Cadastre um livro \n 2-Listar os livros pelo genero \n 3- Listar os livros pelo autor \n 4-Listar por livros empretados \n 5-Fazer a devolução de um livro\n 6-Emprestar livro\n 0-Sair")

# função para cadastro de novos livros
def cadastro(Livros, livros):
    print('---VOCÊ ESCOLHEU CADASTRO---')
    titulo = input('Qual o título: \n')
    autor = input('Qual o autor: \n')
    genero_literario = input('Qual o gênero literário: \n')
    editora = input('Qual a editora: \n')

    livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = genero_literario, Editora = editora, Status = False)
    print('O livro {titulo},')
    ls()

def listar(livros):
    print("--LISTAR TODOS OS LIVROS---")
    print("")
    
    for chave, valor in livros.items():
        print(f"{chave}° - \t{valor.GetNome()}\n\t{valor.GetAutor()}\n\t{valor.GetGenero()}\n\t{valor.GetEditora()}\n\t{valor.GetStatus}")