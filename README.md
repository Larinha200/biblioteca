# PROJETO BIBLIOTECA

### Explicação do código da subpasta por partes -> classe.py



    class Livros:     # criação e declaração de uma nova classe denominada livros
     def __init__(self,Nome,Autor,Genero,Editora,Status):     # parâmetros/valores para criar o objeto
          self.__Nome__ = Nome     # atributo de instância para o título do livro
          self.__Autor__ = Autor     # atributo de instância para o nome do autor
          self.__Genero__ =  Genero     # atributo de instância para o gênero do çivro
          self.__Editora__ = Editora     # atributo de instânsia para a editora da obra
          self.__Status__ = Status     # atributo de instância para os status na ual se encontra a obra (emprestado ou disponível)

Parte do código foi utilizada no começo para realizar a criação de uma classe chamada "Livros", para poder criar objetos e 
guardas as informações denominadas no "def__init__"





     def GetNome (self):     #
        return self.__Nome__     #

ppppppppppp


        
    
     def GetAutor (self):
        return  self.__Autor__
    
     def GetGenero (self):
        return self.__Genero__
     
     def GetEditora (self):
        return self.__Editora__
    
     def GetStatus(self):
        return "Disponível" if self.__Status__ == False else "Emprestado"

    
     def SetNome (self, Nome):
        self.__Nome__= Nome
        return self.__Nome__ 
    
     def SetAutor (self,Autor):
        self.__Autor__ = Autor
        return  self.__Autor__
    
     def SetGenero (self, Genero):
        self.__Genero__ = Genero
        return self.__Genero__
    
     def SetEditora (self, Editora):
        self.__Editora__ = Editora
        return self.__Editora__
    
     def SetStatus (self, Status):
        self.__Status__ = Status
        return self.__Status__   

