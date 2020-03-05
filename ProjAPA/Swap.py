from CalculaRota import Calcula
class Swap:

    def swap(self, rotas):
        distancia = 0
        melhor_NR = []

        for i in range(len(rotas)):
            melhor_rota, melhor_dist = self.metodo_swap(rotas[i])
            distancia+= melhor_dist
            melhor_NR.append(melhor_rota)

        return melhor_NR, distancia

    def swap_pos(self, rota, i, j):
        rota[i], rota[j] = rota[j], rota[i]
        return rota


    def metodo_swap(self, rota):
        boolean = True
        disUnica = Calcula()

        if len(rota) == 1:
            melhor_distancia = 2 * rota[0].get_indice_aresta(rota[0].get_aresta(), 0)
            return rota, melhor_distancia

        while boolean:
            boolean = False
            for i in range(len(rota)):
                melhor_distancia = disUnica.calc_RotaUnica(rota)
                for j in range (len(rota)):
                    if i != j:
                        aux = rota.copy()
                        rota = self.swap_pos(rota, i, j)
                        nova_distancia = disUnica.calc_RotaUnica(rota)
                        if nova_distancia < melhor_distancia:
                            melhor_distancia = nova_distancia
                            boolean = True
                        else:
                            rota = aux.copy()

        return rota, melhor_distancia

