from Grafo import Grafo
class Arquivo:

    def leArquivo(self, caminho):

        file = open(caminho, "r")
        leitura = file.readlines()

        grafo = []
        arraInt = []

        dimensao = leitura[1].split()
        dimensao = int(dimensao[1])
        dimLinha = dimensao+6

        capacidade = leitura[2].split()
        capacidade = int(capacidade[1])

        for linhaDim in range(4, dimensao+4):
            aux = leitura[linhaDim].split()
            id = int(aux[0])
            value = int(aux[1])
            g = Grafo(id, value)
            grafo.append(g)

        for linhaAresta in range(dimLinha, len(leitura) -1):
            aux = leitura[linhaAresta].split()
            # aux é um vetor com todos os valores da linha

            for i in range(len(aux)):
                aux[i] = int(aux[i])
                # passa cada linha para inteiro

            arraInt.append(aux)

        for i in range(dimensao):
            grafo[i].set_aresta(arraInt[i])

        for i in range(dimensao):
            print(grafo[i].get_aresta())

        return dimensao, capacidade, grafo