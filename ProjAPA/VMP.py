from CalculaRota import Calcula

class VMP :
    def roteamento (self,grafo,capacidade,dimensao):
        ArrayRotas = []
        final = 0
        while True:
            carga = 0;
            rota = []
            indice_atual = 0
            prox_indice = 0
            while(carga+grafo[indice_atual].get_value() <= capacidade):
                menor_rota = 1000
                aux_aresta = grafo[indice_atual].get_aresta()
                for j in range(len(grafo[indice_atual].get_aresta())):
                    if indice_atual != j:
                        if not grafo[j].get_visitado() and aux_aresta[j] < menor_rota:
                            if ((carga + grafo[indice_atual].get_value() + grafo[j].get_value() ) <= capacidade):
                                menor_rota = aux_aresta[j]
                                prox_indice = j

                if (grafo[indice_atual].get_id() != 0):
                    final += 1

                carga = carga + grafo[indice_atual].get_value()
                if(grafo[indice_atual].get_id() != 0 ):
                    rota.append(grafo[indice_atual])
                grafo[indice_atual].set_visitado(True)
                indice_atual = prox_indice


            ArrayRotas.append(rota)
            grafo[0].set_visitado(True)

            if(dimensao == (final+1) ):
                calculo = Calcula()
                total_rota = calculo.calcula_rota(ArrayRotas)
                return  ArrayRotas, total_rota

