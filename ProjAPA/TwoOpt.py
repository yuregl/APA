from CalculaRota import Calcula
from Grafo import Grafo

class TwoOpt:

    def opt(self, rotas):
        # melhor_rota = []
        distancia = 0
        # melhor_NR = Grafo
        melhor_NR = []

        for i in range(len(rotas)):
            melhor_rota, melhor_dist = self.metodo_opt(rotas[i])
            distancia+= melhor_dist
            melhor_NR.append(melhor_rota)

        return melhor_NR, distancia

    def opt_troca(self, rota, index_i, index_j):
        nova_rota = []

        for i in range(index_i):
            nova_rota.append(rota[i])

        for i in range(index_j, index_i - 1 , -1):
            nova_rota.append(rota[i])

        for i in range(index_j+1, len(rota)):
            nova_rota.append(rota[i])

        return nova_rota

    def metodo_opt(self, rota):
        aux_rota = rota
        boolean = True
        disUnica = Calcula()

        if len(rota) == 1:
            melhor_distancia = 2 * rota[0].get_indice_aresta(rota[0].get_aresta(), 0)
            return rota, melhor_distancia

        while boolean:
            boolean = False
            for i in range(len(rota)):
                melhor_distancia = disUnica.calc_RotaUnica(aux_rota)
                for j in range(i+1, len(rota)):
                    nova_rota = self.opt_troca(aux_rota, i, j)
                    nova_distancia = disUnica.calc_RotaUnica(nova_rota)
                    if(nova_distancia < melhor_distancia):
                        aux_rota = nova_rota
                        melhor_distancia = nova_distancia
                        boolean = True
                        break

        return aux_rota, melhor_distancia