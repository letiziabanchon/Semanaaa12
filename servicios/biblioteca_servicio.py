from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:

    def __init__(self):
        self.libros = {}        # isbn -> Libro
        self.usuarios = {}      # id -> Usuario
        self.ids = set()        # IDs únicos
        self.prestamos = {}     # isbn -> id_usuario

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.prestamos:
            raise ValueError("Libro prestado.")
        del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id in self.ids:
            raise ValueError("ID repetido.")
        self.usuarios[usuario.id] = usuario
        self.ids.add(usuario.id)

    def prestar(self, isbn, id_usuario):
        if isbn in self.prestamos:
            raise ValueError("Ya prestado.")
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.agregar_libro(libro)
        self.prestamos[isbn] = id_usuario

    def devolver(self, isbn, id_usuario):
        usuario = self.usuarios[id_usuario]
        usuario.quitar_libro(isbn)
        del self.prestamos[isbn]

    def buscar_titulo(self, t):
        return [l for l in self.libros.values() if t.lower() in l.titulo.lower()]

    def buscar_autor(self, a):
        return [l for l in self.libros.values() if a.lower() in l.autor.lower()]

    def buscar_categoria(self, c):
        return [l for l in self.libros.values() if l.categoria.lower() == c.lower()]