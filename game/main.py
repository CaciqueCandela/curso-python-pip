import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('👊piedra, 🖐papel o ✌tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opcion no es valida.')
        # continue
        return None, None

    computer_option = random.choice(options) # También podemos usar una lista en lugar de una tupla.

    print('Turno del usuario =>', user_option)
    print('Turno de la computadora =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('¡Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera.')
            print('¡Esta partida la gana el usuario!')
            user_wins += 1
        else:
            print('Papel gana a piedra.')
            print('¡Esta partida la gana la computadora!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra.')
            print('¡Esta partida la gana el usuario!')
            user_wins += 1
        else:
            print('Tijera gana a papel.')
            print('¡Esta partida la gana la computadora!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel.')
            print('¡Esta partida la gana el usuario!')
            user_wins += 1
        else:
            print('Piedra gana a tijera.')
            print('¡Esta partida la gana la computadora!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
          
        print('Victorias de la computadora:', computer_wins)
        print('Victorias del usuario:', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('*' * 10)
            print('¡La computadora gana el juego!')
            print('*' * 10)
            break

        if user_wins == 2:
            print('*' * 10)
            print('¡El usuario gana el juego!')
            print('*' * 10)
            break
        
run_game()