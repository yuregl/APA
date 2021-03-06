class Calcula:
    def calcula_rota(self, rotas):
        rota_total = 0
        for i in range(len(rotas)):
            aux_rotas = rotas[i]
            if len(aux_rotas) == 1:
                aresta = aux_rotas[0].get_aresta()
                soma_rota = aux_rotas[0].get_indice_aresta(aresta, 0)
                # print(f"Valor soma rota {soma_rota}")
                # print(f"Valor soma rota {soma_rota}")
                rota_total = rota_total + (2 * soma_rota)
                # print(rota_total)

            else:
                for j in range(len(aux_rotas)):

                    if j == 0:
                        aresta = aux_rotas[j].get_aresta()
                        id_pro = aux_rotas[j + 1].get_id()
                        soma_rota = aux_rotas[0].get_indice_aresta(aresta, 0)
                        # print(f"Valor soma rota {soma_rota}")
                        rota_total = rota_total + soma_rota
                        soma_rota = aux_rotas[j].get_indice_aresta(aresta, id_pro)
                        # print(f"Valor soma rota {soma_rota}")
                        rota_total += soma_rota
                        # print(rota_total)

                    if j == len(aux_rotas) - 1:
                        aux_aresta = aux_rotas[j].get_aresta()
                        soma_rota = aux_rotas[j].get_indice_aresta(aux_aresta, 0)
                        # print(f"Valor soma rota {soma_rota}")
                        rota_total += soma_rota
                        # print(rota_total)


                    elif j > 0 and j < len(aux_rotas) - 1:
                        aresta = aux_rotas[j].get_aresta()
                        id_pro = aux_rotas[j + 1].get_id()
                        soma_rota = aux_rotas[j].get_indice_aresta(aresta, id_pro)
                        # print(f"Valor soma rota {soma_rota}")
                        rota_total += soma_rota
                        # print(rota_total)

        return rota_total

    def calc_RotaUnica(self, rota):
        cont_distancia = 0

        for i in range(len(rota) -1):
            aux_aresta = rota[i].get_aresta()
            id_prox = rota[i+1].get_id()
            cont_distancia += rota[i].get_indice_aresta(aux_aresta, id_prox)

        cont_distancia += rota[0].get_indice_aresta(rota[0].get_aresta(), 0)
        cont_distancia += rota[len(rota) -1].get_indice_aresta(rota[len(rota) -1].get_aresta(), 0)

        return cont_distancia

