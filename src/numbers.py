import random

print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar un número del 1 al 100")
print("Escribe 'Salir' para abandonar el juego")

# Número secreto de la máquina
numero_secreto = random.randint(1, 200)

# Contador
i = 10

# Bucle
while True:
    numero_ingresado = input("Ingrese un número para iniciar un juego o escriba 'salir' para finalizar: ")

    if numero_ingresado.lower() == "salir":
        print(f'Que lastima, el numero secreto era {numero_secreto}')
        break

    #Controlar errores
    try:
        numero_ingresado = int(numero_ingresado)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    #Si gana el juego
    if numero_ingresado == numero_secreto:
        if i == 10:  # El usuario lo logró al primer intento
            print("¡Felicidades, lo lograste a la primera!")
        else:
            print(f'¡Felicidades, lo lograste! despues de {10 - i} intentos')
        break
    else:
        i -= 1
        if i == 0:
            print(f'Oh oh, se te terminaron las oportunidades:( el numero secreto era {numero_secreto}')
            break

    #Pistas para el usuario   
    if numero_ingresado > numero_secreto:
        print("El numero es mayor al numero secreto")
    else:
        print("El numero es menor al numero secreto")

    
    print(f"Te quedan {i} intentos")

    

    

    
