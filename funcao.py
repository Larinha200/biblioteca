import os
from classes import *

def ls():
    os.system('pause')
    os.system('cls')

def menu():
    print("Olá, seja bem-vindo(a) a nossa biblioteca! =)")
    print("Selecione a opção na qual deseja:")
    print("\n 1- Cadastre um livro \n 2- Listar os livros pelo gênero \n 3- Listar os livros pelo autor \n 4- Listar por livros empretados \n 5- Fazer a devolução de um livro\n 6- Emprestar livro\n 0- Sair")

# função para cadastro de novos livros
def cadastro(Livros, livros):
    print('---VOCÊ ESCOLHEU CADASTRO---')
    titulo = input('Qual o título: \n')
    autor = input('Qual o autor: \n')
    genero_literario = input('Qual o gênero literário: \n')
    editora = input('Qual a editora: \n')
    livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = genero_literario, Editora = editora  )
    ls()
    ls()
