from Banco import *
from battle import *

pc = Pc()
personagem = Personagem()
possuiHab = PossuiHab()
lc=Local()
loja = Loja()
instancia = Instancia()
instanciaItem = Instanciaitem()
inventario = Inventario()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    clear()
    while(True):
        posicao=lc.getLocalPc(jogador[0][0])
        print("\n"+80*"-"+"\n")
        print(f"\033[1;32m{jogador[0][1]}\nLocal: {posicao[0][2]}\nDescrição: {posicao[0][1]}\nCoordenada: {posicao[0][0]}\033[0m")
        
        ameacas = instancia.getInstanciasLocais(posicao[0][0])
        lojas = loja.getLojaLocal(posicao[0][0])
        
        print("\n"+80*"-"+"\n")
        print("\033[0;36m|1| = Mudar de sala\n|2| = Voltar para o menu principal\n|3| = Lutar\n|4| = Comprar na loja\n|5| = Ver status completo\n"
              "|6| = Vizualizar Inventário\n|7| = Evolução de Personagem\033[0m")
        opcao = input()
        match opcao:
            case '1':
                EncontrarSalas(posicao[0][0], jogador[0][0])
            case '2':
                clear()
                print_devagar("\033[31;1;4m\nVoltando para o menu principal\n\033[0m")
                break
            case '3':
                if ameacas is None:
                    print_devagar("\nMas não tem ninguém pra lutar. Ué?\n")
                else:                  
                    print_devagar("\n\033[1mDigite o ID, e apenas o ID, do inimigo\033[0m\n")              
                    IDbat = input()
                    print_devagar("\n\033[1mDigite o numero, e apenas o numero, do inimigo\033[0m\n")
                    numBat = input()
                    if IDbat.isdigit() and numBat.isdigit():                        
                        verificador = instancia.conferirInstanciaDoLocalPersonagem(posicao[0][0], IDbat, numBat)
                    else:
                        print_devagar("\n\033[1;31mIsso não é um número.\033[0m\n")
                        verificador = None
                    if verificador is not None:
                        luta(IDbat, numBat, Save)
                    else:
                        print_devagar("\n\033[1mEssa monstro não está aqui. Talvez nem exista\033[0m\n")   
            case '4':
                if not lojas:
                    print_devagar("\nComprar a onde?? Não tem nada aqui!\n")
                elif lojas:
                    ## função mostrando os itens que a loja vende
                    loja.getItensLoja(lojas[0][0])

                    print_devagar("\n\033[1mDigite um id para comprar algum item. Ou <n> pra não comprar\033[0m\n")
                    
                    ##Conferir se o item selecionado está na loja
                    digitado = input()
                    if digitado.isdigit():
                        ##Conferir se o item está na loja
                        verificacao1 = loja.getItemDaLoja(lojas[0][0], digitado)

                        if verificacao1:
                            ##Conferir se o jogador tem dinheiro pra comprar o item
                            qwert = pc.getPCbyID(Save)
                            dinheiro = qwert[0][5]
                            precoDoItem = verificacao1[0][3]
                            
                            novoSaldo = dinheiro - precoDoItem
                            if(novoSaldo >= 0):
                                ##Realizar uma transaction criando a instancia e movendo pro inventario do jogador
                                loja.compraDoItem(verificacao1[0][0], Save, novoSaldo, jogador[0][0])
                                
                            else:
                                print_devagar("\nDinheiro insuficiente\n")
                        else:
                            print_devagar("\nA Loja não possui este item\n")
                    
                    elif(digitado == 'n'):
                        print_devagar("\nFoi um prazer ter você em nossa loja!")
                    else:
                        print_devagar("\n\033[1;31mISSO NÃO É UM NUMERO!!!.\033[0m\n")
            case '5':
                StatusJogador(jogador[0][0])

            case '6':
                inventario.verItensInventario(jogador[0][0])

            case '7':
                Evolucao(jogador[0][0])
                    
            case _:
                print("\nOpção inválida\n")    
                

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
            clear()
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

def definirHabilidadePersonagem(pcEspecie):
    possuiHab = PossuiHab()       
    match pcEspecie:
        ## --- Humanous ---
        case 'Humano':
            possuiHab.inserirPossuiHabIncremento(20)
        
        case 'humano':
            possuiHab.inserirPossuiHabIncremento(20)
        
        ## --- Povo do fogo ---
        case 'Povo fogo':
            possuiHab.inserirPossuiHabIncremento(3)
        
        case 'Povo Fogo':
            possuiHab.inserirPossuiHabIncremento(3)
        
        case 'povo fogo':
            possuiHab.inserirPossuiHabIncremento(3)
        
        ## --- Povo do crystal ---
        case 'Povo crystal':
            possuiHab.inserirPossuiHabIncremento(7)
        
        case 'Povo Crystal':
            possuiHab.inserirPossuiHabIncremento(7)
        
        case 'povo crystal':
            possuiHab.inserirPossuiHabIncremento(7)
                
        ## --- Vampirous ---        
        case 'Vampiro':
            possuiHab.inserirPossuiHabIncremento(4)
        
        case 'vampiro':
            possuiHab.inserirPossuiHabIncremento(4)

        ## --- Nao digitou nenhuma opcao valida ---
        case _:
            print("\nDigite uma opção válida\n")
            menuJogador()
            
