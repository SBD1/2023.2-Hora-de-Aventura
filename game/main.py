from Banco.Mundo import * 
from Banco.Personagem import * 


""" 
nomeMundoDestino = input("Digite o nome do seu mundoDeDestino: ")
 """

""" nomeMundo = input("Digite o nome do seu mundo: ")

mundo = Mundo() 
mundo.deletarMundo(nomeMundo)
mundo.consultarMundo() 
 """

doan = Personagem() 

doan.criarPersonagem(4,False)
print('\n')
doan.consultarPersonagem()
print('\n')
doan.consultarPersonagemID(4)
print('\n')
doan.deletarPersonagem(4)
doan.consultarPersonagem()