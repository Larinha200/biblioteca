import os 
from classes import *
from colorama import *

init(autoreset=True)

def ls():
    os.system('pause')
    os.system('cls')

def menu():
    print("\n Olá, seja bem-vindo(a) a nossa biblioteca! =)\n")
    print("Selecione:")
    print("\n 1- Cadastre um livro \n 2- Listar os livros pelo genero \n 3- Listar os livros pelo autor \n 4- Listar os livros por editora \n 5- Listar por livros emprestados \n 6- Fazer a devolução de um livro\n 7- Emprestar livro\n 8- Remover livros \n 9- Listar Todos os Livros\n 10- Editar livros\n 0- Sair")

# função para cadastro de novos livros
def cadastro(Livros, livros):
    while True:
        print('◆━━━━━━▣ VOCÊ ESCOLHEU CADASTRO ▣━━━━━━◆')
        print("Selecione um gênero: \n Selecione:")
        print("\n 1- Romance \n 2- Ficção \n 3- Fantasia \n 4- Terror \n 5- Mistério \n 6- Distopia \n 7- Biografia \n 8- Autobiografia \n 9- Filosofia \n 10- Religião/Espiritualidade \n 11- Poesia \n 12- LGBTQIA+ \n 13- Literatura Infanto Juvenil \n 14- Clássicos \n 15- Mitologia \n 0- Sair\n") 
        resp2 = int(input('\n -->'))
    
        if resp2 == 1:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU ROMANCE ▬▬▬▬▬▬ ◆ \n")

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
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU FICÇÃO ▬▬▬▬▬▬ ◆ \n")

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
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU FANTASIA ▬▬▬▬▬▬ ◆ \n")

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
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU TERROR ▬▬▬▬▬▬ ◆ \n")

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
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU MISTÉRIO ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Mistério', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Mistério foi adicionado com sucesso!')
            ls()

        elif resp2 == 6:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU DISTOPIA ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Distopia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Distopia foi adicionado com sucesso!')
            ls()

        elif resp2 == 7:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU BIOGRAFIA ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Biografia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Biografia foi adicionado com sucesso!')
            ls()

        elif resp2 == 8:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU AUTOBIOGRAFIA ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Autobiografia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Autobiografia foi adicionado com sucesso!')
            ls()

        elif resp2 == 9:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU FILOSOFIA ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Filosofia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Filosofia foi adicionado com sucesso!')
            ls()

        elif resp2 == 10:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU RELIGIÃO/ESPIRITUALIDADE ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Religião/Espiritualidade', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Religião/Espiritualidade foi adicionado com sucesso!')
            ls()

        elif resp2 == 11:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU POESIA ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Poesia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Poesia foi adicionado com sucesso!')
            ls()

        elif resp2 == 12:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU LGBTQIA+ ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'LGBTQIA+', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero LGBTQIA+ foi adicionado com sucesso!')
            ls()

        elif resp2 == 13:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU LITERATURA INFANTO JUVENIL ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Literatura Infanto Juvenil', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Literatura Infanto Juvenil foi adicionado com sucesso!')
            ls()


        elif resp2 == 14:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU CLÁSSICOS ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Clássicos', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Clássicos foi adicionado com sucesso!')
            ls()

        elif resp2 == 15:
            print("◆ ▬▬▬▬▬▬ VOCÊ SELECIONOU MITOLOGIA ▬▬▬▬▬▬ ◆ \n")

            titulo = input('Qual o título: \n')
            print('')
            autor = input('Qual o autor: \n') 
            print('')
            editora = input('Qual a editora: \n')
            print('\n')

            livros[len(livros) + 1] = Livros( Nome= titulo, Autor = autor, Genero = 'Mitologia', Editora = editora, Status = False)
            print(f'O livro {titulo} do autor {autor} da editora {editora} que pertence ao gênero Mitologia foi adicionado com sucesso!')
            ls()

        elif resp2 == 0:
            break
        else:
            print("Número invalido")

