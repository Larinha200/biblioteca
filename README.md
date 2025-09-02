# PROJETO BIBLIOTECA

### Explicação do código da subpasta por partes -> classe.py



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
