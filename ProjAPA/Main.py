from Arquivo import Arquivo
from VMP import VMP
from TwoOpt import TwoOpt
from Swap import Swap

import sys

caminho = "../Instancias/"

while True:
    print("1 - P-n16-k8")
    print("2 - P-n19-k2")
    print("3 - P-n20-k2")
    print("4 - P-n23-k8")
    print("5 - P-n45-k5")
    print("6 - P-n50-k10")
    print("7 - P-n51-k10")
    print("8 - P-n55-k7")
    print("9 - Sair")

    try:
        escolha_arquivo = int(input('Digite o numero para selecionar o arquivo ou 9 para sair\n'))

        if escolha_arquivo == 1:
            caminho = caminho + "P-n16-k8.txt"

        if escolha_arquivo == 2:
            caminho = caminho + "P-n19-k2.txt"

        elif escolha_arquivo == 3:
            caminho = caminho + "P-n20-k2.txt"

        elif escolha_arquivo == 4:
            caminho = caminho + "P-n23-k8.txt"

        elif escolha_arquivo == 5:
            caminho = caminho + "P-n45-k5.txt"

        elif escolha_arquivo == 6:
            caminho = caminho + "P-n50-k10.txt"

        elif escolha_arquivo == 7:
            caminho = caminho + "P-n51-k10.txt"

        elif escolha_arquivo == 8:
            caminho = caminho + "P-n55-k7.txt"

        elif escolha_arquivo == 9:
            print(escolha_arquivo)
            sys.exit()

        arq = Arquivo()
        vmp = VMP()

        dimensao, capacidade, grafo = arq.leArquivo(caminho)
        rotas, tam_rota = vmp.roteamento(grafo,capacidade,dimensao)

        # opt = TwoOpt()
        # opt.opt(rotas)

        swap = Swap()
        swap.swap(rotas)


    except Exception:
        print("Valor inválido, tente novamente\n")
        pass

    caminho = "../Instancias/"
