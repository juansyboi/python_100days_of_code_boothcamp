import random

wins = 0
losses = 0
draw = 0
num_games = 0
isContinue = True

moves = ["rock", "paper", "scissor", "exit"]

print("Welcome to Rock Paper Scissor Game \nDirection: Input 0 for 'Rock', 1 for 'Paper', 2 for 'Scissor', and 3 for 'Exit'")

while isContinue:
    # player_choice = int(input(f"What is your moves? "))
    player1 = moves[int(input(f"What is your moves? "))]
    comp = moves[random.randint(0,2)]

    if player1 == comp:
        draw += 1
        num_games +=1
        print(f"Your Moves {player1} vs Computer Moves {comp}")
        print("Draw")
    elif player1 == "exit":
        isContinue = False
        print("\nThank you for playing\n")
        print(f"-------Status-------\nWins: {wins}\nLosses: {losses}\nDraw: {draw}\nGames Played: {num_games}\n")
        break
    elif player1 != comp:
        if player1 == moves[0]:
            if comp == moves[1]:
                losses += 1
                num_games += 1
                print(f"Your Moves {player1} vs Computer Moves {comp}")
                print("You Lose!")
            elif comp == moves[2]:
                wins += 1
                num_games += 1
                print(f"Your Moves {player1} vs Computer Moves {comp}")
                print("You Win!")
        elif player1 == moves[1]:
            if comp == moves[2]:
                losses += 1
                num_games += 1
                print(f"Your Moves {player1} vs Computer Moves {comp}")
                print("You Lose!")
            elif comp == moves[0]:
                wins += 1
                num_games += 1
                print(f"Your Moves {player1} vs Computer Moves {comp}")
                print("You Win!")
        elif player1 == moves[2]:
            if comp == moves[0]:
                losses += 1
                num_games += 1
                print(f"Your Moves {player1} vs Computer Moves {comp}")
                print("You Lose!")
            elif comp == moves[1]:
                wins += 1
                num_games += 1
                print(f"Your Moves {player1} vs Computer Moves {comp}")
                print("You Win!")