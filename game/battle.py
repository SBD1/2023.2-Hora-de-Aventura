from Banco import *
from random import randint
import sys, time, os

def print_devagar(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.041)

def print_um_pouco_mais_rapido(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)

def luta(idNPC: int, numInstancia: int, jogadorID: int):
   
    
    while(True):

        inimigo = Npc() #atributos do monstro que estao na tabela npc
        inimigoAux = Instancia() #atributos da tabela instancia, especificando qual monstro que é

                
        #pegando a vida da instancia
        i = inimigo.getNPCID(idNPC) # Pegando a informacao da tupla do monstro passado pela funcao
        iAux = inimigoAux.getInstanciaID(idNPC,numInstancia) # Acessando a informacao da instancia especifica do monstro
        
        ## verificando se instancia de monstro é valida
        if iAux is None:
            print_devagar("\nInimigo já foi derrotado ou não existe\n")
            break
        
        #carregando status vindos da tabela npc
        nome = i[0][1] 
        especie = i[0][5]
        nivel = i[0][4]
        forca = i[0][6]
        defesa = i[0][7]

        vidaInstacia = iAux[0][2]

        if(vidaInstacia <= 0):
            break
        #acessando informacoes do jogador
        jogador = Pc()
        statusJogador = jogador.getPC(jogadorID)
        nomeJogador = statusJogador[0][1]
        vidaJogador = statusJogador[0][3]
        nivelJogador = statusJogador[0][4]
        forcaJogador = statusJogador[0][7]
        defesaJogador = statusJogador[0][8]




        print_um_pouco_mais_rapido("\033[1;32m\n\n                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;32m                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;32m                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣽⣦⣀⡀⠤⠤⣤⣀⡀⠀⠀⠀⠀⠀          \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⠀⠀⠀⠀⣀⠴⠊⡉⠔⢛⠭⠉⡇⠙⢄⠈⠐⠮⡉⠒⠬⣑⠢⣀⠀⠀       \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⠀⠀⣠⠞⠁⡴⠋⠀⡰⠊⡀⠀⢸⠀⠀⢣⠀⠀⣦⢄⡀⠈⠣⡈⢧⡀          \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⠀⡔⠁⢀⠎⠀⠀⡰⢡⢮⣇⠀⢸⠀⠀⠀⠃⠀⣿⣦⡙⡄⠀⢷⡀⢃          \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⠸⠁⠀⡞⠀⠀⢀⣇⡇⣾⣿⣆⠀⠀⠀⠀⡸⠘⠛⠛⠛⡉ ⠀⠀⡇⢸         \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⡆⠀⢸⠀⠀⠀⢸⠉⠉⠉⠉⠁⠀⠀⢻⣿⢹⠀⠀⠀⠀⣠  ⠀⠀⠁⢸        \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⡇⠀⢸⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⡀⠀⠫⢾⠀⢀⣤⢞⠋⠀  ⢠⠃⠸        \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⢡⠀⠈⠀⠀⠀⠈⢳⡦⣄⣀⣤⣀⣧⣶⣤⣾⣿⣿⣣ ⢫⠀⠀⡏⢠⠆         \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⠈⢧⡀⠑⡀⠀⠀⠘⠝⠾⠿⣿⣿⡿⠿⡿⠛⠏⠉⠀⡜⢠⠞⣠⠏⠀          \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                       ⠀⠀⠳⣄⠈⢤⠀⠀⠈⢢⡀⠈⠋⡇⠀⠀⠸⠀⠀⡔⡠⣋⡴⠋⠀           \033[0m\n")
        print_um_pouco_mais_rapido("\033[1;34m                        ⠀⠀⠀⠈⠙⠲⠯⠶⢤⣀⣑⣦⣀⡇⠤⠴⠥⠴⠚⠈⠉⠁⠀⠀⠀⠀         \033[0m\n")

        print_devagar(f"\033[1;35mInimigo = \033[0m{nome}\n\033[1;35mEspecie = \033[0m{especie}\n\033[1;35mNivel = \033[0m{nivel}\n\033[1;35mVida = \033[0m{vidaInstacia}\n\n")
        print_devagar(f"{nomeJogador} | vida = {vidaJogador} | lvl = {nivelJogador} | dano = {forcaJogador} | defesa = {defesaJogador}\n\n")

        
        print_devagar("atacar/fugir?\n\n")
        opcao = input()
            
        match opcao:
            
            
            case 'atacar':
                
                #listar opcoes de ataque que o personagem possui: habilidades e itens do inventario que são do tipo armamento
                print_devagar("Voce pode atacar com habilidades, itens ou usar poção: (hab/it/poc)\n\n")
                atacar = input()

                if(atacar == "habilidade" or atacar == "hab" or atacar == "habilidades"):
                    print_devagar("\nhabilidades disponiveis:\n")
                    print_devagar("ID | Nome | Cooldown | Dano\n\n")
                    
                    consulta = PossuiHab()
                    habilidades = consulta.consultarPossuiHabPersonagem(jogadorID)
                    for i in habilidades:
                        print(i)

                    print_devagar("\nDigite apenas o id da habilidade!\n")   

                    hab = input()
                    if hab.isdigit():
                        
                        ID = consulta.getPossuiHabPK(jogadorID, hab)
                    else:
                        print_devagar("\n\033[1;31mIsso não é um número.\033[0m\n")
                        ID = None

                    if ID is not None:
                        danoAtaque = ID[0][3] + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)

                        danoMonstro = forca + randint(-4,3)
                        defesaMonstro = defesa + randint(-4,3)

                        danoInfligidoJogador = danoMonstro - defesaJogador
                        danoInfligidoMonstro = danoAtaque - defesaMonstro

                        os.system('cls')
                        print_devagar(f"jogador -{danoInfligidoJogador}\n")
                        print_devagar(f"monstro -{danoInfligidoMonstro}\n\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)
                        
                        if(danoInfligidoMonstro > 0):
                            novaVidaMonstro = vidaInstacia - danoInfligidoMonstro
                            inimigoAux.atualizarVidaInstanciaID(idNPC, numInstancia, novaVidaMonstro)
                    
                        if(novaVida <= 0):
                            print_um_pouco_mais_rapido("\033[0;31m   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁\033[0m\n")
                            break
                    else:
                        os.system('cls')
                        print_devagar("\nHabilidade inexistente\n")
                        
                        danoMonstro = forca + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)
                        danoInfligidoJogador = danoMonstro - defesaJogador

                        print_devagar(f"jogador -{danoInfligidoJogador}\n\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)
                            if(novaVida <= 0):
                                print_um_pouco_mais_rapido("\033[0;31m   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁\033[0m\n")
                                break

                
                elif(atacar == "i" or atacar == "item" or atacar == "it"):

                    print_devagar("\nItens disponiveis:\n")
                    print_devagar("ID | Nome | Dano\n\n")

                    inv = Inventario()
                    inv.consultarInventarioArmasID(jogadorID)

                    print_devagar("\nDigite apenas o id do item!\n")
                    item = input()
                    if item.isdigit():
                        
                        IDi = consulta.getPossuiHabPK(jogadorID, hab)
                    else:
                        print_devagar("\n\033[1;31mIsso não é um número.\033[0m\n")
                        IDi = None
                    IDi = inv.getInventarioArmasID(jogadorID, item)

                    if IDi is not None:
                        danoAtaque = IDi[0][2] + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)

                        danoMonstro = forca + randint(-4,3)
                        defesaMonstro = defesa + randint(-4,3)

                        danoInfligidoJogador = danoMonstro - defesaJogador
                        danoInfligidoMonstro = danoAtaque - defesaMonstro

                        os.system('cls')
                        print_devagar(f"jogador -{danoInfligidoJogador}\n")
                        print_devagar(f"monstro -{danoInfligidoMonstro}\n\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)

                        if(danoInfligidoMonstro > 0):
                            novaVidaMonstro = vidaInstacia - danoInfligidoMonstro
                            inimigoAux.atualizarVidaInstanciaID(idNPC, numInstancia, novaVidaMonstro)
                    
                        if(novaVida <= 0):
                            print_um_pouco_mais_rapido("\033[0;31m   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                            print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁\033[0m\n")
                            break

                    else:
                        os.system('cls')
                        print_devagar("\nItem inexistente\n")

                        danoMonstro = forca + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)
                        danoInfligidoJogador = danoMonstro - defesaJogador

                        print_devagar(f"jogador -{danoInfligidoJogador}\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)
                            if(novaVida <= 0):
                                print_um_pouco_mais_rapido("\033[0;31m   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                                print_um_pouco_mais_rapido("\033[0;31m    ⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁\033[0m\n")
                                break

                elif(atacar == "poção" or atacar == "poc" or atacar == "pocao"):
                    print_devagar("\nPoções disponiveis:\n")
                    print_devagar("ID | Nome | Cura | Usos\n\n")

                    inv2 = Inventario()
                    inv2.consultarInventarioConsumiveisID(jogadorID)

                    print_devagar("\nDigite apenas o ID da poção!\n")

                    IdPocao = input()
                    if IdPocao.isdigit():
                        
                        teste = inv2.getInventarioConsumiveisID(jogadorID, IdPocao)
                    else:
                        print_devagar("\n\033[1;31mIsso não é um número.\033[0m\n")
                        teste = None

                    os.system('cls')
                    if teste is not None:
                        novaVida = vidaJogador + teste[0][2]
                        jogador.atualizarVidaPCID(jogadorID, novaVida)
                    else:
                        os.system('cls')
                        print_devagar("\nPoção inexistente\n")
                
                if(vidaInstacia <= 0):
                    print_devagar("\nVoce derrotou o monstro\n")    

            case 'fugir':
                print_devagar("Você fugiu!\n")
                break

            case _:
                print_devagar("\nDigite uma das opcoes!\n")

