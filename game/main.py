from Banco import * 
import game

personagem = Personagem()
pc = Pc()

print("            ⠀⠀⠀⠀⠀⠀⠀⠰⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ")
print("            ⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ")
print("            ⠀⠀⠀⠀⠀⢀⣀⣼⣿⣀⣹⣿⡆⠀⢤⡄⢤⣄⢤⡤⠀⢤⣤⣤⣤⣤⢤⣄⠀⢤⣤⡤⣤⣤⣤⢠⡄⠀⣤⢤⡤⢤⡠⣤⠤⣴⠀⠀⠀⠀      ")
print("            ⠀⠀⠀⠀⠀⠈⢹⣿⡇⠉⠉⢿⣿⡄⢸⡇⠀⢹⡏⢿⣠⡟⢹⣿⠤⠄⢸⡿⣷⣼⡇⠀⣿⡇⠀⢸⡇⠀⡇⢸⡇⣎⠀⣿⠶⠌⠀⠀⠀⠀      ")
print("            ⠀⠀⠀⠀⠀⡴⠾⠿⠀⠀⠀⠘⠿⠿⠾⠿⠴⠛⠁⠘⠏⠀⠼⠿⠦⠖⠸⠃⠀⠙⠇⠀⠿⠇⠀⠘⠷⠚⠇⠾⠇⠘⠿⠿⠶⠶⠀⠀⠀        ") 
print("            ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⢠⣤⡤⠀⢲⣶⣶⡄⠀⠀⠀⣰⣶⣶⠖⠀⢲⣶⣶⠶⠶⢶⣶⠀⠀⠀⠀       ") 
print("            ⢀⣀⠀⠀⠀⠀⠀⢀⣸⣿⣉⣀⠀⢟⡉⠉⡉⣿⣿⢉⣉⣙⣛⣘⣿⣇⣀⡀⣿⢿⣿⡄⠀⣼⡿⣿⣿⢠⣤⣬⣭⣭⣤⣤⣤⣬⣤⣤⣀⠀       ")
print("            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⢇⣿⠰⠻⣿⣾⡿⠵⣿⣿⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠁       ")
print("            ⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⣍⠁⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢰⣶⡆⠀⣼⣿⡆⠀⠹⡿⠁⠀⣿⣿⡀⠀⣸⣿⣿⣤⣤⣤⣤⡆⠀⠀⠀       ")
print("            ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⠀⠀⠀⠀⠀⠴⠟⠛⠂⠀⠀⠀⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠻⠋⠀           ")
print("                                                                                ")
print("           ⣠⣴⠶⢶⣦⡀                                                              ")
print("          ⣰⡟⠁⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
print("      ⠀⠀⢀⡟⠀⠀⠀⠀⠀⣿⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⣼⠋⠀⠀⠈⢻⡆⠀⠀⢀⣠⣴⡶⠿⠛⠋⠉⠉⠉⠉⠉⠉⠉⠙⠛⠲⢤⣀⠀⠀⠀⠀⠀   ")
print("      ⠀⠀⣸⠁⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠳⢦⣼⠇⠀⠀⠀⠀⠈⣇⣠⣶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀   ")
print("      ⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠴⠶⠶⣶⣤⡀⠀⠀⠀⠀⠀⠙⢦⠀   ")
print("      ⠀⣼⠁⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠤⠤⠤⠤⠄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠈⢻⣿⡄⠀⠀⠀⠀⠀⠈⣧   ")
print("      ⢠⡿⠀⠀⠀⢀⡴⠊⠉⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠈⠉⠒⢤⡀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠠⣀⡀⠀⣠⡿   ")
print("      ⣸⡇⠀⠀⢠⠋⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣀⠀⠀⢀⣠⣾⠟⠀⠀⠀⠘⣿⣿⠋⠀   ")
print("      ⣿⠇⠀⠀⡇⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠇⠀⠀⠘⡄⢀⡇⠠⠒⠉⠙⠛⣶⣄⠀⣠⠤⠒⠒⠚⠚⠛⠿⢿⡛⠋⠁⠀⠀⠀⠀⠀⠘⣿⡇⠀   ")
print("      ⣿⠀⠀⠀⡇⠀⠀⠀⠀⢀⣿⣿⡏⠂⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠘⡇⠁⠀⠀⠀⠀⠈⣿⠋⠀⠀⢀⣀⣀⡀⠀⠀⠀⠈⠒⢄⠀⠀⠀⠀⠀⠀⣹⡇⠀   ")
print("      ⣿⠀⠀⠀⠘⡄⠀⠀⠀⠀⢿⣿⡿⢿⣿⣿⣄⣈⣯⣉⣉⡇⠀⠀⠀⠀⡜⠀⠇⢆⠀⠀⠀⠀⣰⠇⠀⢀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢀⣿⠁⠀   ")
print("      ⢹⣇⠀⠀⠀⠈⠢⣄⠀⠀⠈⠻⣦⣀⠀⠈⠉⠻⣿⣿⡿⠁⠀⠀⠀⡰⠁⠀⠘⡀⠑⠒⠒⠚⢻⠀⠀⠈⠛⡟⠛⠉⢀⠽⣦⣀⣀⣀⡠⠃⠀⠀⠀⢀⣾⠇⠀⠀   ")
print("      ⠀⢻⣦⠀⠀⠀⠀⠀⠙⠲⠤⣀⡀⠉⠛⠛⠛⠛⠉⠁⠀⢀⣠⠴⠊⠀⠀⠀⠀⢱⡄⠀⠀⠀⠘⡀⠀⠀⠀⣿⣤⣦⡼⠊⠉⡹⠁⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀   ")
print("      ⠀⠀⠙⢷⣦⣀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠒⠒⠒⠒⠚⠉⠁⠀⠀⠀⠀⠀⠀⡠⠋⠙⢦⡀⠀⠀⠐⠠⠀⠔⠁⠈⠛⠣⠄⠚⠁⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀⠀   ")
print("      ⠀⠀⠀⠀⠉⠛⠿⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⠋⠀⠀⠀⠀⠙⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀   ")
print("      ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠻⠷⠶⠶⠶⠶⠶⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠷⠶⠶⠶⠶⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
print("                                                                               ")
print("                             A aventura vai começar                            ")
print("                             Todos juntos vamos                                ")
print("                             Visitar                                           ")
print("                             O mundo de Jake e seu amigo Finn                  ")
print("                             Diversão é aqui!                                  ")
print("                             Hora de aventura!                                 ")
    
while(True):

    print("\n\033[1;32m| Bem-vindo ao MUD Hora de Aventura |\033[0m\n")
    print("\033[0;36m|1| = Acessar Menu")
    print("|2| = Criar Personagem(PC)")
    print("|3| = Carregar Jogo")
    print("|4| = Ver localização")
    print("|5| = Fechar jogo\n")        
    
    print("\033[1;32mEscolha uma opção de 1 a 5:\033[0m\n")
    opcao = input()
    match opcao:
        case '1':  
                
            print("\033[1;32mOpções de jogador:\033[0m")
            print("     1 = Ver jogador")
            print("     2 = Atualizar jogador")
            print("     3 = Deletar jogador")
            print("     4 = Voltar")
            menuJogador = input()
            
            match menuJogador:
                case '1':  
                    print("Deseja ver todos os jogadores ou um jogador especifico?: 1 = Todos/ 2 = Jogador")
                    escolhaMenujogador = input("Escolher entre 1 e 2: ")
                        
                    if(escolhaMenujogador == '1'):
                        pc.consultarPC()
                            
                    if(escolhaMenujogador == '2'):
                        IDdoJogador = input("Digite o ID do jogador que busca:")
                        pc.consultarPCID(IDdoJogador)
                case '4':
                    print("\n--------------------------------------------------------------------------------\n")

                        
        case '2':
            print("Digite suas caracteristicas")
            pcID = input("ID:")
            pcNome = input("Nome:")
            pcEspecie = input("Especie:")
            criarPC = Pc()
            personagem.criarPersonagem(pcID, False)
            criarPC.criarPc(pcID,pcNome,0,100,0,0,pcEspecie,5,0,0)
                
        case'3':
            jogador=game.CarregarJogo()
            lc=Local()
            posicao=lc.getLocalPc(jogador[0])

            print("\n--------------------------------------------------------------------------------\n")
            print(f"\033[1;32m{jogador[1]}\nLocal: {posicao[0][2]}\nDescrição: {posicao[0][1]}\nCoordenada: {posicao[0][0]}\033[0m")
            print("\n--------------------------------------------------------------------------------\n")
            salas=game.EncontrarSalas(jogador[9])
            print(salas)

            print("\n"+80*"-"+"\n")
        case '4':
            print("Localização")
            print("\n--------------------------------------------------------------------------------\n")
        case '5':
           print("Finalizando o jogo.....")
           break    
             