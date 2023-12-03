from Banco import *

pc = Pc()
personagem = Personagem()
possuiHab = PossuiHab()
lc=Local()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    return jogador[0]

def EncontrarSalas(pos, Id):
    Quadrado=2
    Oeste=lc.getLocal(pos-1)
    Norte=lc.getLocal(pos-Quadrado)
    Leste=lc.getLocal(pos+1)
    Sul=lc.getLocal(pos+Quadrado)
    salas_disponiveis = []

    print("\033[1;32mSuas opções de viajem são:\033[0m\n")

    if Oeste is not None and ((pos)%Quadrado):
        print(f"\033[0;36mOeste = {Oeste[0][2]} / Cordenada {Oeste[0][0]}\033[0m\n")
        salas_disponiveis.append(Oeste[0][0])

    if Norte is not None:
        print(f"\033[0;36mNorte = {Norte[0][2]} / Cordenada {Norte[0][0]}\033[0m\n")
        salas_disponiveis.append(Norte[0][0])

    if Leste is not None and (((pos+1)%Quadrado) != 0):
        print(f"\033[0;36mLeste = {Leste[0][2]} / Cordenada {Leste[0][0]}\033[0m\n")
        salas_disponiveis.append(Leste[0][0])

    if Sul is not None:
        print(f"\033[0;36mSul = {Sul[0][2]} / Cordenada {Sul[0][0]}\033[0m\n")
        salas_disponiveis.append(Sul[0][0])

    mudar=int(input("\033[1;32mPara qual sala deseja viajar? Digite -1 para Sair: \033[0m"))

    for i in salas_disponiveis:
        if(i==mudar):
            print("")
            pc.updatePcLocal(Id, mudar)


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
    NomedoJogador = input("Digite o Nome do jogador(es) que busca:")
    jogador = pc.consultarPCNome(NomedoJogador)
    tuplas = [f"| ID:{x[0]} | Nome: {x[1]} | LVL:{x[4]} | Especie:{x[6]}|" for x in jogador]
    for y in tuplas:
        print(y)  
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
                            

#verJogadorOp()
#ListarHabilidadePersonagem()
