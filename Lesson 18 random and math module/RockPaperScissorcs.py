import random
while True:
    user_action = input("Enter a choice(Rock,Paprer,Scissors):")
    possible_actions = ["Rock","Paper","Scissors"]
    computer_actions = random.choice(possible_actions)
    
    print(f"\nYou choose{user_action}computer chose{computer_actions}.\n")

    if user_action == computer_actions:
        print(f"Both players selected {user_action}.Its a tie!")
    elif user_action == "Rock":
        if computer_actions == "Scissors":
            print("Rock smashes scissors. You Win!")
        else:
            print("Paper covers Rock. You Lose")
    elif user_action == "Paper":
        if computer_actions == "Rock":
            print("Paper covers rock. You Win!")
        else:
            print("Scissors cuts Paper. You Lose")
    elif user_action == "Scissors":
        if computer_actions == "Paper":
            print("Scissors cuts Paper. You Win!")
        else:
            print("Rock smashes Scissors. You Lose")

        play_again = input("Play again? (y/n)")
        if play_again != "y":
            break


    


