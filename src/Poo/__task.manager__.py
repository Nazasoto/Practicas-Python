# Sistema de Gestor de Tareas
import json
from datetime import datetime, timedelta

class Tareas:
    def __init__(self, titulo, descripcion, prioridad, estado="Pendiente", fecha_vencimiento=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.fecha_creacion = datetime.now()
        self.fecha_vencimiento = fecha_vencimiento

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "estado": self.estado,
            "fecha_creacion": self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            "fecha_vencimiento": self.fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_vencimiento else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            prioridad=data["prioridad"],
            estado=data["estado"],
            fecha_vencimiento=datetime.strptime(data["fecha_vencimiento"], '%Y-%m-%d %H:%M:%S') if data["fecha_vencimiento"] else None
        )

    def __str__(self):
        vencimiento = (self.fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S')
                       if self.fecha_vencimiento else "Sin vencimiento")
        return (f"Tarea: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Estado: {self.estado}\n"
                f"Fecha de creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Fecha de vencimiento: {vencimiento}\n")

class GestorTareas:
    def __init__(self):
        self.tareas = []

    #Función para cargar las tareas
    def cargar_tareas(self):
        try:
            with open("tareas.json", "r") as archivo:
                datos = json.load(archivo)
                self.tareas = [Tareas.from_dict(tarea) for tarea in datos]
        except FileNotFoundError:
            print("No se encontró el archivo de tareas. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("El archivo de tareas tiene un formato incorrecto. No se pudieron cargar las tareas.")
    #funcion para guardar las tareas
    def guardar_tareas(self):
        with open("tareas.json", "w") as archivo:
            json.dump([tarea.to_dict() for tarea in self.tareas], archivo)

    #Función para agregar tarea
    def agregar_tarea(self):
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea (Alta, Media, Baja): ")

        vencimiento = input("¿Desea agregar una fecha de vencimiento? (s/n): ").lower()
        if vencimiento == "s":
            try:
                fecha_vencimiento = datetime.strptime(
                    input("Ingrese la fecha de vencimiento (YYYY-MM-DD HH:MM): "), '%Y-%m-%d %H:%M')
            except ValueError:
                print("Formato de fecha inválido. No se agregará fecha de vencimiento.")
                fecha_vencimiento = None
        else:
            fecha_vencimiento = None

        nueva_tarea = Tareas(titulo, descripcion, prioridad, fecha_vencimiento=fecha_vencimiento)
        self.tareas.append(nueva_tarea)
        self.guardar_tareas()
        print(f"\nTarea '{titulo}' agregada correctamente.")
    #Función para ver lista de tareas
    def listar_tareas(self):
        if not self.tareas:
            print("\nNo hay tareas registradas.")
            return
        print("\nTareas registradas:")
        for tarea in self.tareas:
            print(tarea)
    #Función para verificar fechas vencidas
    def verificar_fechas_vencidas(self):
        fecha_actual = datetime.now()
        tareas_vencidas = False

        for tarea in self.tareas:
            if tarea.fecha_vencimiento and tarea.fecha_vencimiento < fecha_actual:
                tarea.estado = "Vencida"
                print(f'La tarea "{tarea.titulo}" ha sido marcada como vencida.')
                tareas_vencidas = True

        if not tareas_vencidas:
            print("No hay tareas vencidas.")
    #Función para eliminar tarea
    def eliminar_tarea(self):
        opcion = input("¿Desea eliminar una tarea o todas las tareas? (una/todas): ").lower()

        if opcion == "una":
            titulo = input("Ingrese el título de la tarea: ").strip()
            tarea_encontrada = False

            for tarea in self.tareas:
                if tarea.titulo.lower() == titulo.lower():  
                    self.tareas.remove(tarea)
                    print(f"Tarea '{titulo}' eliminada correctamente.")
                    tarea_encontrada = True
                    break  

            if not tarea_encontrada:
                print(f"No se encontró ninguna tarea con el título '{titulo}'.")

        elif opcion == "todas":
            confirmacion = input("¿Está seguro de que desea eliminar todas las tareas? (s/n): ").lower()
            if confirmacion == "s":
                self.tareas = []  # Vaciar la lista
                print("Todas las tareas han sido eliminadas.")
            else:
                print("Operación cancelada. No se eliminaron las tareas.")

        else:
            print("Opción inválida. Por favor, ingrese 'una' o 'todas'.")
    #Función para editar
    def editar_tarea(self):
        titulo = input("Ingrese el título de la tarea a editar: ").strip()
        tarea_encontrada = None

        #Buscar tarea 
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea_encontrada = tarea
                break

        if not tarea_encontrada:
            print(f"No se encontró ninguna tarea con el título '{titulo}'.")
            return

        #Mostrar información de la tarea actual
        print("\nInformación actual de la tarea:")
        print(tarea)

        nuevo_titulo = input("Ingrese el nuevo título de la tarea (dejar en blanco para mantener el actual): ").strip()
        if nuevo_titulo:
            tarea_encontrada.titulo = nuevo_titulo

        nueva_descripcion = input("Ingrese la nueva descripción de la tarea (dejar en blanco para mantener la actual): ").strip()
        if nueva_descripcion:
            tarea_encontrada.descripcion = nueva_descripcion
        
        while True:
            nueva_fecha_de_vencimiento = input("Ingrese la nueva fecha de vencimiento (YYYY-MM-DD HH:MM) (dejar en blanco para mantener la actual): ").strip()
            if not nueva_fecha_de_vencimiento:
                break
            try:
                tarea_encontrada.fecha_vencimiento = datetime.strptime(nueva_fecha_de_vencimiento, '%Y-%m-%d %H:%M')
                break
            except ValueError:
                print("Formato de fecha inválido. Intente nuevamente.")

        #Cancelar operación 
        print(f'Los cambios que se han hecho hasta ahora son: {tarea_encontrada}')
        confirmacion = input("¿Está seguro de que desea guardar los cambios? (s/n): ").lower()
        if confirmacion != "s":
            print("Operación cancelada. Los cambios no han sido guardados.")
            return
        else:
            print(f"\nTarea '{tarea_encontrada.titulo}' actualizada correctamente.")
            print(tarea_encontrada)

    #Función para buscar por prioridad o estado 
    def buscar_tarea(self):
        opcion = input("¿Qué tipo de tarea desea buscar? (prioridad/estado): ").lower()

        if opcion not in ["prioridad", "estado"]:
            print("Opción inválida. Debe elegir 'prioridad' o 'estado'.")
            return

        # Determinar el criterio de búsqueda
        if opcion == "prioridad":
            criterio = input("Ingrese la prioridad de la tarea (Alta, Media, Baja): ").lower()
            tareas_encontradas = [tarea for tarea in self.tareas if tarea.prioridad.lower() == criterio]
        elif opcion == "estado":
            criterio = input("Ingrese el estado de la tarea (Pendiente, En progreso, Completada, Vencida): ").lower()
            tareas_encontradas = [tarea for tarea in self.tareas if tarea.estado.lower() == criterio]

        # Mostrar resultados
        if tareas_encontradas:
            print(f"\nTareas encontradas con {opcion} '{criterio}':")
            for tarea in tareas_encontradas:
                print(tarea)
        else:
            print(f"No se encontraron tareas con {opcion} '{criterio}'.")


def menu():
    gestor = GestorTareas()
    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Ver lista de tareas")
        print("3. Verificar fechas vencidas")
        print("4. Eliminar tarea")
        print("5. Editar tarea")
        print("6. Buscar tarea")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        try:
            opcion = int(opcion)

            if opcion == 1:
                gestor.agregar_tarea()
            elif opcion == 2:
                gestor.listar_tareas()
            elif opcion == 3:
                gestor.verificar_fechas_vencidas()
            elif opcion == 4:
                gestor.eliminar_tarea()
            elif opcion == 5:
                gestor.editar_tarea()
            elif opcion == 6:
                gestor.buscar_tarea()
            elif opcion == 7:
                print("Saliendo del programa")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

menu()


            
