import random,time

def determine_winner(user, computer):
    user = user.lower()
    computer = computer.lower()
    if user == computer:
        return 'Draw'
    winning_combinations = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    if computer in winning_combinations.get(user, []):
        return 'user won'
    else:
        return 'computer won'


def game_play():
    is_playing = True
    x = 'WELCOME TO THE GAME \n GAME RULES : \n Rock crushes Scissors \n Scissors cut Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitate the Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock'
    for i in x:
        time.sleep(0.1)
        print(i,end = '',  flush = True)
    print()
    while is_playing:
    
        game = input('do you want to play(y/n)?: ')
        if game == 'y':
            options = ['rock','scissors','paper','lizard','spock']
            computer = random.choice(options)
            user = input("rock,paper,scissors,spock,lizard?: ").lower()

            
        else:
            break
    return 'GAME OVER'
if __name__ == '__main__':    
    print(game_play())