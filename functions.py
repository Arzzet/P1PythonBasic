import random

#----------------- Main menu -----------------
# Main menu
def main():
    opcion = "-1"
    while(opcion == "-1"):
        print("1. Adivina el número")
        print("2. Piedra, Papel o Tijera")
        print("3. Ahorcado")
        print("4. Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            adivinaNumero()
            
        elif opcion == "2":
            piedraPapelTijera()
            
        elif opcion == "3":
            ahorcado()
            
        elif opcion == "4":
            print("Saliendo...")
        else:
            print("Opción no válida")
        opcion = "-1"
        
        
        
# ----------------- Adivina numero -----------------
# Adivina el número: Funcion principal para el loop del juego, genera un numero aleatorio, declara las variables del funcionamiento y pide numero al usuario. Luego printa los mensajes de fin de juego.
def adivinaNumero():
    number = random.randint(1, 1000)
    print("Adivina el número entre 1 y 1000")
    guessed = False
    intents = 0
    while(guessed == False and intents < 10):
        intents, guessed = checkNumber(intents, number)
            
    print(f"El número era: {number}")
    print("Fin del juego")
    print("Pulse una ENTER para continuar...")
    input()
    
# Adivina numero: Funcion auxiliar realizar las comprobaciones del input del usuario e imprimir los mensajes correspondientes. 
# Retorna el acierto y el numero de intentos para rellamar la funcion dentro del loop del juego usando las variables
def checkNumber(intents, number):
    guess = input("Adivina el número: ")
    guess = checkType(guess)
    if intents == 10:
        print("Has perdido")
    if guess == number:
        print("Has acertado")
        return intents, True
    elif guess > number:
        print("El número es menor")
        intents += 1
        print(f"Te quedan {10 - intents} intentos\n")
    else:
        print("El número es mayor")
        intents += 1
        print(f"Te quedan {10 - intents} intentos\n")
    return intents, False

# Adivina numero: Funcion auxiliar para comprobar que el input del usuario es un numero y no un string, de lo contrario notifica al usuario y vuelve a pedir el input
def checkType(guess):
    while not guess.isnumeric():
        print("El valor introducido no es un número\n")
        guess = input("Adivina el número: ")
    return int(guess)




# ----------------- Piedra, papel o tijera -----------------
# Funcion principal del juego, inicializa las variables y mantiene el loop del juego hasta que hay un ganador.
def piedraPapelTijera():
    print("Piedra, Papel o Tijera")
    valueOptions = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
    pptgame = True
    playerPoints = 0
    pythonPoints = 0
    while(pptgame):
        # Pide input al usuario.
        print("Escoge una opción\n" +
        "1. Piedra\n"+
        "2. Papel\n"+
        "3. Tijera\n")
        
        choice = input("Escoge una opción: ")
        
        # Python elige un de las opciones al azar
        pythonChoice = random.choice(["Piedra", "Papel", "Tijera"])
        
        # se compprueba el resultado y se actualizan los puntos
        playerPoints, pythonPoints  = checkResult(choice, pythonChoice, playerPoints, pythonPoints)
        pptgame = resolveGame(playerPoints, pythonPoints)
    print ("Press ENTER to continue...")
    input()
        
# Funcion que compara las elecciones para asignar los puntos
def checkResult(choice, pythonChoice, playerPoints, pythonPoints):
    if choice == "1":
        choice = "Piedra"
        if choice == pythonChoice:
            print("Empate - Ambos habeis escogido Piedra")
        elif pythonChoice == "Papel":
            print("Has perdido - Python habia escogido Papel")
            pythonPoints += 1
        else:
            print("Has ganado - Python habia escogido Tijera")
            playerPoints += 1
    elif choice == "2":
        choice = "Papel"
        if choice == pythonChoice:
            print("Empate - Ambos habeis escogido Papel")
        elif pythonChoice == "Tijera":
            print("Has perdido - Python habia escogido Tijera")
            pythonPoints += 1
        else:
            print("Has ganado - Python habia escogido Piedra")
    elif choice == "3":
        choice = "Tijera"
        if choice == pythonChoice:
            print("Empate - Ambos habeis escogido Tijera")
        elif pythonChoice == "Piedra":
            print("Has perdido - Python habia escogido Piedra")
            pythonPoints += 1
        else:   
            print("Has ganado - Python habia escogido Papel")
            playerPoints += 1
    else:
            print("Opción no válida")
    return playerPoints, pythonPoints

# Funcion que determina el resultado de la partida y devuelve True or False para romper o continuar el loop del juego
def resolveGame(playerPoints, pythonPoints):
    print(f"vais {playerPoints} - {pythonPoints}\n")
    if pythonPoints == 3:
        print("Has perdido el juego")
        return False
    elif playerPoints == 3:
        print("Has ganado el juego")
        return False
    else:
        return True




#----------------- Ahorcado -----------------
# Definimos las variables necesarias, python escoge una palabra al azar y se construyen los "_" del "tablero"
def ahorcado():
    # TODO importar las palabras de un csv
    wordList = ["hola", "adios", "python", "programacion", "juego", "ahorcado", "pinzas", "luna", "Pozo", "Playa", "Leyenda", "Colorado", "Encorvar", "Asfalto", "Partir", "Carnada", "Casillero", "Encadenado", "Genio", "Frasco", "Enfermo", "Movimiento", "Herida", "Bola", "Diagonal", "Copiar", "Varita", "Tristeza", "Cubrir", "Erosión"]
    word = random.choice(wordList).lower()
    wordprint = []
    for i in range(len(word)):
        wordprint.append("_")
    errors = []
    figure = {0: "\n", 1: "\n\n\n\n  \ ", 2: "\n\n\n\n/ \ ", 3: "\n\n\n | \n/ \ ", 4: "\n\n\n |\ \n/ \ ", 5: "\n\n\n/|\ \n/ \ ", 6: "\n\n O \n/|\ \n/ \ ", 7: "  ___\n |\n O \n/|\ \n/ \ "}
    
    # Iniciamos el loop principal del juego donde llamamos a las funciones auxiliares
    while len(errors) <= 7 and "_" in wordprint:
        printStatus(figure, wordprint, errors)
        letter = input("Introduce una letra: ").lower()
        if letter in wordprint:
            print("Ya tienes esa letra como correcta, fíjate un poco...")
        elif letter in word:
            for i in range(len(word)):
                if letter == word[i]:
                    wordprint[i] = letter
        else:
            if letter in errors:
                print("Ya has introducido esa letra, y fallaste, fíjate un poco...")
            else:
                errors.append(letter)
        if "_" not in wordprint:
            print(f"Muy bien, la palabra era {word}")
            print("Has ganado")
            
            
        elif len(errors) == 7:
            print("Has perdido")
            print(f"La palabra era: {word}")
            printStatus(figure, wordprint, errors)
            
    return

# Funcion para imprimir el estado del muñeco y el tablero y las letras erroneas
def printStatus(figure, wordprint, errors):
    print("\nTu muñeco está así:")
    print(f"{figure[len(errors)]}\n")
    print(wordprint)
    print(f"Letras erróneas:  {errors}\n")

ahorcado()