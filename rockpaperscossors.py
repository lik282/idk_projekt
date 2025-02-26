import random
options = ("rock", "paper", "scissors")


is_running = True

while is_running:

    player = None
    machine = random.choice(options)

    
    while player not in options:
        player = input("ROCK PAPER OR SCISSORS? ").lower()


    print(f"PLAYERS CHOICE :{player}")
    print(F"MACHINES CHOICE :{machine}")

    
        
    if player == machine:
        print("ITS A TIE  ")
    elif player == "rock" and machine == "paper":
        print("MACHINE WINS") 
    elif player == "rock" and machine == "scissors":
        print("PLAYER WINS")
    elif player == "paper" and machine == "rock":
        print("PLAYER WINS")
    elif player == "paper" and machine == "scissors":
        print("MACHINE WINS")
    elif player == "scissors" and machine == "rock":
        print("MACHINE WINS")
    elif player == "scissors" and machine == "paper":
        print("PLAYER WINS")
    
    play_again = input("WANNA PLAY AGAIN? (y/n)").lower()
    if not play_again == "y" or "yes":
        is_running = False

print("THANKS FOR PLAYING!")