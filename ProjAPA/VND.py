from TwoOpt import TwoOpt
from Swap import Swap
from DRandom import DescRandomica

class VND:

    def vnd(self, rotas, melhor_rota):
        qtd_metodos = 3
        i = 0
        while i < qtd_metodos:
            nova_rotas, melhor_dist = self.Heuristicas(rotas, i)
            if(melhor_dist < melhor_rota ):
                rotas = nova_rotas.copy()
                melhor_rota = melhor_dist
                i = 0
            else:
                i+=1

        return rotas, melhor_dist

    def Heuristicas(self, rotas, opcao):

        if opcao == 0:
            desc = DescRandomica()
            rotas, melhor_tempo = desc.descidaRandomica(rotas)

        if opcao == 1:
            swap = Swap()
            rotas, melhor_tempo = swap.swap(rotas)

        if opcao == 2:
            opt = TwoOpt()
            rotas, melhor_tempo = opt.opt(rotas)

        return rotas, melhor_tempo