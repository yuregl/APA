from CalculaRota import Calcula
from random import randint

class DescRandomica:
    def __init__(self):
        self.viz_aleatorio = []

    def set_viz_aleatorio(self, valor):
        self.viz_aleatorio.append(valor)

    def clear_viz_aleatorio(self):
        self.viz_aleatorio.clear()

    def descidaRandomica(self,rotas):
        distancia = 0
        melhor_NR = []

        for i in range(len(rotas)):
            melhor_rota, melhor_dist = self.metodo_descidaRandomica(rotas[i])
            distancia += melhor_dist
            melhor_NR.append(melhor_rota)

        return melhor_NR, distancia

    def vizinhanca(self, rota):
        vizinhos = []
        if len(rota) == 1:
            vizinhos.append(rota[0])

        else:
            for i in range(len(rota)):
                for j in range(len(rota)):
                    l_aux = rota.copy()
                    aux = l_aux[i]
                    if j > i:
                        l_aux[i] = l_aux[j]
                        l_aux[j] = aux
                        vizinhos.append(l_aux)

        return vizinhos


    def vizinho_random(self, tam):
        while True:
            viz = randint(0, (tam - 1))
            if viz in self.viz_aleatorio:
                pass
            else:
                self.set_viz_aleatorio(viz)
                return viz




    def metodo_descidaRandomica(self, rota):
        i = 0
        vizinhanca = self.vizinhanca(rota)
        tam = len(vizinhanca)
        inter_max = int(tam/2)
        disUnica = Calcula()

        if len(vizinhanca) < 2:
            s = rota.copy()
            rs = disUnica.calc_RotaUnica(rota)
        else:
            while i < inter_max:
                i+=1
                novo_v = self.vizinho_random(tam)

                s = rota.copy()
                s_random = vizinhanca[novo_v].copy()

                rs = disUnica.calc_RotaUnica(s)
                rs_random = disUnica.calc_RotaUnica(s_random)

                if rs_random < rs:
                    i = 0
                    s = s_random
                    rota = s.copy()
                self.clear_viz_aleatorio()


        return s, rs
