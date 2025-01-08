import re
import json

# Clase para representar un contacto
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
    def to_dict(self):
        return {"nombre": self.nombre, "telefono": self.telefono, "correo": self.correo}


# Clase para gestionar la agenda
class Agenda:
    def __init__(self):
        self.contactos = []  # Lista de contactos
        self.cargar_contactos()

    def cargar_contactos(self):
        try:
            with open("contactos.json", "r") as archivo:
                contactos_json = json.load(archivo)
                self.contactos = [Contacto(c["nombre"], c["telefono"], c["correo"]) for c in contactos_json]
        except FileNotFoundError:
            pass


    #Funcion 1
    def agregar_contacto(self):
        nombre = input("Ingrese el usuario: ")
        telefono = input("Ingrese el número de teléfono: ")
        correo = input("Ingrese el correo electrónico: ")

        # Validar teléfono
        while not telefono.isdigit() or len(telefono) != 10:
            print("Por favor, ingrese un número de teléfono válido.")
            telefono = input("Ingrese el número de teléfono del contacto: ")

        # Validar correo electrónico
        while not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            print("Error: el email no es válido.")
            correo = input("Ingrese el correo electrónico del contacto: ")

        # Evitar duplicados
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("Error: ¡este contacto ya existe!")
                return

        # Crea nuevo contacto y agregarlo a la lista
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)
        print(f'¡El contacto {nombre} fue agendado correctamente!')
        print("-" * 30)

        # Guardar contactos en archivo JSON
        try:
            with open("contactos.json", "w") as archivo:
                # Convertir los objetos a diccionarios antes de escribir
                contactos_como_diccionario = [c.to_dict() for c in self.contactos]
                json.dump(contactos_como_diccionario, archivo)
        except Exception as e:
            print("Error al guardar el archivo:", e)

    #Funcion 2
    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos existentes.")
            return
        for i, contacto in enumerate(self.contactos, 1):
            print(f'{i}- Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Correo: {contacto.correo}')
            print("-" * 30)
    
    #Funcion 3
    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del usuario que desea buscar: ")
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("¡Usuario encontrado!")
                print(f'Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Correo: {contacto.correo}')
                print("-" * 30)
                return
        print(f'No se encontró ningún contacto con el nombre de {nombre}.')

    #Funcion 4
    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
        encontrado = False
        # Busca y elimina el contacto
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                encontrado = True
                print(f'¡El contacto {nombre} fue eliminado correctamente!')
                break
        if not encontrado:
            print(f'No se encontró ningún usuario con el nombre {nombre}.')
        else:
            # Guardar cambios en el archivo JSON
            try:
                with open("contactos.json", "w") as archivo:
                    json.dump([c.to_dict() for c in self.contactos], archivo)
            except Exception as e:
                print("Error al guardar el archivo:", e)


def menu():
    agenda = Agenda()
    #BUCLE
    while True: 
        #Opciones
        print("BIENVENIDO A LA AGENDA DE CONTACTO")
        print("1- Agregar contacto")
        print("2- Mostrar contactos")
        print("3- Buscar contacto")
        print("4- Eliminar contacto")
        print("5- Salir")
        #Usuario ingresa una opcion
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

        #Opciones 
        if opcion == 1:
            agenda.agregar_contacto()
        elif opcion == 2:
            agenda.mostrar_contactos()
        elif opcion == 3:
            agenda.buscar_contacto()
        elif opcion == 4:
            agenda.eliminar_contacto()
        elif opcion == 5:
            print("Saliendo del programa...")
            break

menu()