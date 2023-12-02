from Banco import *

pc = Pc()

def CarregarJogo():
    Save=input("\033[1;32mDigite o ID do seu personagem: \033[0m")
    jogador=pc.getPC(Save)
    return jogador[0]

def EncontrarSalas(pos):
    Quadrado=2
    lc=Local()
    Oeste=lc.getLocal(pos-1)
    Norte=lc.getLocal(pos-Quadrado)
    Leste=lc.getLocal(pos+1)
    Sul=lc.getLocal(pos+Quadrado)
    salas_disponiveis = []

    # Adicionar à lista se não for None
    if Oeste is not None:
        salas_disponiveis.append(Oeste[0][0])
        #salas_disponiveis.append(Oeste[0][2])
    if Norte is not None:
        salas_disponiveis.append(Norte[0][0])
        #salas_disponiveis.append(Norte[0][2])
    if Leste is not None:
        salas_disponiveis.append(Leste[0][0])
        #salas_disponiveis.append(Leste[0][2])
    if Sul is not None:
        salas_disponiveis.append(Sul[0][0])
        #salas_disponiveis.append(Sul[0][2])

    # Retornar a lista de salas disponíveis
    return salas_disponiveis
    