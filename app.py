import random

# Juego piedra, papel o tijera

# Especificaciones:

    # La roca gana a las tijeras.
    # Las tijeras ganan al papel.
    # El papel gana a la piedra.

# A tener en cuenta


    # El jugador podrá elegir una de las tres opciones, piedra, pepel o tijeras, y se le debería advertir en caso de introducir una opción no válida.
    # En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
    # Al final de cada ronda, el jugador elegirá si vuelve a jugar.
    # Muestra la puntuación del jugador al final del juego.
    # El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.
    # El juego debe de ser multijugador, donde el ordenador será su oponente y podrá elegir aleatoriamente uno de los elementos (piedra, pepel o tijeras) por cada movimiento, al igual que usted. La interacción con el juego será a través de la consola 

def get_user_choice():
    while True:
        user_choice = input("Elige piedra, papel o tijeras: ").lower()
        if user_choice in ["piedra", "papel", "tijeras"]:
            return user_choice
        else:
            print("Opción no válida. Por favor, elige piedra, papel o tijeras.")

def get_computer_choice():
    choices = ["piedra", "papel", "tijeras"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (user_choice == "piedra" and computer_choice == "tijeras") or (user_choice == "tijeras" and computer_choice == "papel") or (user_choice == "papel" and computer_choice == "piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Tú elegiste: {user_choice}")
        print(f"El oponente eligió: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "Ganaste":
            user_score += 1
        elif result == "Perdiste":
            computer_score += 1

        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != "s":
            break

    print(f"Puntuación final: Tú {user_score} - {computer_score} Oponente")

play_game()
