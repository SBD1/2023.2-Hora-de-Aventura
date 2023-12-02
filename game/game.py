from Banco import *

pc = Pc()
personagem = Personagem()
possuiHab = PossuiHab()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    return jogador[0]

def EncontrarSalas(pos):
    Quadrado=2
    lc=Local()
    Oeste=lc.getLocal(pos-1)
    Norte=lc.getLocal(pos-Quadrado)
    Leste=lc.getLocal(pos+1)
    Sul=lc.getLocal(pos+Quadrado)
    salas_disponiveis = []

    # Adicionar à lista se não for None
    if Oeste is not None:
        salas_disponiveis.append(Oeste[0][0])
        #salas_disponiveis.append(Oeste[0][2])
    if Norte is not None:
        salas_disponiveis.append(Norte[0][0])
        #salas_disponiveis.append(Norte[0][2])
    if Leste is not None:
        salas_disponiveis.append(Leste[0][0])
        #salas_disponiveis.append(Leste[0][2])
    if Sul is not None:
        salas_disponiveis.append(Sul[0][0])
        #salas_disponiveis.append(Sul[0][2])

    # Retornar a lista de salas disponíveis
    return salas_disponiveis

def ListarHabilidadePersonagem():    
    habilidadePersonagem = input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    habilidade = possuiHab.consultarPossuiHabPersonagem(habilidadePersonagem)
    return habilidade[0]

def criarJogador():
    pcID = input("ID do jogador :")
    pcNome = input("Nome do jogador :")
    pcEspecie = input("Especie do jogador :")
    criarPC = Pc()
    personagem.criarPersonagem(pcID, False) 
    criarPC.criarPc(pcID,pcNome,0,100,0,0,pcEspecie,5,0,0)
    menuJogador()
                
def verJogadorOp():
    IDdoJogador = input("Digite o ID do jogador que busca:")
    jogador = pc.getPC(IDdoJogador)
    print("\n--------------------------------------------------------------------------------\n")
    print(f"\033[1;32m\nNome: {jogador[0][1]}\nVida:{jogador[0][3]}\nLVL: {jogador[0][4]}\nDinheiro: {jogador[0][5]}\033[0m")
    print("\n--------------------------------------------------------------------------------\n")
    menuJogador()

def menuJogador():
    print("\033[1;32m Opções de Jogador")
    print("\033[0;36m|1| = Criar personagem")
    print("|2| = Ver jogador")
    print("|3| = Atualizar jogador")
    print("|4| = Deletar jogador")
    print("|5| = Voltar\n")
    
    OpçaoJogador = input()            
    
    match OpçaoJogador:
        case '1':
            criarJogador()
        case '2':
            verJogadorOp()                
                            