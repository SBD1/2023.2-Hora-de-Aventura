from Banco import * 

personagem = Personagem()
pc = Pc()

print(" _   _                       _         ___                  _                   ")
print("| | | |                     | |       / _ \                | |                  ")
print("| |_| | ___  _ __ __ _    __| | ___  / /_\ \_   _____ _ __ | |_ _   _ _ __ __ _ ")
print("|  _  |/ _ \| '__/ _` |  / _` |/ _ \ |  _  \ \ / / _ \ '_ \| __| | | | '__/ _` |")
print("| | | | (_) | | | (_| | | (_| |  __/ | | | |\ V /  __/ | | | |_| |_| | | | (_| |")
print("\_| |_/\___/|_|  \__,_|  \__,_|\___| \_| |_/ \_/ \___|_| |_|\__|\__,_|_|  \__,_|")

while(True):

    print("\n**Bem vindo ao Hora de aventura**\n")
    print("*1 = Acessar Menu***")
    print("*2 = Criar Personagem(PC)*")
    print("*3 = Fazer party*")
    print("*4 = Ver localização*")
    print("**5 = Fechar jogo**\n")        
    
    print("Escolha uma opção de 1 a 5:")
    opcao = input()
    match opcao:
        case '1':  
                
            print("Opções de jogador")
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
            print("oi party")
            print("\n--------------------------------------------------------------------------------\n")
        case '4':
            print("Localização")
            print("\n--------------------------------------------------------------------------------\n")
        case '5':
           print("Finalizando o jogo.....")
           break    
             