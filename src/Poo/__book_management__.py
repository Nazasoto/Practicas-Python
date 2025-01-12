import json

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

    # Funciones para cargar y guardar libros

    def cargar_libros(self):
        try:
            with open("biblioteca.json", "r") as archivo:
                datos = json.load(archivo)
                for libro_data in datos:
                    libro = Libro(**libro_data)
                    self.libros.append(libro)
        except FileNotFoundError:
            print("No se encontró el archivo de libros. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("El archivo de libros tiene un formato incorrecto.")

    def guardar_libros(self):
        with open("biblioteca.json", "w") as archivo:
            json.dump([libro.to_dict() for libro in self.libros], archivo)

    # Funciones para interactuar con la biblioteca

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        try:
            cantidad_de_copias = int(input("Ingrese la cantidad de copias de este libro: "))
            precio = float(input("Ingrese el precio del libro: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            return

        if titulo == "" or autor == "" or genero == "":
            print("Error: Los campos no pueden estar vacíos.")
            return
        if cantidad_de_copias <= 0 or precio <= 0:
            print("Error: El precio y la cantidad de copias deben ser mayores que 0.")
            return
        for libro in self.libros:
            if libro.titulo == titulo:
                print("Error: ¡Este libro ya existe!")
                return

        nuevo_libro = Libro(titulo, autor, genero, precio, cantidad_de_copias)
        self.libros.append(nuevo_libro)
        self.guardar_libros()
        print(f'¡El libro "{titulo}" fue agregado correctamente!')

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros disponibles.")
        else:
            print(f"Hay {len(self.libros)} libros en la biblioteca:")
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. Título: {libro.titulo}")
                print(f"   Autor: {libro.autor}")
                print(f"   Género: {libro.genero}")
                print(f"   Precio: ${libro.precio:.2f}")
                print(f"   Cantidad: {libro.cantidad}")
                print("-" * 30)

    def buscar_libro(self):
        criterio = input("Ingrese el género o autor del libro que desea buscar: ")
        libros_encontrados = False
        for libro in self.libros:
            if libro.genero == criterio or libro.autor == criterio:
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor}")
                print(f"Género: {libro.genero}")
                print(f"Precio: ${libro.precio:.2f}")
                print(f'Cantidad de copias: {libro.cantidad}')
                print("-" * 30)
                libros_encontrados = True
        if not libros_encontrados:
            print(f"No se encontraron libros con el nombre de '{criterio}'.")

     #Funciones para eliminar y editar libros

    def eliminar_libro(self):
        opcion = input("¿Desea eliminar un libro o todos? (uno/todos): ").lower()
        if opcion == "uno":
            titulo = input("Ingrese el título del libro que desea eliminar: ")
            for libro in self.libros:
                if libro.titulo == titulo:
                    self.libros.remove(libro)
                    self.guardar_libros()
                    print(f"¡El libro '{titulo}' ha sido eliminado correctamente!")
                    return
            print(f"No se encontró ningún libro con el título '{titulo}'.")
        elif opcion == "todos":
            self.libros = []
            self.guardar_libros()
            print("Todos los libros han sido eliminados.")
        else:
            print("Opción inválida. Intente de nuevo.")

    def editar_libro(self):
        titulo = input("Ingrese el título del libro que desea editar: ")
        libro_encontrado = None
        for libro in self.libros:
            if libro.titulo == titulo:
                libro_encontrado = libro
                break

        if not libro_encontrado:
            print(f"No se encontró el libro con el título '{titulo}'.")
            return

        print("Información actual del libro:")
        print(f"Título: {libro_encontrado.titulo}")
        print(f"Autor: {libro_encontrado.autor}")
        print(f"Género: {libro_encontrado.genero}")
        print(f"Precio: ${libro_encontrado.precio:.2f}")
        print(f"Cantidad: {libro_encontrado.cantidad}")

        try:
            nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del libro: "))
            if nuevo_precio > 0 and nueva_cantidad > 0:
                libro_encontrado.precio = nuevo_precio
                libro_encontrado.cantidad = nueva_cantidad
                self.guardar_libros()
                print(f"¡El libro '{titulo}' fue editado correctamente!")
            else:
                print("Error: El precio y la cantidad deben ser mayores que 0.")
        except ValueError:
            print("Error: Ingrese valores válidos.")

    #Función para calcular el valor total

    def calcular_el_total(self):
        total = sum(libro.precio * libro.cantidad for libro in self.libros)
        print(f"El valor total de todos los libros en la biblioteca es: ${total:.2f}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Editar libro")
        print("6. Calcular valor total")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")
        try:
            opcion = int(opcion)
            if opcion == 1:
                biblioteca.agregar_libro()
            elif opcion == 2:
                biblioteca.mostrar_libros()
            elif opcion == 3:
                biblioteca.buscar_libro()
            elif opcion == 4:
                biblioteca.eliminar_libro()
            elif opcion == 5:
                biblioteca.editar_libro()
            elif opcion == 6:
                biblioteca.calcular_el_total()
            elif opcion == 7:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

menu()
