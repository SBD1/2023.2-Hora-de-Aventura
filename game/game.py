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
prereqmiss = PreRequisitoMissao()

def CarregarJogo():
    print("\nPersonagens já criados:\n\n")
    print("\033[1;32mID | Nome | Xp | Pv | lvl | $ | Esp    | For | Def | Local\033[0;36m")
    conf = pc.consultarPC()
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    clear()
    while(True):
        posicao=lc.getLocalPc(jogador[0][0])
        print("\n"+80*"-"+"\n")
        print(f"\033[1;32m{jogador[0][1]}\nLocal: {posicao[0][2]}\nDescrição: {posicao[0][1]}\nCoordenada: {posicao[0][0]}\033[0m")
        
        ameacas = instancia.getInstanciasLocais(posicao[0][0])
        lojas = loja.getLojaLocal(posicao[0][0])
        missao = lc.verMissaoLocal(posicao[0][0])
        
        print("\n"+80*"-"+"\n")
        print("\033[0;36m|1| = Mudar de sala\n|2| = Voltar para o menu principal\n|3| = Lutar\n|4| = Comprar na loja\n|5| = Ver status completo\n"
              "|6| = Vizualizar Inventário\n|7| = Evolução de Personagem\n|8| = Ver missão\033[0m")
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
            case '8':
                local = input("Digite o ID do seu local:").strip()
                verMissaoNoLocal(local)       
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

def verMissaoNoLocal(local:int):
    verMissao = lc.verMissaoLocal(local) 
    missoes = [f"\nMissão: {x[1]}\nDescrição:{x[2]}\nRecompensa:{x[3]}" for x in verMissao]
    for y in missoes:
        print(y)
    dependencia = input("\nDeseja ver dependencias de missão? Sim/Não\n")
    if (dependencia == 'Sim' or 's' or 'ss' or 'SS'or 'Ss' or 'sS' ):
        missoes = [f"\nMissão: {x[1]}" for x in verMissao]
        for y in missoes:
            print(y)
        nomeMissao = input("\nDigite qual das missões ?\n")
        missao = prereqmiss.consultarPreRequisitoNomeMissao(nomeMissao)
        print(f"\nA missão {nomeMissao} é pré-requisito de:")
        missoes = [f"\nMissão: {y[0]}\nDescricao:{y[1]}\nRecompensa:{y[2]}\n" for y in missao]
        for z in missoes:
                print(z)
    else:
        print("Digite sim ou não !")
                   
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
    Hab=possuiHab.consultarPossuiHabPersonagem(jogador[0][0])
    for i in Hab:
        print(i)

def Evolucao(Id:int):
    jogador=pc.getPC(Id)
    Id=jogador[0][0]
    Xp=jogador[0][2]
    Vida = jogador[0][3]
    LvL = jogador[0][4]
    Forca = jogador[0][7]
    Defesa = jogador[0][8]

    print("\n"+80*"-"+"\n")
    print("Você pode gastar 100 de Xp para subir de nível ou 150 de Xp para aprender novas habilidades\n\n"
        f"Você está no nível \033[1;32m{LvL}\033[0m e possui \033[1;32m{Xp}\033[0m de Xp\n")
    print("\033[0;36m|1| = Subir de nível\n|2| = Aprender Habilidades\n\033[0m")
    opcao = input()
    match opcao:
        case '1': # Subir de Nível
            NovoXp=Xp-100
            NovoLvl=LvL+1
            NovaVida=Vida+10
            NovaForca=Forca+2
            NovaDefesa=Defesa+2
            print(f'\nNovos Atributros: \n\nNível = \033[90m{LvL}\033[0m -> \033[1;32m{NovoLvl}\033[0m\n'
                  f'Vida = \033[90m{Vida}\033[0m -> \033[1;32m{NovaVida}\033[0m\nForça = \033[90m{Forca}\033[0m -> \033[1;32m{NovaForca}\033[0m\n'
                  f'Defesa = \033[90m{Defesa}\033[0m -> \033[1;32m{NovaDefesa}\033[0m\nXp = \033[90m{Xp}\033[0m -> \033[1;32m{NovoXp}\033[0m\n'
                  '\nDigite 1 para confirmar ou -1 para cancelar')
            opcao2 = input()
            if opcao2 == '1':
                if Xp >= 100: # Aumenta os atributos do jogador

                    pc.PcSubirNivel(Id,NovoXp,NovoLvl,NovaVida,NovaForca,NovaDefesa)
                    clear()
                    print(f"Você subiu de nível e agora está no nível \033[1;32m{NovoLvl}\033[0m!\n")
                else:
                    clear()
                    print("Você não possui Xp suficiente para subir de nível!\n")
            else:
                clear()
        case '2': # Aprender Habilidades
            Evo=possuiHab.consultarEvolucoesHabilidade(Id)
            if not Evo: # Caso não existam evoluções encerra a função
                return 0
            Hab=possuiHab.consultarPossuiHabPersonagem(Id)
            Lista=[]
            for i in Hab:
                Lista.append(i[0])
            print("Você pode aprender as seguintes habilidades:\n")
            for i in Evo: # Printa os opções de escolha
                if i[0] not in Lista:
                    #print(f"ID = \033[1;32m{i[0]}\033[0m | Nome = \033[1;32m{i[1]}\033[0m | Dano = \033[1;32m{i[2]}\033[0m | Cooldown = \033[1;32m{i[3]}\033[0m")
                    print(f"\033[1;32mID\033[0m = {i[0]} | \033[1;32mNome\033[0m = {i[1]} | \033[1;32mDano\033[0m = {i[2]} | \033[1;32mCooldown\033[0m = {i[3]}")
            
            print("\nDigite o ID da habilidade que deseja aprender. Digite -1 para cancelar")
            escolha=int(input())
            if escolha == -1:
                clear()
            for i in Evo:
                if(i[0]==escolha):
                    if Xp >=150:
                        NovoXp=Xp-150
                        possuiHab.adicionarHabJogador(Id,escolha,NovoXp)
                        print(f'Você aprendeu a Habilidade: {i[1]}')
                    else:
                        clear()
                        print("Você não possui Xp suficiente para aprender essa habilidade!\n")
                    


 

 