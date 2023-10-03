import random

print("🏴‍☠️ LA BÚSQUEDA DEL TESORO PERDIDO 🏴‍☠️")

texto_largo1 = """\nEl valiente explorador, que ha oído hablar de un antiguo tesoro perdido en una isla misteriosa, 
llamada la Isla del Suspiro; ha decidido ir su busca con un mapa antiguo en mano y un espíritu indomable. Se aventurará a través de densas 
junglas y peligrosas cuevas en busca de riquezas inimaginables. El objetivo del juego será guiar al jugador a través de la búsqueda del tesoro 🔍💎."""
print(texto_largo1)

player_name = input("\nEscriba el nombre de el/la valiente explorador/a 🕵🏼‍♀️🕵🏼‍♂️: ")
player_location = "Jungla 🍃"
objective = "Encontrar el tesoro perdido en la Isla del Suspiro 💎"

texto_largo2 = """\nMientras exploras la jungla en busca del tesoro en la Isla del Suspiro, 
te encuentras frente a una puerta misteriosa. En ella, encuentras una inscripción que dice: 
'Para avanzar, adivina el número secreto que hay en mi corazón'. Te das cuenta de que debes adivinar 
un número para continuar tu búsqueda del tesoro. Frente a la puerta, ves un panel con un teclado numérico y 
un rango de números posibles del 1 al 10, ambos incluidos. Tu misión ahora es descifrar el número correcto y 
desbloquear el camino hacia el tesoro perdido. 🍃🌴🌳"""
print(texto_largo2)

numero_aleatorio = random.randint(1, 10)

tiro = int(input("\n¿Cuál es el número secreto que hay en mi corazón " + player_name + " ? 🤍 "))

while tiro != numero_aleatorio:
    tiro = int(input("¿Cuál es el número secreto? 🤫 "))

print("\n¡Lo has descifrado! 😄 ¡Puedes pasar, pero ve con cuidado! 😰 ")

print(f"\nAhora que ya has pasado la primera pista y sigues en la {player_location} 🍃.")
print(f"Tu objetivo es: {objective} 🔍")

texto_largo3 = """\nTe encuentras en medio de la densa jungla, en busca del legendario tesoro. Frente a ti, tienes dos opciones: 
1) Explorar los rincones ocultos de la jungla o, 
2) Seguir el mapa antiguo que tienes en tu posesión. 
Tu elección determinará el curso de tu aventura. ¿Qué vas a hacer? 🤔 """
print(texto_largo3)

player_choice = int(input("\nElige el número 1 o 2 en función de tu elección: "))

texto_largo4 = """\nMientras te adentras en los densos y misteriosos rincones de la jungla en busca del tesoro de la isla, 
te encuentras frente a dos antiguas estatuas cubiertas de enredaderas. Cada estatua sostiene un pergamino con un enigma. 
Resolver estos dos acertijos es la clave para avanzar en tu búsqueda del tesoro."""

texto_largo5 = """\nSiguiendo el mapa antiguo con determinación, llegas a una bifurcación en el camino. Frente a ti, 
ves una extraña puerta con inscripciones enigmáticas. En el mapa, hay una pista que dice: 'La respuesta a tu destino 
se encuentra en la mente'. La respuesta correcta te llevará por el camino correcto hacia el tesoro perdido."""

if player_choice == 1:
    print(texto_largo4)
    print("Acertijo 1: \n¿En qué momento será correcta la operación 11 + 3 = 2? ")
    respuesta1 = input("\nEscribe tu respuesta: 'Será correcta la operación si pensamos en...' 🕖 ")
    while respuesta1.lower() != "horas":
        respuesta1 = input("Has fallado, inténtalo de nuevo: ")
    print("\n¡Has acertado el primer acertijo! 😄 \n")

    print("Acertijo 2: \n'Corren más que los minutos pero nunca llegan los primeros.' ¿Qué son? ")
    respuesta2 = input("\nEscribe tu respuesta: 'Los...' 🕖 ")
    while respuesta2.lower() != "segundos":
        respuesta2 = input("Has fallado, inténtalo de nuevo: ")
    print("\n¡Has acertado nuevamente! ¡Estás muy cerca de encontrar el tesoro! 😄 ")

elif player_choice == 2:
    print(texto_largo5)
    print("\nLas inscripciones en la puerta dicen: '¿Qué es tan frágil como el cristal, pero si lo rompes, no puedes arreglarlo?' ")
    respuesta3 = input("\nEscribe tu respuesta: 'La...' 🤗 ")
    while respuesta3.lower() != "confianza":
        respuesta3 = input("Has fallado, inténtalo de nuevo: ")
    print("\n¡Has acertado! 😄 ")

else:
    print("Elección no válida. Inténtalo de nuevo.")


print("Ahora que ya has pasado varios obstáculos, cada vez estás más cerca de encontrar el tesoro perdido. 🔍💎\n")
print("Tras varias horas avanzando por el camino de la isla, finalmente llegas a una bifurcación.")
print("Las paredes de la cueva en la que te acabas de adentrar están cubiertas de musgo y las antorchas parpadean con una luz tenue. 🔥")
print("Frente a ti, ves dos puertas de aspecto antiguo talladas en piedra. 🚪🚪")
print("Cada puerta parece llevar a un destino desconocido.")
print("Debes tomar una decisión y elegir sabiamente, " + player_name + ".")
print("¿Serás capaz de encontrar el tesoro perdido? ¡El destino está en tus manos! 🧐\n ")

eleccion = input("¿Elegir la puerta de la izquierda (1) o la puerta de la derecha (2)? ")

while eleccion != "2":
        print("\nHas elegido la puerta de la izquierda.")
        print("Al abrirla, encuentras una habitación vacía. Debes regresar y tomar la otra puerta. 🤯 ")
        eleccion = input("\n¿Eliges la puerta de la izquierda (1) o la puerta de la derecha (2)? ")

if eleccion == "2":
    print("\nHas elegido la puerta de la derecha.")
    print("\n¡Felicidades, has encontrado el tesoro perdido de la Isla del Suspiro! 🤩🎉")
    print("Gracias por jugar, " + player_name + ". ¡Espero que hayas disfrutado de la búsqueda del tesoro! 🤭")
