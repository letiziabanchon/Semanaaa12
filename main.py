from servicios.biblioteca_servicio import BibliotecaServicio
from modelos.libro import Libro
from modelos.usuario import Usuario

svc = BibliotecaServicio()

def menu():
    print("\n1. Añadir libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar por título")
    print("99. Salir")

while True:
    menu()
    op = input("Opción: ")

    if op == "99":
        break

    elif op == "1":
        t = input("Título: ")
        a = input("Autor: ")
        c = input("Categoría: ")
        i = input("ISBN: ")
        svc.agregar_libro(Libro(t, a, c, i))
        print("Libro agregado.")

    elif op == "2":
        n = input("Nombre: ")
        uid = input("ID: ")
        svc.registrar_usuario(Usuario(n, uid))
        print("Usuario registrado.")

    elif op == "3":
        isbn = input("ISBN: ")
        uid = input("ID usuario: ")
        svc.prestar(isbn, uid)
        print("Libro prestado.")

    elif op == "4":
        isbn = input("ISBN: ")
        uid = input("ID usuario: ")
        svc.devolver(isbn, uid)
        print("Libro devuelto.")

    elif op == "5":
        t = input("Título: ")
        res = svc.buscar_titulo(t)
        for l in res:
            print(l)