def deletarJogador(pcID):
    pc.deletarPC(pcID)
    
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

def criarJogador(pcNome,pcEspecie):
    if(pcEspecie != "Humano" and pcEspecie != "humano" and pcEspecie != "Povo Fogo" and 
            pcEspecie != "Povo fogo" and pcEspecie != "povo fogo" 
            and pcEspecie != "Povo Crystal" 
            and pcEspecie != "Povo crystal" 
            and pcEspecie != "povo crystal" 
            and pcEspecie != "Vampiro" 
            and pcEspecie != "vampiro"): 
                print("\033[1;31mERROR: ESPÉCIE INVÁLIDA!\n")
                return
    #------------------------------------------------------------------------   
    criarPC = Pc()
    personagem.criarPersonagemIncrementoID(True) 
    criarPC.criarPc(pcNome,0,100,0,0,pcEspecie,5,0,0)
    definirHabilidadePersonagem(pcEspecie)
    #inventario.inserirInventario(pcID, 0, pcID)
    #inserirInventarioPersonagem(pcID)
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
           # pcID = input("ID do jogador :")
            pcNome = input("Nome do jogador :")
            pcEspecie = input("|Especies: |\n|Humano|\n|Povo Fogo|\n|Povo Crystal|\n|Vampiro|:\n")
            criarJogador(pcNome,pcEspecie)
        case '2':
            print("\nPersonagens já criados:\n\n")
            print("\033[1;32mID | Nome | Xp | Pv | lvl | $ | Esp    | For | Def | Local\033[0;36m")
            conf = pc.consultarPC()
            print("\nVer personagem em específico:\n\n")
            pcID = input("ID do jogador :")
            NomedoJogador = input("Digite o Nome do jogador(es) que busca:")
            print("\n")
            verJogadorOp(NomedoJogador,pcID)
                          
        case '3':
            NomedoJogador = input("Digite seu Nome")
            pcID = input("ID do jogador que você deseja atualizar o Nome:")
            pcNome = input("Novo Nome do jogador :")
            atualizarJogador(pcID,pcNome)
        case '4':
            pcID = input("ID do jogador que deseja deletar :")
            #Ordem de deleção: itens do inventário -> inventário -> pc -> possuihab -> personagem 
            ##deletar itens do inventario
            instanciaItem.deletarInstanciaItemIDinv(pcID)
            ##deletar inventario
            inventario.deletarInventario(pcID)
            #deleta pc
            deletarJogador(pcID)
            #tirar id de possuihab
            possuiHab.deletarPossuiHabALL(pcID)
            #tirar id de personagem
            personagem.deletarPersonagem(pcID)
            #

def StatusJogador(Id:int):
    clear()
    jogador=pc.getPC(Id)
    print(f'\033[35mID = {jogador[0][0]}\n')
    print(f'Nome = {jogador[0][1]}\n')
    print(f'XP = {jogador[0][2]}\n')
    print(f'Vida = {jogador[0][3]}\n')
    print(f'LvL = {jogador[0][4]}\n')
    print(f'Dinheiro = {jogador[0][5]}\n')
    print(f'Espécie = {jogador[0][6]}\n')
    print(f'Força = {jogador[0][7]}\n')
    print(f'Defesa = {jogador[0][8]}\n')
    print(f'Local = {jogador[0][9]}\033[0m\n')

def Evolucao(Id:int):
    jogador=pc.getPC(Id)
    Xp=jogador[0][2]
    Vida = jogador[0][3]
    LvL = jogador[0][4]
    Forca = jogador[0][7]
    Defesa = jogador[0][8]

    print("\n"+80*"-"+"\n")
    print(f"Você está no nível \033[1;32m{LvL}\033[0m e possui \033[1;32m{Xp}\033[0m de Xp\n")
    print("\033[0;36m|1| = Gastar 100 de Xp para subir de nível\n|2| = Melhorar Habilidades\n\033[0m")
    opcao = input()
    match opcao:
        case '1':
            if Xp >= 100: # Aumenta os atributos do jogador
                NovoXp=Xp-100
                NovoLvl=LvL+1
                NovaVida=Vida+10
                NovaForca=Forca+2
                NovaDefesa=Defesa+2
                pc.PcSubirNivel(jogador[0][0],NovoXp,NovoLvl,NovaVida,NovaForca,NovaDefesa)
                clear()
                print(f"Você subiu de nível e agora está no nível \033[1;32m{NovoLvl}\033[0m!\n")
            else:
                clear()
                print("Você não possui Xp suficiente para subir de nível!\n")

