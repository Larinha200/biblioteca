from funcao import *
from classes import *
from colorama import *
init(autoreset=True)

l1= Livros (Nome="Para todos os garotos que eu já amei",Autor="Jenny Han",Genero= "Romance", Editora= "Intrínseca",Status= False)
l2= Livros (Nome="A guerra dos furacões ", Autor="Thea Guanzon",Genero="Romance", Editora="Intrínseca",Status=  False )
l3= Livros (Nome="Tudo é rio",Autor="Carla Madeira",Genero="Ficção", Editora="Record",Status=  False )
l4= Livros (Nome="O Hobbit",Autor="J. R. R. Tolkien", Genero="Ficção", Editora="HarperCollins ", Status= False  )
l5= Livros (Nome="Percy Jackson: A batalha do labirinto", Autor="Rick Riordan",Genero= "Fantasia", Editora=" Intrínseca",Status=  False )
l6= Livros (Nome="A rainha do nada",Autor= "Holly Black", Genero="Fantasia",Editora= "Galera",Status=  False)
l7= Livros (Nome="Casas Estranhas Vol 1",Autor="Uketsu",Genero="Terror" , Editora="Intrínseca",Status=  False )
l8= Livros (Nome="Jantar Secreto",Autor="Raphael Montes",Genero="Mistério",Editora= "Companhia Das Letras",Status=  False)
l9= Livros (Nome="Mentirosos", Autor="E.Lockhart",Genero= "Mistério", Editora="Seguinte", Status= False)
l10= Livros (Nome="Divergente",Autor= "Veronica Roth",Genero="Distopia",Editora=" Rocco", Status= False)
l11= Livros (Nome="Jogos vorazes",Autor="Suzanne Collins",Genero="Distopia",Editora=" Rocco", Status= False)
l12= Livros (Nome="Ainda estou aqui ",Autor="Marcelo Rubens Paiva",Genero="Biografia",Editora="Alfaguara", Status= False)
l13= Livros (Nome="O diário de Anne Frank ",Autor= "Anne Frank",Genero="Autobiografia", Editora="Via Leitura", Status= False  )
l14= Livros (Nome="Metamorfose",Autor="Franz Kafka",Genero="Filosofia", Editora="Principis",Status=  False)
l15= Livros (Nome="Crime e Castigo", Autor="Fiódor Dostoiévski",Genero="Filosofia", Editora="Editora 34", Status= False)
l16= Livros (Nome="Imitação de cristo ",Autor= "Tomás de Kempis",Genero="Religião/Espiritualidade",Editora= "Petra - NF",Status= False)
l17= Livros (Nome="Umbanda: Uma história do Brasil ",Autor= "Luis Antonio Simas",Genero="Religião/Espiritualidade",Editora="Civilização Brasileira",Status=  False)
l18= Livros (Nome="Eu sempre morro", Autor="Kaio Bruno Dias", Genero="Poesia", Editora="Devir, poesia e prosa",Status= False)
l19= Livros (Nome="Desculpe o exagero, mas não sei sentir pouco", Autor="Geffo Pinheiro", Genero="Poesia", Editora="Astra Cultura",Status=  False)
l20= Livros (Nome="Os dois morrem no final",Autor="Adam Silveira",Genero= "LGBTQIA+",Editora= "Intrínseca",Status=  False)
l21= Livros (Nome="Combina?",Autor= "Casey McQuiston", Genero="LGBTQIA+",Editora= "Seguinte",Status=  False)
l22= Livros (Nome="Manual de Assassinato para boas garotas",Autor= "Holly Jackson", Genero="Literatura Infanto Juvenil",Editora= "Intrínseca", Status= False)
l23= Livros (Nome="As vantagens de ser invisível", Autor="Stephen Chbosky", Genero="Literatura Infanto Juvenil",Editora= "Rocco",Status=  False)
l24= Livros (Nome="Memórias Póstumas de Brás Cubas", Autor="Machado de Assis", Genero="Clássicos", Editora="Penguin e Companhia Das Letras", Status= False  )
l25= Livros (Nome="Origens da Mitologia ",Autor="Annette Giesecke", Genero="Mitologia",Editora= "Darkside",Status=  False )


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

    if resp == 2:
        ls()
        listar_por_genero(livros)

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

