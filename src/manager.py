#GESTOR DE INVENTARIO
import string

def inventario():
    #Opciones
    print("Bienvenido al gestor de inventario")
    print("1- Agregar un producto")
    print("2- Ver inventario")
    print("3- Calcular el valor total del inventario")
    print("4- Buscar un producto")
    print("5- Borrar producto")
    print("6- Salir")

    productos = []

    while True:
        
        opcion = input("Ingrese una opcion: ")
        #Verifica errores
        try:
            opcion = int(opcion)
            if opcion not in [1, 2, 3, 4, 5, 6]:
                print("Esa opción no está disponible.")
                continue	
        except ValueError:
            print("Por favor, ingese una opción valida.")
            continue
        except SyntaxError:
            print("Por favor, ingrese una opción valida.")
            continue


           
        
            #FUNCIONES

        # Agregar producto
        def agregar_producto():
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio por unidad: $")
            cantidad = input("Ingrese el stock disponible: ")
            if nombre == "" or precio == "" or cantidad == "":
                print("Por favor ingrese todos los datos requeridos.")
            else:
                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
                print("¡Producto agregado con éxito!")
                # Guardar la información en el archivo
                with open('productos.txt', 'a') as archivo:
                    archivo.write(f'Nombre: {nombre}, Precio: ${precio}, Stock: {cantidad}\n')

       
        #Ver inventario
        def leer_productos():
            try:
                with open('productos.txt', 'r') as archivo:
                    for linea in archivo.readlines():
                        print(linea.strip())
            except FileNotFoundError:
                        print("No hay productos guardados en el archivo.")
    

        #Calcular valor
        def calcular_total():
            valor_total  = 0
            for producto in productos:
                valor_total += float(producto["precio"])
            return valor_total
        

        #Buscar producto    
        def buscar_producto():
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            encontrado = False
            for producto in productos: 
                if producto["nombre"] == nombre_producto:
                    print(f"Nombre: {producto['nombre']}, Precio ${producto['precio']}, Stock: {producto['cantidad']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")
                
        
        #Borrar producto
        def borrar_producto():
            nombre_a_borrar = input("Ingrese el nombre del producto a borrar: ")
            for producto in productos[:]:
                if producto["nombre"] == nombre_a_borrar:
                    productos.remove(producto)
                    # Actualizar el archivo
                    with open('productos.txt', 'w') as archivo:
                        for p in productos:
                            archivo.write(f'Nombre: {p["nombre"]}, Precio: ${p["precio"]}, Stock: {p["cantidad"]}\n')
                    print("Producto borrado con éxito.")
                    return
            print("Producto no encontrado.")


            #Condiciones
        if opcion == 1:
            agregar_producto()

        if opcion == 2:
            leer_productos()

        if opcion == 3:
            valor_total = calcular_total()
            print(f"El valor total del inventario es: ${valor_total}")
        
        if opcion == 4:
            buscar_producto()

        if opcion == 5:
            borrar_producto()

        if opcion == 6:
            print("Saliendo del programa...")
            break


inventario()

        


        


