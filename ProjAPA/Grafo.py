class Grafo:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.aresta = []
        self.visitado = False

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_aresta(self):
        return self._aresta

    def set_aresta(self, aresta):
        self._aresta = aresta

    def get_visitado(self):
        return self._visitado

    def set_visitado(self, visitado):
        self._visitado = visitado

    def get_indice_aresta(self, aresta, indice):
        return aresta[indice]