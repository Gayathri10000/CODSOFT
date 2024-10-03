import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice: #if tie happen between the user and the computer
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \ #if the user is choice rock while the computer choice the scissors 
         (user_choice == 'scissors' and computer_choice == 'paper') or \ # if the the ueser is choice the scissors and the computer choice the paper
         (user_choice == 'paper' and computer_choice == 'rock'): #if user choice paper and the rock by the computer then the user wins if not then the computer wins.
        return "You win!"
    else:
        return "You lose!"

# Function to play one round of Rock-Paper-Scissors
def play_round(): 
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower() #the .lower() is used for the print the all option in lower case
    
    while user_choice not in choices:
        user_choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower() 
    
    computer_choice = random.choice(choices) #random is used so the computer will get the random value from the choice list
    
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    return result

# Function to play the game with score tracking
def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while True:
        print(f"\n--- Round {round_number} ---")
        result = play_round()
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"\nScores - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
        
        round_number += 1
    
    print("\nFinal Scores:")
    print(f"You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")

# Start the game
play_game()
