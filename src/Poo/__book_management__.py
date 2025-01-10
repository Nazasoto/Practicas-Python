#Biblioteca de gestión de libros

class Libro:
    def __init__(self, titulo, autor, genero, precio, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "precio": self.precio,
            "cantidad": self.cantidad,
        }

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.cargar_libros()

    def cargar_libros(self):
        # Cargar libros desde archivo JSON
        pass

    def guardar_libros(self):
        # Guardar libros en archivo JSON
        pass

    # Métodos: agregar, mostrar, buscar, eliminar, editar, calcular total
    pass

def menu():
    # Menú principal
    pass
