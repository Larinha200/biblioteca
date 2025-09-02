# PROJETO BIBLIOTECA

### Explicação do código da subpasta por partes -> classe.py


![Image](https://github.com/user-attachments/assets/b912d01b-30cd-4384-9855-4a9f54297da9)


 **Parte do código foi utilizada no começo para realizar a criação de uma classe chamada "Livros", para poder criar objetos e 
guardas as informações denominadas no "def__init__"** <br>

    class Livros:     # criação e declaração de uma nova classe denominada livros
     def __init__(self,Nome,Autor,Genero,Editora,Status):     # parâmetros/valores para criar o objeto
          self.__Nome__ = Nome     # atributo de instância para o título do livro
          self.__Autor__ = Autor     # atributo de instância para o nome do autor
          self.__Genero__ =  Genero     # atributo de instância para o gênero do çivro
          self.__Editora__ = Editora     # atributo de instânsia para a editora da obra
          self.__Status__ = Status     # atributo de instância para os status na ual se encontra a obra (emprestado ou disponível)


![Image](https://github.com/user-attachments/assets/b912d01b-30cd-4384-9855-4a9f54297da9)


**Já apartir desta parte do código ela tera como função definir um método de classe para poder retornar o valor armazenado no atributo** <br> 


     def GetNome (self):     # define uma função e permite acessar outros atributos e métodos da instância 
        return self.__Nome__     # retorna esse valor atribuido que está armazenado no objeto
        
    
     def GetAutor (self):     # define uma função e permite acessar outros atributos e métodos da instância
        return  self.__Autor__     # retorna esse valor atribuido que está armazenado no objeto
        
    
     def GetGenero (self):     # define uma função e permite acessar outros atributos e métodos da instância
        return self.__Genero__     # retorna esse valor atribuido que está armazenado no objeto
        
     
     def GetEditora (self):     # define uma função e permite acessar outros atributos e métodos da instância
        return self.__Editora__     # retorna esse valor atribuido que está armazenado no objeto
        
    
     def GetStatus(self):     # define uma função e permite acessar outros atributos e métodos da instância
        return "Disponível" if self.__Status__ == False else "Emprestado"     # retorna esse valor atribuido que está armazenado no objeto


![Image](https://github.com/user-attachments/assets/b912d01b-30cd-4384-9855-4a9f54297da9)


**Este trecho define um método setter, na qual recebe um valor, atribui este valor ao atributo do objeto e retorno o valor atribuído**<br>
    
     def SetNome (self, Nome):     # parâmetro para passar com um novo nome
        self.__Nome__= Nome     # faz uma atribuição do valor passado para o atributo do objeto
        return self.__Nome__     # é um método utilizado para retornar o valor na qual acabou de ser salvo

    
     def SetAutor (self,Autor):     # parâmetro para passar com um novo nome
        self.__Autor__ = Autor     # faz uma atribuição do valor passado para o atributo do objeto
        return  self.__Autor__     # é um método utilizado para retornar o valor na qual acabou de ser salvo

    
     def SetGenero (self, Genero):     # parâmetro para passar com um novo nome
        self.__Genero__ = Genero     # faz uma atribuição do valor passado para o atributo do objeto
        return self.__Genero__     # é um método utilizado para retornar o valor na qual acabou de ser salvo

    
     def SetEditora (self, Editora):     # parâmetro para passar com um novo nome
        self.__Editora__ = Editora     # faz uma atribuição do valor passado para o atributo do objeto
        return self.__Editora__     # é um método utilizado para retornar o valor na qual acabou de ser salvo

    
     def SetStatus (self, Status):     # parâmetro para passar com um novo nome
        self.__Status__ = Status     # faz uma atribuição do valor passado para o atributo do objeto
        return self.__Status__      # é um método utilizado para retornar o valor na qual acabou de ser salvo


![Image](https://github.com/user-attachments/assets/b912d01b-30cd-4384-9855-4a9f54297da9)


### Explicação do código da subpasta por partes -> app.py


![Image](https://github.com/user-attachments/assets/b912d01b-30cd-4384-9855-4a9f54297da9)


**Este início de código é utilizado para a realização da importação e instalação dos arquivos de outras pastas e programas que irão ser utilizados, além de também ativá-los **

    from funcao import *     # importa o arquivo da pasta funções
    from classes import *     # importa o arquivo da pasta classes
    from colorama import *     # importa o arquivo do programa colorama
    init(autoreset=True)     # utilizado para fazer com que a biblioteca colorama funcione


![Image](https://github.com/user-attachments/assets/b912d01b-30cd-4384-9855-4a9f54297da9)    


**Nesse trecho do código foi criado e utilizado uma lista com o objetivo de armazenar as informações dos livros selecionados e disponíveis na biblioteca possuindo todas as informações necessárias, como título da obra, autor, gênero, editora e também os status inicial da obra denominada como disponível = false**

    l1= Livros (Nome="Para todos os garotos que eu já amei",Autor="Jenny Han",Genero= "Romance", Editora= "Intrínseca",Status= False)     # informações sobre o livro nº 1       "Para todos os garotos que eu já amei"
    l2= Livros (Nome="A guerra dos furacões ", Autor="Thea Guanzon",Genero="Romance", Editora="Intrínseca",Status=  False )     #
    l3= Livros (Nome="Tudo é rio",Autor="Carla Madeira",Genero="Ficção", Editora="Record",Status=  False )     #
    l4= Livros (Nome="O Hobbit",Autor="J. R. R. Tolkien", Genero="Ficção", Editora="HarperCollins ", Status= False  )     #
    l5= Livros (Nome="Percy Jackson: A batalha do labirinto", Autor="Rick Riordan",Genero= "Fantasia", Editora=" Intrínseca",Status=  False )     #
    l6= Livros (Nome="A rainha do nada",Autor= "Holly Black", Genero="Fantasia",Editora= "Galera",Status=  False)     #
    l7= Livros (Nome="Casas Estranhas Vol 1",Autor="Uketsu",Genero="Terror" , Editora="Intrínseca",Status=  False )     #
    l8= Livros (Nome="Jantar Secreto",Autor="Raphael Montes",Genero="Mistério",Editora= "Companhia Das Letras",Status=  False)     #
    l9= Livros (Nome="Mentirosos", Autor="E.Lockhart",Genero= "Mistério", Editora="Seguinte", Status= False)     #
    l10= Livros (Nome="Divergente",Autor= "Veronica Roth",Genero="Distopia",Editora=" Rocco", Status= False)     #
    l11= Livros (Nome="Jogos vorazes",Autor="Suzanne Collins",Genero="Distopia",Editora=" Rocco", Status= False)     #
    l12= Livros (Nome="Ainda estou aqui ",Autor="Marcelo Rubens Paiva",Genero="Biografia",Editora="Alfaguara", Status= False)     #
    l13= Livros (Nome="O diário de Anne Frank ",Autor= "Anne Frank",Genero="Autobiografia", Editora="Via Leitura", Status= False  )     #
    l14= Livros (Nome="Metamorfose",Autor="Franz Kafka",Genero="Filosofia", Editora="Principis",Status=  False)     #
    l15= Livros (Nome="Crime e Castigo", Autor="Fiódor Dostoiévski",Genero="Filosofia", Editora="Editora 34", Status= False)     #
    l16= Livros (Nome="Imitação de cristo ",Autor= "Tomás de Kempis",Genero="Religião/Espiritualidade",Editora= "Petra - NF",Status= False)     #
    l17= Livros (Nome="Umbanda: Uma história do Brasil ",Autor= "Luis Antonio Simas",Genero="Religião/Espiritualidade",Editora="Civilização Brasileira",Status=  False)     #
    l18= Livros (Nome="Eu sempre morro", Autor="Kaio Bruno Dias", Genero="Poesia", Editora="Devir, poesia e prosa",Status= False)     #
    l19= Livros (Nome="Desculpe o exagero, mas não sei sentir pouco", Autor="Geffo Pinheiro", Genero="Poesia", Editora="Astra Cultura",Status=  False)     #
    l20= Livros (Nome="Os dois morrem no final",Autor="Adam Silveira",Genero= "LGBTQIA+",Editora= "Intrínseca",Status=  False)     #
    l21= Livros (Nome="Combina?",Autor= "Casey McQuiston", Genero="LGBTQIA+",Editora= "Seguinte",Status=  False)     #
    l22= Livros (Nome="Manual de Assassinato para boas garotas",Autor= "Holly Jackson", Genero="Literatura Infanto Juvenil",Editora= "Intrínseca", Status= False)     #
    l23= Livros (Nome="As vantagens de ser invisível", Autor="Stephen Chbosky", Genero="Literatura Infanto Juvenil",Editora= "Rocco",Status=  False)     #
    l24= Livros (Nome="Memórias Póstumas de Brás Cubas", Autor="Machado de Assis", Genero="Clássicos", Editora="Penguin e Companhia Das Letras", Status= False  )     #
    l25= Livros (Nome="Origens da Mitologia ",Autor="Annette Giesecke", Genero="Mitologia",Editora= "Darkside",Status=  False )     #




    livros = {}

    livros['1']= l1
    livros['2']= l2
    livros['3']= l3
    livros['4']= l4
    livros['5']= l5
    livros['6']= l6
    livros['7']= l7
    livros['8']= l8
    livros['9']= l9
    livros['10']= l10
    livros['11']= l11
    livros['12']= l12
    livros['13']= l13
    livros['14']= l14
    livros['15']= l15
    livros['16']= l16
    livros['17']= l17
    livros['18']= l18
    livros['19']= l19
    livros['20']= l20
    livros['21']= l21
    livros['22']= l22
    livros['23']= l23
    livros['24']= l24
    livros['25']= l25

        while True:
            menu()
            resp = int(input("\n---> "))

        if resp == 1:
            ls()
            cadastro(Livros, livros)
            ls()

        elif resp == 2:
            ls()
            listar_por_genero(livros)
            ls()

        elif resp == 3:
            ls()
            listar_por_autor(livros)
            ls()

        elif resp == 4:
            ls()
            listar_por_editora(livros)
            ls()

        elif resp == 5:
            ls()
            listar_emprestados(livros)
            ls()

        elif resp == 6:
            ls()
            devolver_livro(livros)
            ls()

        elif resp == 7: 
            ls()
            emprestar_livro(livros)
            ls()

        elif resp == 8:
            ls() 
            remover_livro(livros)
            ls()

        elif resp == 9: 
            ls()
            listar(livros)
            ls()

        elif resp == 10:
            ls()
            editar(livros)
            ls()

        elif resp == 0:
            break

        else:
            print("Número invalido")
        
            print("Saindo...")
