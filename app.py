from funcao import *
from  classes import *

l1= Livros ("Para todos os garotos que eu já amei","Jenny Han", "Romance", "Intrínseca", False)
l2= Livros (" A guerra dos furacões ", "Thea Guanzon","Romance", "Intrínseca", False )
l3= Livros ("Tudo é rio","Carla Madeira","Ficção", "Record", False )
l4= Livros ("O Hobbit","J. R. R. Tolkien", "Ficção", "HarperCollins ", False  )
l5= Livros ("Percy Jackson: A batalha do labirinto", "Rick Riordan", "Fantasia", " Intrínseca", False )
l6= Livros ("A rainha do nada", "Holly Black", "Fantasia", "Galera", False)
l7= Livros ("Casas Estranhas Vol 1","Uketsu","Terror" , "Intrínseca", False )
l8= Livros ("Jantar Secreto","Raphael Montes","Mistério", "Companhia Das Letras", False)
l9= Livros ("Mentirosos", "E.Lockhart", "Mistério", "Seguinte", False)
l10= Livros ("Divergente", "Veronica Roth","Distopia"," Rocco", False)
l11= Livros ("Jogos vorazes","Suzanne Collins","Distopia"," Rocco", False)
l12= Livros ("Ainda estou aqui ","Marcelo Rubens Paiva","Biografia","Alfaguara", False)
l13= Livros ("O diário de Anne Frank ", "Anne Frank","Autobiografia", "Via Leitura", False )
l14= Livros ("Metamorfose","Franz Kafka","Filosofia", "Principis", False)
l15= Livros ("Crime e Castigo", "Fiódor Dostoiévski","Filosofia", "Editora 34", False)
l16= Livros ("Imitação de cristo ", "Tomás de Kempis", "Religião/Espiritualidade", "Petra - NF", False)
l17= Livros ("Umbanda: Uma história do Brasil ", "Luis Antonio Simas","Religião/Espiritualidade","Civilização Brasileira", False)
l18= Livros ("Eu sempre morro", "Kaio Bruno Dias", "Poesia", "Devir, poesia e prosa", False)
l19= Livros ("Desculpe o exagero, mas não sei sentir pouco", "Geffo Pinheiro", "Poesia", "Astra Cultura", False)
l20= Livros ("Os dois morrem no final","Adam Silveira", "LGBTQIA+", "Intrínseca", False)
l21= Livros ("Combina?", "Casey McQuiston", "LGBTQIA+", "Seguinte", False)
l22= Livros ("Manual de Assassinato para boas garotas", "Holly Jackson", "Literatura Infanto Juvenil", "Intrínseca", False)
l23= Livros ("As vantagens de ser invisível", "Stephen Chbosky", "Literatura Infanto Juvenil", "Rocco", False)
l24= Livros ("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Clássicos", "Penguin e Companhia Das Letras", False  )
l25= Livros ("Origens da Mitologia ","Annette Giesecke", "Mitologia", "Darkside", False )


livros = {}

while True:
    menu()
    resp = int(input("\n---> "))

    if resp == 1:
        ls()
        cadastro(Livros, livros)

    if resp == 2:
        pass

    if resp == 3:
        pass

    if resp == 4:
        pass

    if resp == 5:
        pass

    if resp == 6: 
        pass

    if resp == 7: 
        pass

    if resp == 8: 
        ls()
        listar(livros)

    if resp == 0:
        pass

