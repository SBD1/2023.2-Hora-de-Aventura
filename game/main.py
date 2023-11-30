from Banco import * 

personagem = Personagem()
pc = Pc()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.consultarPCID(Save)
    return jogador[0]

print("\033[1;31m _   _                       _         ___                  _                   ")
print("| | | |                     | |       / _ \                | |                  ")
print("| |_| | ___  _ __ __ _    __| | ___  / /_\ \_   _____ _ __ | |_ _   _ _ __ __ _ ")
print("|  _  |/ _ \| '__/ _` |  / _` |/ _ \ |  _  \ \ / / _ \ '_ \| __| | | | '__/ _` |")
print("| | | | (_) | | | (_| | | (_| |  __/ | | | |\ V /  __/ | | | |_| |_| | | | (_| |")
print("\_| |_/\___/|_|  \__,_|  \__,_|\___| \_| |_/ \_/ \___|_| |_|\__|\__,_|_|  \__,_|\033[0m")

while(True):

    print("\n\033[1;32m| Bem-vindo ao MUD Hora de Aventura |\033[0m\n")
    print("\033[0;36m|1| = Acessar Menu")
    print("|2| = Criar Personagem(PC)")
    print("|3| = Fazer party")
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
            jogador=CarregarJogo()

            
            print("oi party")
            print(jogador[1])
            print("\n--------------------------------------------------------------------------------\n")
        case '4':
            print("Localização")
            print("\n--------------------------------------------------------------------------------\n")
        case '5':
           print("Finalizando o jogo.....")
           break    
             