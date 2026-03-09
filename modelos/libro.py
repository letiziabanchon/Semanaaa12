class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self._titulo_autor = (titulo, autor)  # tupla
        self._categoria = categoria
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo_autor[0]

    @property
    def autor(self):
        return self._titulo_autor[1]

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, c):
        self._categoria = c

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.categoria}) [{self.isbn}]"