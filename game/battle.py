from Banco import *
from random import randint

def luta(idNPC: int, numInstancia: int, jogadorID: int):
   
    
    while(True):
        inimigo = Npc() #atributos do monstro que estao na tabela npc

        i = inimigo.getNPCID(idNPC) # Pegando a informacao da tupla do monstro passado pela funcao
        
        #carregando status vindos da tabela npc
        nome = i[0][1] 
        especie = i[0][5]
        nivel = i[0][4]
        forca = i[0][6]
        defesa = i[0][7]

        #pegando a vida da instancia
        inimigoAux = Instancia() #atributos da tabela instancia, especificando qual monstro que é
        iAux = inimigoAux.getInstanciaID(idNPC,numInstancia) # Acessando a informacao da instancia especifica do monstro
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




        print("\033[1;32m\n\n                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \033[0m")
        print("\033[1;32m                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          \033[0m")
        print("\033[1;32m                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣽⣦⣀⡀⠤⠤⣤⣀⡀⠀⠀⠀⠀⠀          \033[0m")
        print("\033[1;34m                       ⠀⠀⠀⠀⣀⠴⠊⡉⠔⢛⠭⠉⡇⠙⢄⠈⠐⠮⡉⠒⠬⣑⠢⣀⠀⠀       \033[0m")
        print("\033[1;34m                       ⠀⠀⣠⠞⠁⡴⠋⠀⡰⠊⡀⠀⢸⠀⠀⢣⠀⠀⣦⢄⡀⠈⠣⡈⢧⡀          \033[0m ")
        print("\033[1;34m                       ⠀⡔⠁⢀⠎⠀⠀⡰⢡⢮⣇⠀⢸⠀⠀⠀⠃⠀⣿⣦⡙⡄⠀⢷⡀⢃          \033[0m ")
        print("\033[1;34m                       ⠸⠁⠀⡞⠀⠀⢀⣇⡇⣾⣿⣆⠀⠀⠀⠀⡸⠘⠛⠛⠛⡉ ⠀⠀⡇⢸         \033[0m ")
        print("\033[1;34m                       ⡆⠀⢸⠀⠀⠀⢸⠉⠉⠉⠉⠁⠀⠀⢻⣿⢹⠀⠀⠀⠀⣠  ⠀⠀⠁⢸        \033[0m  ")
        print("\033[1;34m                       ⡇⠀⢸⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⡀⠀⠫⢾⠀⢀⣤⢞⠋⠀  ⢠⠃⠸        \033[0m  ")
        print("\033[1;34m                       ⢡⠀⠈⠀⠀⠀⠈⢳⡦⣄⣀⣤⣀⣧⣶⣤⣾⣿⣿⣣ ⢫⠀⠀⡏⢠⠆         \033[0m ")
        print("\033[1;34m                       ⠈⢧⡀⠑⡀⠀⠀⠘⠝⠾⠿⣿⣿⡿⠿⡿⠛⠏⠉⠀⡜⢠⠞⣠⠏⠀          \033[0m ")
        print("\033[1;34m                       ⠀⠀⠳⣄⠈⢤⠀⠀⠈⢢⡀⠈⠋⡇⠀⠀⠸⠀⠀⡔⡠⣋⡴⠋⠀           \033[0m  ")
        print("\033[1;34m                        ⠀⠀⠀⠈⠙⠲⠯⠶⢤⣀⣑⣦⣀⡇⠤⠴⠥⠴⠚⠈⠉⠁⠀⠀⠀⠀         \033[0m ")

        print(f"Inimigo = {nome}\nEspecie = {especie}\nNivel = {nivel}\nVida = {vidaInstacia}\n\n")
        print(f"{nomeJogador} | vida = {vidaJogador} | lvl = {nivelJogador} | dano = {forcaJogador} | defesa = {defesaJogador}\n\n")


        print("atacar/fugir?\n\n")
        opcao = input()
            
        match opcao:
            
            
            case 'atacar':
                
                #listar opcoes de ataque que o personagem possui: habilidades e itens do inventario que são do tipo armamento
                print("Voce pode atacar com habilidades, itens ou usar poção: (hab/it/poc)\n")
                atacar = input()

                if(atacar == "habilidade" or atacar == "hab" or atacar == "habilidades"):
                    print("habilidades disponiveis:\n")
                    print("ID | Nome | Cooldown | Dano\n\n")
                    
                    consulta = PossuiHab()
                    consulta.consultarPossuiHabPersonagem(jogadorID)

                    print("\nDigite apenas o id da habilidade!\n")   

                    hab = input()
                    ID = consulta.getPossuiHabPK(jogadorID, hab)
                    if ID is not None:
                        danoAtaque = ID[0][3] + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)

                        danoMonstro = forca + randint(-4,3)
                        defesaMonstro = defesa + randint(-4,3)

                        danoInfligidoJogador = danoMonstro - defesaJogador
                        danoInfligidoMonstro = danoAtaque - defesaMonstro

                        print(f"jogador -{danoInfligidoJogador}")
                        print(f"monstro -{danoInfligidoMonstro}")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)
                        
                        if(danoInfligidoMonstro > 0):
                            novaVidaMonstro = vidaInstacia - danoInfligidoMonstro
                            inimigoAux.atualizarVidaInstanciaID(idNPC, numInstancia, novaVidaMonstro)
                    
                    else:
                        danoMonstro = forca + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)
                        danoInfligidoJogador = danoMonstro - defesaJogador

                        print(f"jogador{danoInfligidoJogador}\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)

                
                elif(atacar == "i" or atacar == "item" or atacar == "it"):

                    print("\n itens disponiveis:\n")
                    print("ID | Nome | Dano\n\n")

                    inv = Inventario()
                    inv.consultarInventarioArmasID(jogadorID)

                    print("\nDigite apenas o id do item!\n")
                    item = input()
                    IDi = inv.getInventarioArmasID(jogadorID, item)  

                    if IDi is not None:
                        danoAtaque = IDi[0][2] + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)

                        danoMonstro = forca + randint(-4,3)
                        defesaMonstro = defesa + randint(-4,3)

                        danoInfligidoJogador = danoMonstro - defesaJogador
                        danoInfligidoMonstro = danoAtaque - defesaMonstro

                        print(f"jogador -{danoInfligidoJogador}")
                        print(f"monstro -{danoInfligidoMonstro}")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)
                        
                        if(danoInfligidoMonstro > 0):
                            novaVidaMonstro = vidaInstacia - danoInfligidoMonstro
                            inimigoAux.atualizarVidaInstanciaID(idNPC, numInstancia, novaVidaMonstro)
                    
                    else:
                        danoMonstro = forca + randint(-4,3)
                        defesa = defesaJogador + randint(-4,3)
                        danoInfligidoJogador = danoMonstro - defesaJogador

                        print(f"jogador -{danoInfligidoJogador}\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)

                elif(atacar == "poção" or atacar == "poc" or atacar == "pocao"):
                    print("\nPoções disponiveis:\n")
                    print("ID | Nome | Cura | Usos\n\n")

                    inv2 = Inventario()
                    inv2.consultarInventarioConsumiveisID(jogadorID)

                    print("\nDigite apenas o ID da poção!\n")

                    IdPocao = input()
                    teste = inv2.getInventarioConsumiveisID(jogadorID, IdPocao)

                    if teste is not None:
                        novaVida = vidaJogador + teste[0][2]
                        jogador.atualizarVidaPCID(jogadorID, novaVida)                    
                
            case 'fugir':
                print("Você fugiu!\n")
                break

            case _:
                print("\nDigite uma das opcoes!\n")

    if(vidaInstacia <= 0):
        print("\nVoce derrotou o monstro\n")

luta(3, 1, 4)
