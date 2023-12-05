from Banco import *

pc = Pc()
personagem = Personagem()
possuiHab = PossuiHab()
lc=Local()
instanciaItem = Instanciaitem()
inventario = Inventario()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    while(True):
        posicao=lc.getLocalPc(jogador[0][0])
        print("\n"+80*"-"+"\n")
        print(f"\033[1;32m{jogador[0][1]}\nLocal: {posicao[0][2]}\nDescrição: {posicao[0][1]}\nCoordenada: {posicao[0][0]}\033[0m")
        print("\n"+80*"-"+"\n")
        print("\033[0;36m|1| = Mudar de sala\n|2| = Voltar para o menu principal\033[0m")
        opcao = input()
        match opcao:
            case '1':
                EncontrarSalas(posicao[0][0], jogador[0][0])
            case '2':
                print("\033[31;1;4mVoltando para o menu principal\033[0m")
                break


def EncontrarSalas(pos, Id):
    Quadrado=15
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
            print(f"Você viajou para a sala: {i}")
            pc.updatePcLocal(Id, mudar)


        
#def inserirInventarioPersonagem(pcID):
#    IDinv+=1
#    inventario.inserirInventario(IDinv,1,pcID)    

def ListarHabilidadePersonagem(pcID):    
    habilidade = possuiHab.consultarPossuiHabPersonagem(pcID)
    tuplasHabilidade =[f"|Habilidades que possui\n|Nome Habilidade:| {y[1]}\n\n" for y in habilidade]
    for x in tuplasHabilidade:
        print(x)       
    
def definirHabilidadePersonagem(pcEspecie,pcID):
    possuiHab = PossuiHab()       
    match pcEspecie:
        ## --- Humanous ---
        case 'Humano':
            possuiHab.inserirPossuiHab(pcID,1)
        
        case 'humano':
            possuiHab.inserirPossuiHab(pcID,1)
        
        ## --- Povo do fogo ---
        case 'Povo fogo':
            possuiHab.inserirPossuiHab(pcID,2)
        
        case 'Povo Fogo':
            possuiHab.inserirPossuiHab(pcID,2)
        
        case 'povo fogo':
            possuiHab.inserirPossuiHab(pcID,2)
        
        ## --- Povo do crystal ---
        case 'Povo crystal':
            possuiHab.inserirPossuiHab(pcID,3)
        
        case 'Povo Crystal':
            possuiHab.inserirPossuiHab(pcID,3)
        
        case 'povo crystal':
            possuiHab.inserirPossuiHab(pcID,3)
                
        ## --- Vampirous ---        
        case 'Vampiro':
            possuiHab.inserirPossuiHab(pcID,4)
        
        case 'vampiro':
            possuiHab.inserirPossuiHab(pcID,4)

        ## --- Nao digitou nenhuma opcao valida ---
        case _:
            print("\nDigite uma opção válida\n")
            menuJogador()

def deletarJogador(pcID):
    criarPC = Pc()
    criarPC.deletarPC(pcID)
    
def verJogadorOp(NomedoJogador,pcID):
    jogador = pc.consultarPCNome(NomedoJogador)
    tuplas = [f"|Caracteristicas personagem\n| ID:{x[0]} | Nome: {x[1]} | LVL:{x[4]}| Especie:{x[6]}|\n\n" for x in jogador]
    for y in tuplas:
        print(y)
    ListarHabilidadePersonagem(pcID)
    menuJogador()
            
def atualizarJogador(pcID,pcNome):
    pc.updatePc(pcID,pcNome)
    menuJogador()

def criarJogador(pcID,pcNome,pcEspecie):
    # --- Verificando se o id selecionado pelo usuario já existe no banco ---
    conferir = personagem.getPersonagemByID(pcID)
    if conferir is not None:
        print("\nEste ID já está em uso para algum jogador ou para algum npc")
        print("\033[1;33mDica: Selecione 'Ver jogadores' pra ver os que já foram criados\n")
        menuJogador()
        return
    if(pcEspecie != "Humano" and pcEspecie != "humano" and pcEspecie != "Povo Fogo" and pcEspecie != "Povo fogo" and pcEspecie != "povo fogo" and pcEspecie != "Povo Crystal" and pcEspecie != "Povo crystal" and pcEspecie != "povo crystal" and pcEspecie != "Vampiro" and pcEspecie != "vampiro"):
        print("\033[1;31mERROR: ESPÉCIE INVÁLIDA!\n")
        return
    #------------------------------------------------------------------------   
    criarPC = Pc()
    personagem.criarPersonagem(pcID, True) 
    criarPC.criarPc(pcID,pcNome,0,100,0,0,pcEspecie,5,0,0)
    definirHabilidadePersonagem(pcEspecie, pcID)
    ##inserirInventarioPersonagem(pcID)
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
            pcID = input("ID do jogador :")
            pcNome = input("Nome do jogador :")
            pcEspecie = input("|Especies: |\n|Humano|\n|Povo Fogo|\n|Povo Crystal|\n|Vampiro|:\n")
            criarJogador(pcID,pcNome,pcEspecie)
        case '2':
            print("\nPersonagens já criados:\n\n")
            print("\033[1;32mID | Nome | Xp | Pv | lvl | $ | Esp | For | Def | Local\033[0;36m")
            conf = pc.consultarPC()
            menuJogador()
                          
        case '3':
            NomedoJogador = input("Digite seu Nome")
            pcID = input("ID do jogador que você deseja atualizar o Nome:")
            pcNome = input("Novo Nome do jogador :")
            atualizarJogador(pcID,pcNome)
        case '4':
            pcID = input("ID do jogador que deseja deletar :")
            #Ordem de deleção: pc -> possuihab -> personagem
            deletarJogador(pcID)
            #tirar id de possuihab
            possuiHab.deletarPossuiHabALL(pcID)
            #tirar id de personagem
            personagem.deletarPersonagem(pcID)
