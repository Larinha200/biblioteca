import os

def ls():
    os.system('pause')
    os.system('cls')

# função para cadastro de novos livros
def cadastro(livros, nome,autor, ):
    print('---VOCÊ ESCOLHEU CADASTRO---')
    nome = input('Qual o título: \n')
    autor = input('Qual o autor: \n')
    genero_literario = input('Qual o gênero literário: \n')
    editora = input('Qual a editora: \n')