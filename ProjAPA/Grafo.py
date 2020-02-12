class Grafo:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.aresta = []
        self.visitado = False

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_aresta(self):
        return self.aresta

    def set_aresta(self, aresta):
        self.aresta = aresta

    def get_visitado(self):
        return self.visitado

    def set_visitado(self, visitado):
        self.visitado = visitado

    def get_indice_aresta(self, aresta, indice):
        return aresta[indice]