class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id = id_usuario
        self._prestados = []  # lista de libros

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def prestamos(self):
        return self._prestados

    def agregar_libro(self, libro):
        self._prestados.append(libro)

    def quitar_libro(self, isbn):
        self._prestados = [l for l in self._prestados if l.isbn != isbn]