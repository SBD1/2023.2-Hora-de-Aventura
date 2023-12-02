from Banco import *

#funcao localizar persogem mostra coordenada do local
#funcao pega essa coordenada e vê quais instancias de monstro estao no local
#chamar a funcao de lutar, passando numero e id da instancia, e o id do personagem que vem da main

#select i.personagem,i.numero, i.vida, n.nome, n.vidamax, n.especie, n.lvl, n.forca, n.defesa from instancia i
#join npc n
#on i.personagem = n.personagem;
#luta(nome: str, especie: str, forca: int, defesa: int, vidaInstacia: int):

def luta(idNPC: int, numInstancia: int, jogadorID: int):
    
    inimigo = Npc() #atributos do monstro que estao na tabela npc
    inimigoAux = Instancia() #atributos da tabela instancia, especificando qual monstro que é

    i = inimigo.getNPCID(idNPC) # Pegando a informacao da tupla do monstro passado pela funcao
    iAux = inimigoAux.getInstanciaID(idNPC,numInstancia) # Acessando a informacao da instancia especifica do monstro
    
    #carregando status vindos da tabela npc
    nome = i[0][1] 
    especie = i[0][5]
    nivel = i[0][4]
    forca = i[0][6]
    defesa = i[0][7]

    #pegando a vida da instancia
    vidaInstacia = iAux[0][2]

    #acessando informacoes do jogador
    jogador = Pc()
    statusJogador = jogador.getPC(jogadorID)
    nomeJogador = statusJogador[0][1]
    vidaJogador = statusJogador[0][3]
    nivelJogador = statusJogador[0][4]
    forcaJogador = statusJogador[0][7]
    defesaJogador = statusJogador[0][8]




    print("\033[1;32m                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   \033[0m")
    print("\033[1;32m                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       \033[0m")
    print("\033[1;32m                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣽⣦⣀⡀⠤⠤⣤⣀⡀⠀⠀⠀⠀⠀      \033[0m")
    print("                       ⠀⠀⠀⠀⣀⠴⠊⡉⠔⢛⠭⠉⡇⠙⢄⠈⠐⠮⡉⠒⠬⣑⠢⣀⠀⠀    ")
    print("                       ⠀⠀⣠⠞⠁⡴⠋⠀⡰⠊⡀⠀⢸⠀⠀⢣⠀⠀⣦⢄⡀⠈⠣⡈⢧⡀     ")
    print("                       ⠀⡔⠁⢀⠎⠀⠀⡰⢡⢮⣇⠀⢸⠀⠀⠀⠃⠀⣿⣦⡙⡄⠀⢷⡀⢃     ")
    print("                       ⠸⠁⠀⡞⠀⠀⢀⣇⡇⣾⣿⣆⠀⠀⠀⠀⡸⠘⠛⠛⠛⡉ ⠀⠀⡇⢸    ")
    print("                       ⡆⠀⢸⠀⠀⠀⢸⠉⠉⠉⠉⠁⠀⠀⢻⣿⢹⠀⠀⠀⠀⣠  ⠀⠀⠁⢸    ")
    print("                       ⡇⠀⢸⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⡀⠀⠫⢾⠀⢀⣤⢞⠋⠀  ⢠⠃⠸    ")
    print("                       ⢡⠀⠈⠀⠀⠀⠈⢳⡦⣄⣀⣤⣀⣧⣶⣤⣾⣿⣿⣣ ⢫⠀⠀⡏⢠⠆    ")
    print("                       ⠈⢧⡀⠑⡀⠀⠀⠘⠝⠾⠿⣿⣿⡿⠿⡿⠛⠏⠉⠀⡜⢠⠞⣠⠏⠀     ")
    print("                       ⠀⠀⠳⣄⠈⢤⠀⠀⠈⢢⡀⠈⠋⡇⠀⠀⠸⠀⠀⡔⡠⣋⡴⠋⠀       ")
    print("                        ⠀⠀⠀⠈⠙⠲⠯⠶⢤⣀⣑⣦⣀⡇⠤⠴⠥⠴⠚⠈⠉⠁⠀⠀⠀⠀    ")

    print(f"Inimigo = {nome}\nEspecie = {especie}\nNivel = {nivel}\nVida = {vidaInstacia}\n\n")
    print(f"{nomeJogador} | vida = {vidaJogador} | lvl = {nivelJogador} | dano = {forcaJogador} | defesa = {defesaJogador}\n\n")


    print("atacar/fugir?\n\n")
    opcao = input()
        
    match opcao:
        
        case 'atacar':
            #atacar
            #listar opcoes de ataque que o personagem possui: habilidades e itens do inventario que são do tipo armamento
            



            #ao atacar, fazer o sistema de dano. Decrementar da vida da instancia o dano do personagem
            #e ver quanto de dano tira dependendo da defesa do npc monstro
            #se a vida do personagem ou do monstro for <=0 parar luta
            #se a instancia tiver perdido, deletar instancia da tabela instancias
            #se o personagem tiver perdido GAME OVER, mandar pro spawn ou inicio da dungeon
            #ao final, tem que atualizar no banco as duas tabelas de qualquer forma
            #porque a vida que o personagem perdeu na batalha continua perdida 
            print("Voce ataca o inimigo\n")
            
        case 'fugir':
            print("voce foge\n")

luta(1, 1, 4)





##def luta(forca: int, nome: str, especie: str, defesa: int, vidaInstacia: int, instanciaNum: int):