#função para listar todos os livros
def listar(livros):
    print(" ◆━━━━━━▣ LISTAR TODOS OS LIVROS ▣━━━━━━◆ ")
    print("\n")
    
    if len (livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for chave, valor in livros.items():
            print(Fore.MAGENTA + f"{chave}° - \tNome: ", end= "")
            print(valor.GetNome())
            print(Fore.MAGENTA + f"\tAutor: ", end= "")
            print(valor.GetAutor())
            print(Fore.MAGENTA + f"\tGênero:", end= "")
            print( valor.GetGenero())
            print(Fore.MAGENTA + f"\tEditora: ", end= "")
            print(valor.GetEditora())
            print(Fore.MAGENTA + f"\tStatus: ", end= "")
            print(valor.GetStatus())
            print("")
            

    
# Função para listar livros por gênero
def listar_por_genero(livros):
    while True:
        print(" ◆━━━━━━▣ LISTAR LIVROS POR GÊNERO ▣━━━━━━◆ \n")
        print('Selecione:')
        print("\n 1- Romance \n 2- Ficção \n 3- Fantasia \n 4- Terror \n 5- Mistério \n 6- Distopia \n 7- Biografia \n 8- Autobiografia \n 9- Filosofia \n 10- Religião/Espiritualidade \n 11- Poesia \n 12- LGBTQIA+ \n 13- Literatura Infanto Juvenil \n 14- Clássicos \n 15- Mitologia \n 0- Voltar\n")

        escolha = int(input('\n --> '))

        generos_lista = {
            1: "Romance",
            2: "Ficção",
            3: "Fantasia",
            4: "Terror",
            5: "Mistério",
            6: "Distopia",
            7: "Biografia",
            8: "Autobiografia",
            9: "Filosofia",
            10: "Religião/Espiritualidade",
            11: "Poesia",
            12: "LGBTQIA+",
            13: "Literatura Infanto Juvenil",
            14: "Clássicos",
            15: "Mitologia"
        }

        if escolha == 0:
            break  # volta pro menu principal

        if escolha < 0 or escolha > 15:   # <-- aqui evita erro
            print("Opção inválida!\n")
            continue

        genero_escolhido = generos_lista[escolha]
        print(f"\n◆━━ LIVROS DO GÊNERO: {genero_escolhido} ━━◆\n")

        encontrados = False
        for chave, livro in livros.items():
            if livro.GetGenero().strip().lower() == genero_escolhido.strip().lower():
                encontrados = True
                print(f"{chave}° - Título: {livro.GetNome()}")
                print(f"\tAutor: {livro.GetAutor()}")
                print(f"\tEditora: {livro.GetEditora()}")
                print(f"\tStatus: {livro.GetStatus()}\n")
    

        if not encontrados:
            print("Nenhum livro cadastrado com este gênero.\n")
        ls()

# Função para listar livros por editora
def listar_por_editora(livros):
    while True:
        print(" ◆━━━━━━▣ LISTAR LIVROS POR EDITORA ▣━━━━━━◆ \n")
        print('Selecione:')
        print("1- Intrínseca \n2- Record \n3- HarperCollins \n4- Galera \n5- Companhia Das Letras \n6- Seguinte \n7- Rocco \n8- Alfaguara \n9- Via Leitura \n10- Principis \n11- Editora 34 \n12- Petra - NF \n13- Civilização Brasileira \n14- Devir, poesia e prosa \n15- Astra Cultura \n16- Penguin e Companhia Das Letras \n17- Darkside \n 0- Voltar")

        escolha = int(input('\n --> '))

        editora_lista = {
            1: "Intrínseca",
            2: "Record",
            3: "HarperCollins ",
            4: "Galera ",
            5: "Companhia Das Letras",
            6: "Seguinte ",
            7: "Rocco ",
            8: "Alfaguara ",
            9: "Via Leitura",
            10: "Principis ",
            11: "Editora 34",
            12: "Petra - NF",
            13: "Civilização Brasileira",
            14: "Devir, poesia e prosa",
            15: "Astra Cultura",
            16: "Penguin e Companhia Das Letras",
            17: "Darkside"
        }

        if escolha == 0:
            break  # volta pro menu principal

        if escolha < 0 or escolha > 17:   # <-- aqui evita erro
            print("Opção inválida!\n")
            continue

        editora_escolhida = editora_lista[escolha]
        print(f"\n◆━━ LIVROS Da EDITORA: {editora_escolhida} ━━◆\n")

        encontrados = False
        for chave, livro in livros.items():
            if livro.GetEditora().strip().lower() == editora_escolhida.strip().lower():
                encontrados = True
                print(f"{chave}° - Título: {livro.GetNome()}")
                print(f"\tAutor: {livro.GetAutor()}")
                print(f"\tGênero: {livro.GetGenero()}")
                print(f"\tStatus: {livro.GetStatus()}\n")
    
        if not encontrados:
            print("Nenhum livro cadastrado com esta editora.\n")
        ls()

# Função para listar livros por autor
def listar_por_autor(livros):
    while True:
        print(" ◆━━━━━━▣ LISTAR LIVROS POR AUTOR ▣━━━━━━◆ \n")
        print('Selecione:')
        print("1- Jenny Han  \n2- Thea Guanzon \n3- HarperCollins \n4- Carla Madeira \n5- J. R. R. Tolkien \n6- Rick Riordan \n7- Holly Black \n8- Uketsu \n9- Raphael Montes  \n10- EE.Lockhart  \n11- Veronica Roth \n12- Suzanne Collins \n13- Marcelo Rubens Paiva \n14- Anne Frank \n15- Franz Kafka  \n16- Fiódor Dostoiévski \n17- Tomás de Kempis \n 18- Luis Antonio Simas \n 19 - Kaio Bruno Dias \n 20- Geffo Pinheiro \n 21- Adam Silveira \n 22- Casey McQuiston\n 23- Holly Jackson\n 24- Stephen Chbosky\n 25 - Machado de Assis\n 26- Annette Giesecke\n 0- Voltar")

        escolha = int(input('\n --> '))

        autor_lista = {
            1: "Jenny Han",
            2: "Thea Guanzon",
            3: "HarperCollins ",
            4: "Carla Madeira",
            5: "J. R. R. Tolkien",
            6: "Rick Riordan ",
            7: "Holly Black ",
            8: "Uketsu ",
            9: "Raphael Montes ",
            10: "EE.Lockhart ",
            11: "Veronica Roth",
            12: "Suzanne Collins",
            13: "Marcelo Rubens Paiva",
            14: "Anne Frank",
            15: "Franz Kafka ",
            16: "Fiódor Dostoiévski ",
            17: "Tomás de Kempis ",
            18: "Luis Antonio Simas ",
            19: "Kaio Bruno Dias ",
            20: "Geffo Pinheiro ",
            21: "Adam Silveira ",
            22: "Casey McQuiston",
            23: "Holly Jackson",
            24: "Stephen Chbosky",
            25: "Machado de Assis",
            26: "Annette Giesecke"
        }

        if escolha == 0:
            break  # volta pro menu principal

        if escolha < 0 or escolha > 15:   # <-- aqui evita erro
            print("Opção inválida!\n")
            continue

        autor_escolhido = autor_lista[escolha]
        print(f"\n◆━━ LIVROS Da EDITORA: {autor_escolhido} ━━◆\n")

        encontrados = False
        for chave, livro in livros.items():
            if livro.GetAutor().strip().lower() == autor_escolhido.strip().lower():
                encontrados = True
                print(f"{chave}° - Título: {livro.GetNome()}")
                print(f"\tEditora: {livro.GetEditora()}")
                print(f"\tGênero: {livro.GetGenero()}")
                print(f"\tStatus: {livro.GetStatus()}\n")
    
        if not encontrados:
            print("Nenhum livro cadastrado com este autor.\n")
        ls()

# Função para listar livros emprestados
def listar_emprestados(livros):
    print(" ◆━━━━━━▣ LIVROS EMPRESTADOS ▣━━━━━━◆ \n")

    emprestados = False
    for chave, livro in livros.items():
        if livro.GetStatus() == "Emprestado":
            emprestados = True
            print(f"{chave}° - Título: {livro.GetNome()}")
            print(f"\tAutor: {livro.GetAutor()}")
            print(f"\tGênero: {livro.GetGenero()}")
            print(f"\tEditora: {livro.GetEditora()}\n")

    if not emprestados:
        print("Nenhum livro emprestado no momento.\n")

    ls()

# Função para emprestar livro
def emprestar_livro(livros):
    print(" ◆━━━━━━▣ EMPRESTAR LIVRO ▣━━━━━━◆ \n")

# Mostrar livros disponíveis
    disponiveis = False
    for chave, livro in livros.items():
        if livro.GetStatus() == "Disponível":
            disponiveis = True
            print(f"{chave}° - Título: {livro.GetNome()}")
            print(f"\tAutor: {livro.GetAutor()}\n")

    if not disponiveis:
        print("Nenhum livro disponível para empréstimo.\n")
        ls()
        return

    try:
        codigo = input("Digite o número do livro que deseja emprestar: ")
        if codigo not in livros:
            print("Código de livro não encontrado!")
            ls()
            return

        livro = livros[codigo]
        if livro.GetStatus() == "Emprestado":
            print("Este livro já está emprestado!")
            ls()
            return

# Realizar empréstimo
        livro.SetStatus(True)# True significa emprestado
        print(f"\n✅ Livro '{livro.GetNome()}' emprestado com sucesso!")

    except ValueError:
        print("Código inválido!")

    ls()

# Função para devolver livro
def devolver_livro(livros):
    print(" ◆━━━━━━▣ DEVOLVER LIVRO ▣━━━━━━◆ \n")

# Mostrar livros emprestados
    emprestados = True
    for chave, livro in livros.items():
        if livro.GetStatus() == "Emprestado":
            emprestados = True
            print(f"{chave}° - Título: {livro.GetNome()}")
            print(f"\tAutor: {livro.GetAutor()}\n")

    if not emprestados:
        print("Nenhum livro emprestado no momento.\n")
        ls()
        return

    try:
        codigo = input("Digite o número do livro que deseja devolver: ")
        if codigo not in livros:
            print("Código de livro não encontrado!")
            ls()
            return

        livro = livros[codigo]
        if livro.GetStatus() == "Disponível":
            print("Este livro já está disponível!")
            ls()
            return

# Realizar devolução
        livro.SetStatus(False)# False significa disponível
        print(f"\n✅ Livro '{livro.GetNome()}' devolvido com sucesso!")

    except ValueError:
        print("Código inválido!")

    ls()

# Função para remover livro
def remover_livro(livros):
    print(" ◆━━━━━━▣ REMOVER LIVRO ▣━━━━━━◆ \n")

    listar(livros)

    if len(livros) == 0:
        ls()
        return

    try:
        codigo = input("Digite o número do livro que deseja remover: ")
        if codigo not in livros:
            print("Código de livro não encontrado!")
            ls()
            return

        livro = livros[codigo]
        confirmacao = input(f"Tem certeza que deseja remover '{livro.GetNome()}'? (S/N): ")

        if confirmacao.upper() == 'S':
            del livros[codigo]
            print("Livro removido com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Código inválido!")

    ls()


def editar(livros):    
    var = None 
    
    print("digite: \n1-Nome \n2-Autor \n3-Genero \n4-Editora")    
    resp3 = int(input("----> "))
    
    if resp3 == 1:
        listar(livros)
        var = input("Digite o número do seu livro: ")

        for chave , valor in livros.items():
            if chave == var:
                
                nome = input("---> ")
                valor.SetNome(nome)
                print(nome)
                ls()
                menu()
                
            
    elif resp3 == 2:
        listar(livros)
        var = input("Digite o número do seu livro: ")

        for chave , valor in livros.items():
            if chave == var:
                
                autor = input("---> ")
                valor.SetAutor(autor)
                print(autor)
                ls()
                menu()

    elif resp3 == 3:
        listar(livros)
        var = input("Digite o número do seu livro: ")

        for chave , valor in livros.items():
            if chave == var:
                
                genero = input("---> ")
                valor.SetGenero(genero)
                print(genero)
                ls()
                menu()
    
    elif resp3 == 4:
        listar(livros)
        var = input("Digite o número do seu livro: ")

        for chave , valor in livros.items():
            if chave == var:
                
                editora = input("---> ")
                valor.SetEditora(editora)
                print(editora)
                ls()
                menu()