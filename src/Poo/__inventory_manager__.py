# Gestor de inventario con categorías 
import json

class productos:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def to_dict(self):
        return {    
        "nombre": self.nombre, 
        "precio": self.precio, 
        "cantidad": self.cantidad, 
        "categoria": self.categoria
        }


class Inventario:
    def __init__(self):
        self.productos = [] #Array vacio
        self.cargar_productos()
    #Metodo para cargar los productos desde el archivo JSON
    def cargar_productos(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                for producto_data in datos:
                    producto = productos(**producto_data)
                    self.productos.append(producto)
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
        except json.JSONDecodeError:
                print("El archivo de inventario tiene un formato incorrecto.")
    #Metodo para guardar los prodcutos
    def guardar_productos(self):
        with open("inventario.json", "w") as archivo:
            json.dump([producto.to_dict() for producto in self.productos], archivo)
    
    #Metodo para agregar productos al inventario
    def agregar_producto_al_inventario(self):
        #Se le solicita al usuario ingresar los datos del producto
        nombre = input("Ingrese el nombre del producto: ")
        #Verifica que los datos ingresados sean validos con valor numéricos
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos válidos.")
            return
        categoria = input("Ingrese la categoría del producto: ")
        #Evita campos vacios
        if nombre == "" or precio == 0 or cantidad == 0 or categoria == "":
            print("Los campos no pueden estar vacios")
        elif precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad no pueden ser menor o igual a 0")
        #Evita productos duplicados
        for producto in self.productos:
            if producto.nombre == nombre:
                print("Error: ¡este producto ya existe!")
                return
        #Crea un nuevo producto y lo agrega al archivo
        nuevo_producto = productos(nombre, precio, cantidad, categoria)
        self.productos.append(nuevo_producto)
        self.guardar_productos()
        print(f'¡El producto {nombre} fue agregado correctamente!')

    #Metodo para mostrar los productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Productos en el inventario:")
            for producto in self.productos:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}, Categoría: {producto.categoria}")

    #Metodo para buscar producto por categoria
    def buscar_categoria(self):
        categoria = input("Ingrese la categoría del producto que desea buscar: ")
        encontrado = False
        for producto in self.productos:
            if producto.categoria == categoria:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}, Categoría: {producto.categoria}")
                encontrado = True
        if not encontrado:
            print(f'No se encontraron productos en la categoría {categoria}.')

    #Metodo para buscar producto por nombre
    def buscar_nombre(self):
        nombre = input("Ingrese el nombre del producto: ") 
        encontrado = False
        for producto in self.productos:
            if producto.nombre == nombre:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}, Categoría: {producto.categoria}")
                encontrado = True
        if not encontrado:
            print(f"No se encontraron productos con el nombre de {nombre}.")

    #Metodo para eliminar un producto o todos
    def eliminar_producto(self):
        opcion = input("¿Desea eliminar un producto específico o todos los productos? (específico/todos): ").lower()
    
        # Verifica que la opción sea válida antes de proceder
        if opcion not in ["específico", "todos"]:
            print("Opción no válida. Por favor, elija 'específico' o 'todos'.")
            return
    
        # Abre el archivo
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
            return
    
        if not datos:
            print("El inventario está vacío.")
            return
        
        if opcion == "específico":
            nombre = input("Ingrese el nombre del producto que desea eliminar: ")
            producto_encontrado = False
        
        # Busca y elimina el producto específico
        for i in range(len(datos)-1, -1, -1):
            if datos[i]["nombre"] == nombre:
                datos.pop(i)
                producto_encontrado = True
                print(f"El producto '{nombre}' ha sido eliminado.")
                break
        
        if not producto_encontrado:
            print(f"No se encontró ningún producto con el nombre '{nombre}'.")
    
        else:  # opcion == "todos"
            datos.clear()
            print("Todos los productos han sido eliminados.")
    
        # Guarda los cambios en el archivo
        try:    
            with open("inventario.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar los cambios: {e}")
            return

    #Metodo para calcular el total de productos en el inventario
    def calcular_total(self):
        total = 0
    
        # Primero, calcular el total de los productos en memoria
        for producto in self.productos:
            total += producto.precio * producto.cantidad
    
        # calcular el total de los productos en el archivo
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                for producto_data in datos:
                    producto = productos(**producto_data)
                    total += producto.precio * producto.cantidad
                
            return total
        
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
            # Si no se encuentra el archivo, devolver solo el total de los productos en memoria
            return total
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario: formato JSON inválido.")
            return total
        except Exception as e:
            print(f"Error inesperado al calcular el total: {e}")
            return total

    #Metodo para editar producto existente
    def editar_producto(self):
        nombre = input("Ingrese el nombre del producto que desea editar: ")

        #Busca el producto
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre:
                producto_encontrado = producto
                break
        #Si no lo encuentra 
        if not producto_encontrado:
            print(f"No se encontró ningún producto con el nombre '{nombre}'.")
            return
        
        #Muestra la informacion del producto 
        print("Información del producto:")
        print(f'Nombre: {producto_encontrado}, Precio: {producto_encontrado.precio}, Cantidad: {producto_encontrado.cantidad}, Categoría: {producto_encontrado.categoria}')

        opcion = input("¿Desea editar este producto? s/n")

        if opcion.lower() != "s":
            print("¡Operacion cancelada!")
            return

        try:
        # Solicita los nuevos datos con validación
            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")

            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero válido para la cantidad.")
        # Actualizamos los valores
            producto_encontrado.precio = nuevo_precio
            producto_encontrado.cantidad = nueva_cantidad
        
        # Guardamos los cambios
            self.guardar_productos()
            print(f"\nEl producto '{nombre}' ha sido editado exitosamente.")
        
        # Mostramos la información actualizada
            print("\nInformación actualizada del producto:")
            print(f"Nombre: {producto_encontrado.nombre}, Precio: ${producto_encontrado.precio:.2f}, Cantidad: {producto_encontrado.cantidad}, Categoría: {producto_encontrado.categoria}")
        
        except Exception as e:
            print(f"Error al editar el producto: {e}")
            print("Los cambios no fueron guardados.")

def menu():
    inventario = Inventario()
    print("Bienvenido al Gestor de Inventario")
    while True:
        print("\nMenú:")
        print("1. Agregar producto al inventario")
        print("2. Mostrar productos en el inventario")
        print("3. Buscar producto por categoría")
        print("4. Buscar producto por nombre")
        print("5. Eliminar producto")
        print("6. Calcular total de productos en el inventario")
        print("7. Editar producto existente")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            opcion = int(opcion)
            if opcion not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print(f"La opción {opcion} no está disponible")
                continue
        except ValueError:
            print("Por favor, ingrese una opción válida.")
            continue

        # Opciones
        if opcion == 1:
            inventario.agregar_producto_al_inventario()
        elif opcion == 2:
            inventario.mostrar_productos()
        elif opcion == 3:
            inventario.buscar_categoria()
        elif opcion == 4:
            inventario.buscar_nombre()  # Ajuste aquí: no existe `inventario.buscar`
        elif opcion == 5:
            inventario.eliminar_producto()
        elif opcion == 6:
            total = inventario.calcular_total()
            print(f"El total de los productos en el inventario es: ${total:.2f}")
        elif opcion == 7:
            inventario.editar_producto()
        elif opcion == 8:
            print("Saliendo del programa...")
            break

menu()

