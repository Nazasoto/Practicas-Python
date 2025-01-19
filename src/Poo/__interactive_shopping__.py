import json

class Inventario:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Compras:
    def __init__(self):
        self.productos = []
        self.cargar_archivo()

    # Cargar productos desde archivo JSON
    def cargar_archivo(self):
        try:
            with open("productos.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = [Inventario(**producto) for producto in datos]
        except FileNotFoundError:
            print("No se encontró el archivo de productos. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("El archivo de productos tiene un formato incorrecto.")

    # Guardar productos en archivo JSON
    def guardar_archivo(self):
        datos = [producto.to_dict() for producto in self.productos]
        with open("productos.json", "w") as archivo:
            json.dump(datos, archivo)

    # Agregar producto
    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ").strip()
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            return

        if not nombre or cantidad <= 0 or precio <= 0:
            print("Error: Los valores no pueden estar vacíos ni ser menores o iguales a 0.")
            return

        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"El producto '{nombre}' ya existe en la lista.")
                return

        nuevo_producto = Inventario(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_archivo()
        print(f"Producto '{nombre}' agregado con éxito.")

    # Eliminar producto
    def eliminar_producto(self):
        nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                self.guardar_archivo()
                print(f"Producto '{nombre}' eliminado con éxito.")
                return
        print(f"No se encontró el producto '{nombre}' en la lista.")

    # Mostrar lista de productos
    def mostrar_lista(self):
        if not self.productos:
            print("La lista de productos está vacía.")
        else:
            print("\nLista de productos:")
            for producto in self.productos:
                print(producto)

    # Buscar producto
    def buscar_producto(self):
        nombre = input("Ingrese el nombre del producto que desea buscar: ").strip()
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"\nInformación del producto '{nombre}':\n{producto}")
                return
        print(f"No se encontró el producto '{nombre}' en la lista.")


def menu():
    compras = Compras()
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar lista de productos")
        print("4. Buscar producto")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        try:
            opcion = int(opcion)
            if opcion == 1:
                compras.agregar_producto()
            elif opcion == 2:
                compras.eliminar_producto()
            elif opcion == 3:
                compras.mostrar_lista()
            elif opcion == 4:
                compras.buscar_producto()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


menu()
