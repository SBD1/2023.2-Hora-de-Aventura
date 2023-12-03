from Banco import *
from random import randint


#funcao localizar persogem mostra coordenada do local
#funcao pega essa coordenada e vê quais instancias de monstro estao no local
#chamar a funcao de lutar, passando numero e id da instancia, e o id do personagem que vem da main

#select i.personagem,i.numero, i.vida, n.nome, n.vidamax, n.especie, n.lvl, n.forca, n.defesa from instancia i
#join npc n
#on i.personagem = n.personagem;
#luta(nome: str, especie: str, forca: int, defesa: int, vidaInstacia: int):

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
                print("Voce pode atacar com habilidades ou itens: (hab/it)\n")
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
                        danoAtaque = ID[0][3] + randint(-10,10)
                        defesa = defesaJogador + randint(-10,10)

                        danoMonstro = forca + randint(-10,10)
                        defesaMonstro = defesa + randint(-10,10)

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
                        danoMonstro = forca + randint(-10,10)
                        defesa = defesaJogador + randint(-10,10)
                        danoInfligidoJogador = danoMonstro - defesaJogador

                        print(f"jogador{danoInfligidoJogador}\n")

                        if(danoInfligidoJogador > 0):
                            novaVida = vidaJogador - danoInfligidoJogador
                            jogador.atualizarVidaPCID(jogadorID, novaVida)

                
                #if(atacar == "i" or atacar == "item" or atacar == "it"):




                        
                    #ao atacar, fazer o sistema de dano. Decrementar da vida da instancia o dano do personagem
                    #e ver quanto de dano tira dependendo da defesa do npc monstro
                    #se a vida do personagem ou do monstro for <=0 parar luta
                    #se a instancia tiver perdido, deletar instancia da tabela instancias
                    #se o personagem tiver perdido GAME OVER, mandar pro spawn ou inicio da dungeon
                    #ao final, tem que atualizar no banco as duas tabelas de qualquer forma
                    #porque a vida que o personagem perdeu na batalha continua perdida 
                    
                
            case 'fugir':
                print("voce foge\n")
                break

            case _:
                print("\nDigite uma das opcoes!\n")

    if(vidaInstacia <= 0):
        print("\nVoce derrotou o monstro\n")

luta(3, 1, 4)





##def luta(forca: int, nome: str, especie: str, defesa: int, vidaInstacia: int, instanciaNum: int):