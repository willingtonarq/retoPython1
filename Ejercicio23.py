#Ejercicio #23 (Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10, dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales).

# Definimos el número preestablecido que el usuario debe adivinar
print("Bienvenido al juego de adivinar el número.")
print("He pensado en un número entre 1 y 10.")
print("Tienes 3 intentos para adivinarlo. ¡Buena suerte!")

numero_preestablecido = 7  # Este es el número que el usuario debe adivinar

while True:
    # Inicializamos el contador de intentos
    intentos = 0

    # Bucle para permitir al usuario hacer hasta 3 intentos
    while intentos < 3:
        # Pedimos al usuario que ingrese su intento
        intento_usuario = int(input(f"Intento {intentos + 1}: Ingresa un número entre 1 y 10: "))

        # Verificamos si el intento es correcto
        if intento_usuario == numero_preestablecido:
            print("¡Felicidades! Has adivinado el número.")
            break  # Salimos del bucle si el usuario adivina correctamente

        else:
            print("Intenta nuevamente.")
            intentos += 1  # Incrementamos el contador de intentos

    # Verificamos si el usuario ha agotado sus intentos
    if intentos == 3:
        print(f"Lo siento, has agotado tus intentos. Intentalo de nuevo.")
        
    # Preguntamos al usuario si quiere jugar de nuevo
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente != 's':
        print("Gracias por jugar. ¡Hasta luego!")
        break  # Salimos del bucle principal si el usuario no quiere jugar nuevamente
    else:
        print("¡Comencemos de nuevo!")
        # Reiniciamos el contador de intentos para la nueva partida
        intentos = 0


