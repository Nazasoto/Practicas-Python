import json
import re

#Agenda de contactos
def agenda_de_contactos():

    print("Bienvenido a la agenda de contactos")
    print("1- Agregar contacto")
    print("2- Mostrar contactos")
    print("3- Buscar contacto")
    print("4- Eliminar contacto")
    print("5- Salir")

    #Funciones

    #1- Agregar contacto
    def agregar_contacto():
        #Validacion para crear el arhivo json
        try:
            with open("contactos.json", "r") as archivo:
                contactos = json.load(archivo)
        except FileNotFoundError:
            contactos = []
        #Ingresar datos
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")

        #Verifica que los datos del telefono sean correctos
        while not telefono.isdigit() or len(telefono) != 10:
            print("Por favor, ingrese un número de teléfono válido")
            telefono = input("Ingrese el número de teléfono del contacto: ")

        #Verifica que el mail es valido
        while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Error: el email no es válido")
            email = input("Ingrese el email del contacto: ")

        # Evita que el usuario ingrese datos vacios
        if nombre == "" or telefono == "" or email == "":
            print("Por favor, llene los campos requeridos")
            return

        # Verifica si el contacto ya existe
        for contacto in contactos:
            if contacto["nombre"] == nombre and contacto["telefono"] == telefono and contacto["email"] == email:
                print("Error: ¡este contacto ya existe!")
                return

        # Agrega el contacto a la lista
        contactos.append({"nombre": nombre, "telefono": telefono, "email": email})

        # Intenta escribir el contacto en el archivo
        try:
            with open("contactos.json", "w") as archivo:
                json.dump(contactos, archivo)
            print("Contacto agregado con éxito.")
        except Exception as e:
            print("Error: ", e)

    #2- Mostrar todos los contactos
    def mostrar_contactos():
        #Abre el archivo
        try:
            with open("contactos.json", "r") as archivo:
                contactos = json.load(archivo)
        except FileNotFoundError:
            print("No hay contactos existentes.")
            return
        #Muestra a todos los contactos
        for contacto in contactos:
            print(f'Nombre: {contacto["nombre"]}, Telefono: {contacto["telefono"]}, Email: {contacto["email"]}')

    #3- Buscar contacto
    def buscar_contacto():
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        #Abre el archivo
        try:
            with open("contactos.json", "r") as archivo:
                contactos = json.load(archivo)
        except FileNotFoundError:
            print("No hay contactos existentes.")
            return
        #Busca el contacto dentro del archivo
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                print("¡Usuario encontrado!")
                print(f'Nombre: {contacto["nombre"]}, Telefono: {contacto["telefono"]}, Email: {contacto["email"]}')
                return
        print("No se encontró ningún contacto con ese nombre.")

    #4- Eliminar especifico o todos
    def eliminar_contacto_o_todos():
        #Ingresamos un bucle para que el usuario elija si quiere eliminar un contacto especifico o todos
        while True:
            opcion = input("¿Desea eliminar un contacto específico o todos? (específico/todos): ")
            if opcion == "especifico":
                nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
                #Abre el archivo
                try:
                    with open("contactos.json", "r") as archivo:
                        contactos = json.load(archivo)
                except FileNotFoundError:
                    print("No hay contactos existentes...")
                    return
                encontrado = False
                #Ciclo for para eliminar el contacto especifico
                for contacto in contactos:
                    if contacto["nombre"] == nombre:
                        contactos.remove(contacto)
                        encontrado = True
                        break
                if encontrado:
                    try:
                        with open("contactos.json", "w") as archivo:
                            json.dump(contactos, archivo)
                        print("¡Contacto eliminado con éxito!")
                    except Exception as e:
                        print("Error: ", e)
                else:
                    print("Contacto no encontrado.")
                break
            #Ciclo for para eliminar todos los contactos
            elif opcion == "todos":
                try:
                    with open("contactos.json", "w") as archivo:
                        json.dump([], archivo)
                    print("Todos los contactos han sido eliminados con éxito.")
                except Exception as e:
                    print("Error: ", e)
                break
            else:
                print("Opción inválida. Por favor, ingrese 'específico' o 'todos'.")

    #BUCLE
    while True:
        opcion = input("Ingrese una opción: ")    
    #Verifica errores
        try:
            opcion = int(opcion)
            if opcion not in [1, 2, 3, 4, 5]:
                print("Esa opción no está disponible.")
                continue	
        except ValueError:
            print("Por favor, ingese una opción valida.")
            continue
        except SyntaxError:
            print("Por favor, ingrese una opción valida.")
            continue

        #Condiciones

        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            mostrar_contactos()
        elif opcion == 3:
            buscar_contacto()
        elif opcion == 4:
            eliminar_contacto_o_todos()
        elif opcion == 5:
            print("¡Gracias por usar la agenda de contactos!")
            print("Saliendo del programa...")
            break



agenda_de_contactos()