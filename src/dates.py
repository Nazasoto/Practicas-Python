#GESTOR DE DATOS
import string

#Funcion
def opciones():
        print("Bienvenido al gestor de datos")
        print("1- Agregar datos")
        print("2- Mostrar datos")
        print("3- Eliminar datos")
        print("4- Salir")
        
        #creamos una lista vacia
        datos = []

        while True:
            opcion = input("Ingrese una opcion: ")

            #Validación de error
            try:
                opcion = int(opcion)
                if opcion not in [1, 2, 3, 4]:
                    print("Por favor, selecciona una opción válida.")
                    continue
            except ValueError:
                print("Por favor, ingresa una opción válida.")
                continue
            except SyntaxError:
                print("Por favor, ingresa una opción válida.")
                continue
            
            #Crear un usuario y contraseña
            if opcion == 1:
                    mail = input("Ingrese su usuario: ")
                    password = input("Ingrese su contraseña: ")
                    #Verifica que los campos no esten vacios
                    if mail == "" or password == "":
                     print("Por favor, ingrese datos validos")
                    elif any(dato["user"] == mail for dato in datos):
                        print("El usuario ya existe. Ingrese uno diferente.")
                    else:    
                        #Guardamos los datos en la lista
                        datos.append({
                            "user": mail, 
                            "password": password
                            })
                        print("¡Datos guardados con éxito!")
            
            #Mostrar lista 
            if opcion == 2:
                if datos:
                    print("Lista de usuarios:")
                    for dato in datos:
                        print(f'Usuario: {dato["user"]}, Contraseña: {dato["password"]}')
                else: 
                    print(f'No hay datos guardados')

            #Borrar un usuario
            if opcion == 3:
                if datos:
                    advertencia = input("¿Estás seguro que querés eliminar los datos? S/N ")
                    if advertencia == "S":
                        datos.clear()
                        print("¡Datos eliminados!")
                    elif advertencia == "N":
                            print("¡Operación cancelada!")
                    else:
                        print("Opción no valida.")
                else:
                    print("No hay datos para eliminar")         
            #Salir del programa
            if opcion == 4:
                print("Saliendo del sistema...")   
                break             



#Llama a la funcion
opciones()








