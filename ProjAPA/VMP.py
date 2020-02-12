from Grafo import Grafo
class VMP :
    def roteamento (self,grafo,capacidade,dimensao):
        capacidade_total = 0
        ArrayRotas = []
        cont_Rota = 0
        final = 0
        while True :
            carga = 0;
            rota = []
            indice_atual = 0
            prox_indice = 0
            while(carga+grafo.get_value()<= capacidade):
                menor_rota = 1000
                aux_aresta = grafo[indice_atual].get_aresta()
                for j in range(len(grafo[indice_atual].get_aresta())):
                    if(indice_atual != j):
                        if not (grafo[j].get_visitado() and aux_aresta[j]) < menor_rota:
                            if ((carga + grafo[indice_atual].get_value() + grafo[j].get_value) <= capacidade):
                                menor_rota = aux_aresta[j]
                                prox_indice = j
                                print(prox_indice)
                            else:
                                if (j == len(grafo[indice_atual].get_Aresta())):
                                    menor_rota = aux_aresta[0]
                if (grafo[indice_atual].get_id() != 0):
                    final += 1
                    if(dimensao == final+1):
                        menor_rota = aux_aresta[0]
                    carga+= grafo[indice_atual].gel_value()
                    rota.append(grafo[indice_atual])
                    grafo[indice_atual].set_visitado(True)
                    indice_atual = prox_indice


        rotas_total.append(rota)